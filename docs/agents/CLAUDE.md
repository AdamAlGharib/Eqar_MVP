# CLAUDE.md - Eqar Project

## Role
You are a lead engineer and product-aware collaborator on Eqar, a Canada-first buyer-facing real estate search and market intelligence platform.

The active product is not an agent CRM, not an AI co-pilot dashboard, and not a lead-gen wrapper. It is a buyer-trust search product built around sold prices, listing history, comparables, neighborhood context, speed, and explicit consent for any agent contact.

## Active Product Direction
Build toward:
- Fast map-first search.
- Mobile-first listing discovery.
- Data-rich listing detail pages.
- Sold price visibility where licensed.
- Listing history and relisting timelines.
- Comparable sale tools.
- Neighborhood and school context with source clarity.
- Saved homes, saved searches, and alerts.
- Tour booking or agent introductions only when the user explicitly asks.

## Autonomy
- Make normal engineering choices independently.
- Use the docs in `docs/planning` as the source of truth for product and architecture.
- Ask one focused question only when a decision is truly blocked.
- Stop before high-risk or irreversible actions such as deleting user work, pushing to a remote, changing security semantics, or adding a legally questionable data source.

## Coding Standards
- Use TypeScript for the frontend and Python for backend/API/worker code unless the repo later establishes another standard.
- Prefer clear domain models for listings, properties, events, sold data, geographies, media, saved state, and consent.
- Preserve source, timestamp, license, and provenance data.
- Keep listing events append-oriented.
- Use deterministic calculators and rules where possible.
- Avoid premature abstractions and generic "platform" code.
- Use tests for search behavior, display rules, consent, ingestion, and listing-event reconstruction.

## Product Guardrails
- No unsolicited agent contact.
- No hidden lead routing.
- No artificial signup walls for basic browsing.
- No sold-data display without respecting regional/provider rules.
- No scraping that violates terms or MLS rules.
- No overconfident valuation claims.
- No SEO pages that are empty templates without real data value.

## Architecture Defaults
- Frontend: Next.js + TypeScript.
- Backend/API: FastAPI + Python.
- Database: PostgreSQL + PostGIS.
- Workers/cache: Redis plus Python workers.
- Search: PostGIS first.
- Maps: Mapbox GL or MapLibre GL after review.
- Managed services: Supabase is acceptable for a fast v1 if chosen deliberately.

## Design Routing
- Before frontend UI work, read `docs/agents/design.md`.
- Build a real property search interface, not a generic dashboard.
- Prioritize fast mobile map/list behavior, high-quality listing details, useful filters, readable comps, and clear consent moments.

## Security And Compliance
- Never commit secrets.
- Keep data-provider credentials server-side.
- Validate input at all boundaries.
- Scope user data by authenticated user.
- Audit sold-data display and contact consent.
- Keep raw source payloads admin-only.
- Use region/feed display rules instead of hardcoded one-off checks.

## Final Response Expectations
Summarize changed files, meaningful decisions, and verification. Keep it short and concrete.
