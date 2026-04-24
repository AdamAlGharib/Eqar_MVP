from typing import Any

from fastapi import APIRouter, Depends

from app.core.settings import Settings, get_settings

router = APIRouter()


@router.get("/health/live")
async def live() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/health/ready")
async def ready(settings: Settings = Depends(get_settings)) -> dict[str, Any]:
    auth_configured = settings.auth_disabled or bool(settings.supabase_jwt_secret)

    return {
        "status": "ok",
        "checks": {
            "auth_configured": auth_configured,
            "openai_configured": bool(settings.openai_api_key),
            "supabase_url_configured": bool(settings.supabase_url),
        },
    }

