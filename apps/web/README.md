# Eqar Web

Private dashboard-first frontend scaffold for Eqar, a Canada-first AI real-estate co-pilot for agents.

## Run locally

```bash
cd apps/web
npm install
npm run dev
```

The app runs on `http://localhost:3000` by default.

## Environment

Copy `env.example` to `.env.local` and fill in:

- `NEXT_PUBLIC_APP_ENV`: local, preview, or production.
- `NEXT_PUBLIC_API_BASE_URL`: FastAPI backend URL.
- `NEXT_PUBLIC_SUPABASE_URL`: Supabase project URL.
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`: Supabase browser anon key.

Do not put service-role keys, OpenAI API keys, or other server secrets in this frontend app.
