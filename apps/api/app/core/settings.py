from functools import lru_cache
from typing import Literal

from pydantic import AnyUrl, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="EQAR_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Eqar API"
    environment: Literal["local", "test", "staging", "production"] = "local"
    api_prefix: str = "/api/v1"
    cors_origins: str = ""

    auth_disabled: bool = False
    supabase_url: AnyUrl | None = None
    supabase_anon_key: SecretStr | None = None
    supabase_service_role_key: SecretStr | None = None
    supabase_jwt_secret: SecretStr | None = None
    supabase_jwt_audience: str = "authenticated"

    openai_api_key: SecretStr | None = None
    openai_model: str = "gpt-4.1-mini"
    openai_embedding_model: str = "text-embedding-3-small"
    redis_url: str | None = None

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

    @model_validator(mode="after")
    def protect_production_auth(self) -> "Settings":
        if self.environment == "production" and self.auth_disabled:
            raise ValueError("EQAR_AUTH_DISABLED cannot be true in production.")
        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()
