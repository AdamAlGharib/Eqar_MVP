# Agent Context - Eqar

This file is shared working memory for AI coding agents on the Eqar project, including Codex and Claude Code. Read it before meaningful project changes and update it after important decisions, reversals, or milestones.

## Current Snapshot
- Project name: Eqar, working name only.
- Repository: `c:\Users\adamg\Documents\RealEstate`.
- Current stage: planning reset / blank-slate implementation.
- Current repo state: docs only; no application source code has been scaffolded in this workspace.
- Product direction: Canada-first buyer-facing real estate search and market intelligence platform.
- Superseded direction: the previous agent AI co-pilot plan is no longer the active product.

## Active Product Thesis
Eqar should be the Canadian real estate search product that behaves like it is on the buyer's side.

The product combines:
- Map-first search.
- Sold price visibility where legally/licensed.
- Listing history, relisting, price-drop, and sold-event timelines.
- Comparable sale tooling.
- Neighborhood and school context with sources.
- Predicted sale price later, only with real model evaluation and confidence bands.
- Mobile-first speed and usability.
- Agent/tour contact only after explicit user action.

Working positioning:
- Search like a buyer, not like a lead.
- No agent harassment.
- Serious data depth without dark-pattern signup walls.

## Primary Users
- Serious Canadian buyers.
- Buyer-investors.
- Sellers researching local comps before listing.

Secondary:
- Casual browsers from SEO pages.
- Agents who receive explicit user-requested referrals or tour requests.

Agents are not the primary customer in the active plan.

## Product Principles
- Buyer trust first.
- Browsing, saving, viewing sold data, or reading SEO pages must not trigger agent contact.
- Sold data is a core feature, not a teaser.
- Signup gates should exist only for saved state, alerts, explicit contact workflows, or true legal/data-provider requirements.
- Every data point should preserve source/provenance where practical.
- Every estimate should include assumptions and uncertainty.
- Mobile performance matters as much as desktop polish.
- Monetization must not recreate the lead-gen incentives the product is trying to avoid.

## Technical Direction
Current defaults:
- Frontend: Next.js + TypeScript.
- Backend/API: FastAPI + Python.
- Database: PostgreSQL + PostGIS.
- Managed v1 option: Supabase for Postgres, Auth, and Storage where useful.
- Queue/cache: Redis plus Python workers.
- Search: Postgres/PostGIS first, then OpenSearch/Typesense only if needed.
- Maps: Mapbox GL or MapLibre GL, pending cost/licensing decision.
- Deployment: Vercel for web, managed API/worker hosting, managed Postgres.

Core architecture:
- Store raw source records separately from normalized properties/listings.
- Build append-oriented listing event history.
- Model sold-data display permissions by region/feed/rule version.
- Model user contact consent explicitly.
- Keep valuation models out of v1 until backtesting and confidence bands exist.

## High-Risk Areas
- MLS, sold-data, listing-photo, and historical-data licensing.
- Regional display rules for sold prices and addresses.
- Data completeness and freshness.
- Duplicate property/listing matching.
- Geocoding accuracy.
- SEO pages becoming thin or violating listing terms.
- Valuation estimates becoming overconfident.
- Lead-gen pressure eroding product trust.

## Guardrails For Agents
- Do not rebuild the old agent co-pilot plan.
- Do not add an LLM/chatbot as a core v1 feature unless the user explicitly redirects.
- Do not propose scraping protected real estate sites or MLS data without terms/licensing review.
- Treat source licensing and sold-data display as first-class architecture.
- Preserve provenance, timestamps, and rule versions in data-model proposals.
- Keep contact flows opt-in and auditable.
- Optimize product surfaces for buyers and market researchers first.

## Suggested First Build Slice
After planning is accepted, build a thin vertical slice:
- Next.js search page.
- FastAPI search endpoint.
- Postgres/PostGIS schema for geographies, properties, listings, listing versions, listing events, media, users, saved homes, and saved searches.
- Seeded demo data.
- Map/list search with filters.
- Listing detail with photo gallery, property facts, event timeline, and source timestamp.
- Saved home/search behind auth.

Do not block this slice on real MLS feed access. Use permitted demo/seed data while the data access path is resolved.

## Open Questions
- Final product name.
- First Canadian region.
- Exact MLS/sold-data access path.
- Map provider: Mapbox or MapLibre.
- Auth provider: Supabase Auth, Clerk, or Auth.js.
- Whether Supabase should be the managed production database or only a fast-start option.
- Initial monetization timing.

## Progress Log
- 2026-04-26: Reset docs from an agent AI co-pilot plan to a buyer-first Canadian real estate search and market intelligence plan.
- 2026-04-26: Replaced the technical architecture with a geospatial search, listing-history, sold-data permissions, and opt-in consent architecture.
- 2026-04-26: Updated agent context to mark the old agent-dashboard plan as superseded.

## Journal Format
Use this format for future entries:

```md
### YYYY-MM-DD - Agent Name - Short Title
- Type: progress | decision | discovery | correction | risk | future-thought
- Context: What happened or what was learned.
- Impact: Why it matters for future work.
- Next: What the next agent should consider.
```

## Incremental Journal

### 2026-04-26 - Codex - Product Reset
- Type: correction
- Context: The user clarified that the intended product is a buyer-first Canadian search platform inspired by the gap between Zoo Casa, HouseSigma, and Realtor.ca, not the prior agent co-pilot plan.
- Impact: All future planning should center search, sold prices, comps, listing history, mobile UX, data licensing, and explicit consent for agent contact.
- Next: Confirm first region and data access path before real listing ingestion. Build with seeded demo data while those are resolved.
