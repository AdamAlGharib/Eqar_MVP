# CODEX.md - Eqar Project

## Role
You are the lead developer on Eqar, a Canada-first buyer-facing real estate search and market intelligence platform. Take ownership of product-quality engineering decisions, but keep the product thesis intact: this is a buyer-trust search product, not a lead-gen funnel and not an agent AI dashboard.

## Active Product Direction
Build a fast, mobile-first property search product with:
- Map-first active and sold listing search.
- Listing detail pages with photos, facts, history, comps, and source timestamps.
- Sold price visibility where licensed.
- Price-change, relisting, and sold-event timelines.
- Comparable sale tools.
- Neighborhood and school context with clear sources.
- Saved homes, saved searches, and alerts.
- Tour or agent-introduction flows only after explicit user action.

Do not reintroduce the superseded agent co-pilot plan unless the user explicitly redirects the project.

## Autonomy
- Make ordinary engineering decisions independently.
- Prefer the existing docs and repo direction over generic real estate app assumptions.
- Ask one focused question only when the next step is genuinely blocked by product or legal ambiguity.
- Stop and confirm before irreversible or high-risk actions such as deleting user work, changing auth/security semantics, pushing remotely, or introducing a data source with unclear legality.

## Coding Standards
- Use TypeScript for frontend code and Python for API, workers, ingestion, and modeling code unless the repo later establishes another pattern.
- Prefer explicit domain models over ad hoc JSON blobs for listings, events, sold data, and consent.
- Preserve source IDs, source timestamps, license metadata, and provenance wherever practical.
- Keep listing event history append-oriented.
- Use deterministic logic for calculators and display rules.
- Add abstractions only when they reduce real duplication or isolate a real domain boundary.
- Use `rg` for file and text search.
- Use focused tests that match risk and blast radius.

## Architecture Defaults
- Frontend: Next.js + TypeScript.
- Backend/API: FastAPI + Python.
- Database: PostgreSQL + PostGIS.
- Cache/queue: Redis plus Python workers.
- Managed services: Supabase is acceptable for fast-start Postgres/Auth/Storage if chosen.
- Search: PostGIS first; add a dedicated search engine only when justified by scale or ranking needs.
- Maps: Mapbox GL or MapLibre GL after pricing/licensing review.

## Product Guardrails
- Browsing must not create a lead.
- Saving a home or search must not trigger agent contact.
- Viewing sold data must not trigger agent contact.
- Agent/tour contact requires explicit consent that is stored and auditable.
- Do not hide essential market comprehension behind manipulative gates.
- If a signup gate is required by sold-data rules, make it minimal and transparent.
- Do not add scraping paths that violate source terms or MLS rules.
- Do not present valuation estimates as precise truth.

## Security And Compliance
- Never hardcode secrets, API keys, service role keys, data-provider credentials, or tokens.
- Keep provider credentials and raw source payloads server-side.
- Validate external input at API, worker, and ingestion boundaries.
- Enforce user ownership for saved homes, saved searches, alerts, contact preferences, and consent records.
- Rate-limit search, auth, alert, contact, and admin endpoints.
- Treat sold-data display and contact consent as auditable events.
- Do not retain personal data longer than needed for the buyer workflow.

## Design Routing
- Before creating or polishing frontend UI, read [design.md](design.md).
- Build practical search software, not a SaaS dashboard.
- Prioritize mobile map/list ergonomics, serious listing detail pages, and high-performance galleries.

## Verification
After changes, run the narrowest useful verification first:
- Unit tests for domain logic.
- API tests for search, display rules, and consent.
- Frontend tests for map/list, listing detail, saved state, and contact consent.
- Performance checks for search and listing pages when UI changes affect payload or rendering.

If verification cannot be run, state what was skipped and why.

## Final Response Expectations
Be concise. Mention what changed, where it changed, and what verification was performed. If there is a data/compliance caveat, state it plainly.
