from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import chat, health
from app.core.settings import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved_settings = settings or get_settings()

    api = FastAPI(
        title=resolved_settings.app_name,
        version="0.1.0",
        description="Backend API for Eqar's AI real-estate co-pilot.",
    )

    if resolved_settings.cors_origin_list:
        api.add_middleware(
            CORSMiddleware,
            allow_origins=resolved_settings.cors_origin_list,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    api.include_router(health.router, prefix=resolved_settings.api_prefix, tags=["health"])
    api.include_router(chat.router, prefix=resolved_settings.api_prefix, tags=["chat"])

    return api


app = create_app()
