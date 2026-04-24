from app.core.settings import Settings
from app.llm.base import (
    LLMCompletion,
    LLMMessage,
    LLMProviderNotConfigured,
    LLMProviderNotImplemented,
    LLMTool,
)


class OpenAIChatProvider:
    name = "openai"

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    async def complete(
        self,
        messages: list[LLMMessage],
        tools: list[LLMTool],
        metadata: dict[str, str],
    ) -> LLMCompletion:
        if not self._settings.openai_api_key:
            raise LLMProviderNotConfigured("EQAR_OPENAI_API_KEY is required for chat completions.")

        raise LLMProviderNotImplemented(
            "OpenAI provider is scaffolded; wire the live API client after orchestration policy is set."
        )
