from typing import Literal
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field

from app.auth.dependencies import CurrentUser, get_current_user
from app.core.settings import Settings, get_settings
from app.country_packs import UnsupportedCountryPackError, get_country_pack
from app.llm.base import LLMMessage, LLMProviderNotConfigured, LLMProviderNotImplemented, LLMTool
from app.llm.openai_provider import OpenAIChatProvider
from app.tools.registry import build_default_tool_registry

router = APIRouter()


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str = Field(min_length=1, max_length=20_000)


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(min_length=1, max_length=50)
    country: str = Field(default="CA", min_length=2, max_length=2)
    region: str | None = Field(default="ON", max_length=16)
    enable_tools: bool = True


class ChatResponse(BaseModel):
    id: str
    status: Literal["completed", "provider_not_configured", "not_implemented"]
    provider: str
    model: str
    country_pack: str
    available_tools: list[str]
    message: ChatMessage | None = None


@router.post("/chat", response_model=ChatResponse)
async def create_chat_completion(
    request: ChatRequest,
    settings: Settings = Depends(get_settings),
    user: CurrentUser = Depends(get_current_user),
) -> ChatResponse:
    try:
        country_pack = get_country_pack(request.country, request.region)
    except UnsupportedCountryPackError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    registry = build_default_tool_registry()
    available_tool_definitions = [
        tool for tool in registry.list_tools() if tool.name in country_pack.tool_names
    ]
    available_tools = [tool.name for tool in available_tool_definitions]

    provider = OpenAIChatProvider(settings=settings)
    messages = [LLMMessage(role=message.role, content=message.content) for message in request.messages]
    llm_tools = [
        LLMTool(name=tool.name, description=tool.description, input_schema=tool.input_schema)
        for tool in available_tool_definitions
    ]

    try:
        completion = await provider.complete(
            messages=messages,
            tools=llm_tools if request.enable_tools else [],
            metadata={
                "user_id": user.id,
                "country": country_pack.country_code,
                "region": country_pack.region_code,
            },
        )
    except LLMProviderNotConfigured as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
    except LLMProviderNotImplemented as exc:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail=str(exc),
        ) from exc

    return ChatResponse(
        id=str(uuid4()),
        status="completed",
        provider=provider.name,
        model=settings.openai_model,
        country_pack=country_pack.key,
        available_tools=available_tools,
        message=ChatMessage(role="assistant", content=completion.content),
    )
