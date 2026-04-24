# Eqar API

FastAPI backend scaffold for Eqar, a Canada-first AI real-estate co-pilot for agents.

## Setup

```bash
cd apps/api
..\..\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

## Run

```bash
..\..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

The API mounts versioned routes under `/api/v1`.

## Test

```bash
..\..\.venv\Scripts\python.exe -m pytest
```

The current tests cover deterministic real-estate calculators and do not require Supabase,
OpenAI, or network access.

## Environment

Configuration is read from environment variables with the `EQAR_` prefix:

- `EQAR_ENVIRONMENT`: `local`, `test`, `staging`, or `production`.
- `EQAR_CORS_ORIGINS`: comma-separated allowed origins.
- `EQAR_AUTH_DISABLED`: set to `true` only for local development.
- `EQAR_SUPABASE_URL`: Supabase project URL.
- `EQAR_SUPABASE_ANON_KEY`: public Supabase anon key.
- `EQAR_SUPABASE_SERVICE_ROLE_KEY`: server-only Supabase service role key.
- `EQAR_SUPABASE_JWT_SECRET`: JWT secret used to verify Supabase access tokens.
- `EQAR_SUPABASE_JWT_AUDIENCE`: expected JWT audience, defaults to `authenticated`.
- `EQAR_OPENAI_API_KEY`: OpenAI API key for the provider adapter.
- `EQAR_OPENAI_MODEL`: OpenAI model name, defaults to `gpt-4.1-mini`.
- `EQAR_OPENAI_EMBEDDING_MODEL`: embedding model name, defaults to `text-embedding-3-small`.
- `EQAR_REDIS_URL`: Redis URL for future background jobs.

No secrets are committed. Without `EQAR_AUTH_DISABLED=true` or a configured Supabase JWT
secret, authenticated routes fail closed.
