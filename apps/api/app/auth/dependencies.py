from typing import Any

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import InvalidTokenError
from pydantic import BaseModel, Field

from app.core.settings import Settings, get_settings

bearer_scheme = HTTPBearer(auto_error=False)


class CurrentUser(BaseModel):
    id: str
    email: str | None = None
    role: str | None = None
    claims: dict[str, Any] = Field(default_factory=dict)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    settings: Settings = Depends(get_settings),
) -> CurrentUser:
    if settings.auth_disabled:
        return CurrentUser(id="local-dev-user", role="authenticated")

    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing bearer token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not settings.supabase_jwt_secret:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Supabase JWT verification is not configured.",
        )

    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.supabase_jwt_secret.get_secret_value(),
            algorithms=["HS256"],
            audience=settings.supabase_jwt_audience,
            options={"verify_aud": bool(settings.supabase_jwt_audience)},
        )
    except InvalidTokenError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid bearer token.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc

    subject = payload.get("sub")
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer token is missing a subject.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return CurrentUser(
        id=subject,
        email=payload.get("email"),
        role=payload.get("role"),
        claims=payload,
    )

