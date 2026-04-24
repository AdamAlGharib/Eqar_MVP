# Eqar Infrastructure

This directory holds deployment and platform setup notes for the Eqar monorepo.

## Target Services
- Frontend: Vercel, serving `apps/web`.
- Backend API and workers: Render, serving `apps/api`.
- Auth, Postgres, storage, and vector search: Supabase.
- Background queue: Redis-compatible service on Render.

## Environment
Use [env.example](env.example) as the deployment checklist. Real secrets belong in platform secret stores, not in git.

## Supabase
Initial schema work lives under [supabase/migrations](supabase/migrations). Apply migrations through the Supabase CLI or dashboard once a project is created.
