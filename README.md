# Eqar

Eqar is an AI real-estate co-pilot for agents, starting with a Canada-first web SaaS dashboard.

## Project Documents
- Agent instructions: [docs/agents/CODEX.md](docs/agents/CODEX.md) and [docs/agents/CLAUDE.md](docs/agents/CLAUDE.md)
- Shared agent memory: [docs/agents/Agent_Context.md](docs/agents/Agent_Context.md)
- Product plan: [docs/planning/PLAN.md](docs/planning/PLAN.md)
- Technical architecture plan: [docs/planning/TECHNICAL_ARCHITECTURE.md](docs/planning/TECHNICAL_ARCHITECTURE.md)

## Current Structure
```text
apps/
  api/         FastAPI backend and worker code
  web/         Next.js agent dashboard
docs/
  agents/      Agent operating instructions and shared context
  planning/    Product and implementation planning documents
infra/         Deployment, Supabase, and environment setup
packages/
  shared/      Shared TypeScript domain contracts
```

## Local Development
1. Copy `.env.example` into service-specific local env files as needed. For the API, `apps/api/env.example` lists the exact `EQAR_` variables.
2. Install JavaScript dependencies with `npm install`.
3. Run the web app with `npm run dev:web`.
4. Install API dependencies into the project venv with `cd apps/api && ..\..\.venv\Scripts\python.exe -m pip install -e ".[dev]"`.
5. Run the API from `apps/api` with `..\..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload`.
6. Run API tests with `npm run test:api`.

## Verification
- Web typecheck: `npm run typecheck`
- Web lint: `npm run lint:web`
- Web build: `npm run build:web`
- API tests: `npm run test:api`
- API lint: `npm run lint:api`

## Security Notes
- `npm audit` currently reports a residual moderate PostCSS advisory through Next.js 16.2.4's pinned transitive dependency.
- The high-severity Next.js 14 advisories were removed by upgrading to Next.js 16.2.4.
- Do not run `npm audit fix --force` without reviewing the output; npm currently suggests a breaking Next downgrade path.

The first implementation milestone is the foundation scaffold. Supabase project setup and real secrets are intentionally not committed.
