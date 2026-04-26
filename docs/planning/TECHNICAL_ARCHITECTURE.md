# Eqar Technical Architecture

## Summary
Build Eqar as a Canada-first property search and market intelligence platform with a mobile-first web app, geospatial search backend, durable listing-event data model, strict data provenance, and explicit user-consent flows for tours or agent introductions.

The architecture should optimize for:
- Fast map/list search.
- Rich listing detail pages.
- Sold price and comparable sale workflows where data is licensed.
- Listing history reconstruction.
- SEO pages for cities and neighborhoods.
- Data-provider compliance and regional display rules.
- Future valuation models with measurable accuracy and confidence bands.

The old agent co-pilot architecture is superseded. LLM features are not core to v1.

## Chosen Defaults
- Monorepo: apps, packages, docs, infra.
- Frontend: Next.js + TypeScript.
- Backend/API: FastAPI + Python.
- Database: PostgreSQL with PostGIS.
- Managed option for v1: Supabase Postgres, Auth, Storage, and Edge-compatible primitives where helpful.
- Cache/queue: Redis plus Python workers.
- Maps: Mapbox GL or MapLibre GL, selected after pricing and licensing review.
- Search engine: Postgres/PostGIS first; OpenSearch or Typesense only when query load or ranking needs justify it.
- Object storage/CDN: Supabase Storage or S3-compatible storage behind a CDN for listing media and generated assets.
- Deployment: Vercel for web, Render/Fly.io/Railway for API and workers, managed Postgres/Supabase for data.

## Target Repository Layout
```txt
apps/
  web/                 # Next.js buyer-facing app
  api/                 # FastAPI domain API
  workers/             # Ingestion, normalization, alerts, media, model jobs
packages/
  shared/              # Shared schemas, constants, generated API types
  map-utils/           # Geospatial helpers shared by app/API if useful
infra/
  migrations/          # SQL migrations and seed data
  env/                 # Example environment files
  deployment/          # Deployment notes and runbooks
docs/
  agents/              # Agent operating context and design guidance
  planning/            # Product plan and architecture
```

## System Boundaries
### Web App
Responsibilities:
- Public search experience.
- Listing detail pages.
- SEO city/neighborhood pages.
- Account flows for saved homes, saved searches, alerts, and contact preferences.
- Explicit tour and agent-introduction requests.
- Admin surfaces only if needed for internal review.

The browser should not talk directly to private data-provider APIs or expose service credentials.

### API
Responsibilities:
- Search, listing detail, comps, sold history, neighborhoods, schools, saved searches, alerts, and consent records.
- Region-specific display rules.
- Authentication and authorization.
- Listing-event reconstruction endpoints.
- Admin/feed health endpoints.
- OpenAPI contract for generated client types.

### Workers
Responsibilities:
- Feed ingestion.
- Source record normalization.
- Listing/property matching and deduplication.
- Event timeline generation.
- Media processing.
- Saved-search alerts.
- SEO page materialization when useful.
- Valuation model training/inference jobs later.

### Database
Responsibilities:
- Canonical property and listing data.
- Listing event history.
- Sold transactions and display permissions.
- Geospatial indexes.
- User saved state and consent records.
- Feed provenance and audit logs.

## Core Data Model
Use source records and normalized records separately. Never lose provenance.

Primary tables:
- `source_feeds`: data partner, board, region, feed type, license metadata, status.
- `source_records`: immutable-ish raw payload snapshots, source IDs, hashes, received time.
- `properties`: canonical real-world property entity, address, parcel/geocode references, normalized attributes.
- `listings`: market listing entity, source listing ID, property ID, status, current price, timestamps.
- `listing_versions`: normalized snapshots used to detect changes over time.
- `listing_events`: price change, listed, relisted, suspended, terminated, sold, expired, open house, media update.
- `sold_transactions`: sale price, sale date, property/listing link, source, display permission.
- `media_assets`: photos/floorplans/videos, source URL, storage URL, dimensions, order, license/display rules.
- `geographies`: cities, neighborhoods, school zones, custom polygons, slugs, hierarchy.
- `schools`: school metadata, source, grades, boards, geospatial relationship.
- `market_stats`: precomputed aggregates by geography, property type, date bucket.
- `valuation_estimates`: estimate, range, model/rule version, evidence, generated time.
- `users`: account identity linked to auth provider.
- `saved_homes`: user-property/listing saved state.
- `saved_searches`: filters, polygon, alert settings, notification cadence.
- `alert_events`: generated alert records and delivery status.
- `tour_requests`: explicit user requests for showings.
- `agent_intro_requests`: explicit user requests for an agent introduction.
- `contact_consents`: who can contact whom, for what reason, at what time, with what proof.
- `audit_logs`: sensitive data access, sold-data display, admin actions, feed events.

Important constraints:
- `properties.geom` and `listings.geom` should use PostGIS geography/geometry with spatial indexes.
- `listing_events` should be append-only except for corrective maintenance.
- Sold-data visibility should be controlled by region/feed rule tables, not scattered conditionals.
- Media display rules should be enforceable per asset.

## Data Ingestion Pipeline
Pipeline stages:
1. Fetch or receive source feed records.
2. Store raw payload snapshot with hash and source metadata.
3. Validate schema and required fields.
4. Normalize addresses, attributes, prices, statuses, dates, and geocodes.
5. Match to existing property or create candidate property.
6. Upsert listing/version records.
7. Diff latest version against prior version.
8. Emit listing events.
9. Process media assets and CDN references.
10. Refresh search indexes, materialized views, market stats, and alerts.

Ingestion requirements:
- Jobs must be idempotent by source record hash and source listing ID.
- Every normalized field should know its source when practical.
- Failed records should be inspectable without blocking the whole feed.
- Feed lag and error rate should be visible in admin/monitoring.
- No scraping path should be added unless terms and licensing are reviewed.

## Search Architecture
Start with Postgres/PostGIS because the first launch should prioritize correctness, provenance, and velocity.

Search API inputs:
- Viewport bounding box.
- Optional polygon.
- Location slug or geocoded place.
- Listing status: active, sold, pending/conditional where permitted.
- Price range.
- Beds/baths.
- Property type.
- Size, lot, parking, days on market, sold date.
- Open house flag.
- School/neighborhood filters later.

Search API outputs:
- Lightweight listing summaries only.
- Map cluster data at low zoom.
- Cursor-based pagination for list results.
- Facet counts where cheap enough.
- Source timestamp and coverage notes when useful.

Performance approach:
- Use spatial indexes on listing/property geometry.
- Keep listing-card payloads small.
- Cache common viewport/geography queries.
- Use server-side clustering for high-density map views.
- Precompute neighborhood and market aggregates.
- Move to OpenSearch/Typesense only after PostGIS query complexity becomes the bottleneck.

## Listing Detail Architecture
Listing detail API should return a composed, cacheable response:
- Listing facts.
- Current and historical status.
- Media gallery metadata.
- Property details.
- Event timeline.
- Sold transaction where display is permitted.
- Comparable sales summary.
- Neighborhood and school context.
- Carrying-cost estimate assumptions.
- Source/provenance metadata.
- Contact/tour eligibility based on user state and region rules.

Avoid large nested payloads:
- Fetch photos in paged chunks if needed.
- Fetch comps separately when filters change.
- Fetch heavy market stats lazily.

## Sold Data And Display Rules
Sold data is a first-class domain with region-specific rules.

Model display permissions explicitly:
- `can_show_public`.
- `requires_auth`.
- `requires_region_membership` or equivalent if a data agreement requires it.
- `can_show_price`.
- `can_show_sold_date`.
- `can_show_address`.
- `can_index_for_seo`.
- `allowed_retention_days` if applicable.

Rules should be versioned:
- A listing shown under rule version X should be auditable later.
- If a rule changes, derived pages and caches must be invalidated.

If a sold-data gate is required, the UI should explain it plainly and collect only the minimum needed information.

## Comparables And Valuation
V1 comps:
- Query sold properties by distance, geography, property type, beds/baths, size, lot, parking, and sold date.
- Score comparable relevance with transparent heuristics.
- Show why a comp was included.
- Allow users to adjust filters without creating an account.

Valuation progression:
1. Rule-based estimate range from recent comps and simple adjustments.
2. Backtested statistical model by region/property type.
3. Model-backed predicted sale price with confidence band.

Model requirements before public launch:
- Time-based train/test split.
- Error metrics by city/neighborhood/property type.
- Calibration check for confidence ranges.
- Drift monitoring.
- Explanation surface that references comps and model limits.

Do not show a model estimate as a single precise truth.

## Auth, Privacy, And Consent
Authentication is required for:
- Saved homes.
- Saved searches and alerts.
- Contact preferences.
- Tour requests.
- Agent introductions.
- Any sold-data access that legally requires an account.

Authentication should not be used as a dark pattern.

Consent model:
- Browsing never triggers agent contact.
- Saving a home never triggers agent contact.
- Viewing sold data never triggers agent contact.
- An agent/referral contact can only be created by explicit tour or intro action.
- Store consent text/version, timestamp, user ID, listing/property context, and destination party.
- Let users withdraw or change contact preferences.

## API Design
Core endpoints:
- `GET /search/listings`
- `GET /search/clusters`
- `GET /listings/{listing_id}`
- `GET /properties/{property_id}/history`
- `GET /properties/{property_id}/comps`
- `GET /geographies/{slug}`
- `GET /geographies/{slug}/market-stats`
- `POST /saved-homes`
- `POST /saved-searches`
- `POST /tour-requests`
- `POST /agent-intro-requests`
- `GET /me/contact-preferences`
- `PUT /me/contact-preferences`

Admin/internal endpoints:
- `GET /admin/feeds`
- `GET /admin/feeds/{feed_id}/runs`
- `GET /admin/source-records/{record_id}`
- `POST /admin/reprocess/{record_id}`

Use shared schema validation:
- Pydantic on the backend.
- Generated TypeScript types or OpenAPI client on the frontend.

## Frontend Architecture
Next.js routes:
- `/` search experience.
- `/homes/[province]/[city]/[slug]` listing detail, subject to data-provider URL rules.
- `/sold/[province]/[city]` sold search landing where permitted.
- `/ca/[province]/[city]` city page.
- `/ca/[province]/[city]/[neighborhood]` neighborhood page.
- `/saved` saved homes/searches.
- `/alerts` alert settings.
- `/account/contact` contact preferences.

UI primitives:
- Map/list split view on desktop.
- Bottom sheet result list on mobile.
- Sticky filter toolbar with real controls.
- Listing detail gallery optimized for swipe and keyboard.
- Event timeline component.
- Comparable sales map/table component.
- Explicit contact/tour modal with consent text.

SEO:
- Server-render city/neighborhood pages.
- Use structured data only when accurate and permitted.
- Use canonical URLs.
- Avoid indexing pages that violate listing-feed terms.
- Generate pages from data coverage, not empty template permutations.

## Performance Budgets
Frontend:
- Mobile LCP under 2.5 seconds for search and SEO pages.
- CLS under 0.1.
- Initial JS kept small; lazy-load map/gallery heavy code.
- Image thumbnails served from CDN with responsive sizes.
- No oversized listing payloads in initial HTML.

Backend:
- Search p95 under 300 ms after cache warmup for normal queries.
- Listing detail p95 under 500 ms excluding image CDN.
- Comps p95 under 800 ms for bounded queries.
- Ingestion lag visible and budgeted by feed type.

Data:
- Spatial indexes on geometry.
- Composite indexes for common filters.
- Materialized views for market stats.
- Cache invalidation tied to listing/event changes.

## Security And Compliance
- Never expose data-provider credentials to the browser.
- Keep raw source payload access admin-only.
- Apply row-level or backend authorization checks for user-owned saved state.
- Log sensitive admin access.
- Rate-limit search, auth, and contact endpoints.
- Protect tour/intro forms from spam and abuse.
- Do not store more personal data than needed for the buyer workflow.
- Implement deletion/export flows for user data.
- Keep source-license metadata attached to listing and media records.

## Observability
Track:
- Search latency by geography and filter complexity.
- Map tile/cluster latency.
- Listing detail latency.
- Feed ingestion lag and failure rate.
- Missing geocode rate.
- Duplicate property/listing match conflicts.
- Sold-data display events.
- Contact consent events.
- Alert delivery success.
- Valuation model error and drift later.

## Implementation Milestones
### 1. Foundation
- Scaffold monorepo.
- Add Next.js, FastAPI, Postgres/PostGIS migrations, Redis worker, and shared schemas.
- Add local seed data and development commands.

### 2. Search Data Model
- Implement properties, listings, listing versions, listing events, media, geographies, and users.
- Add seed/import script for permitted demo data.
- Add geospatial indexes and search queries.

### 3. Map Search Web
- Build map/list UI.
- Add filters, listing cards, clustering, and mobile bottom sheet.
- Add saved homes/searches behind auth.

### 4. Listing Detail
- Build listing detail route and API.
- Add photo gallery, facts, event timeline, source timestamp, and carrying-cost estimate.

### 5. Neighborhood SEO
- Build city/neighborhood pages.
- Add market stats, active listings, recent sold data where permitted, metadata, and canonical handling.

### 6. Sold And Comps
- Add sold transaction model and regional display rules.
- Build comparable sale map/table workflow.
- Add audit logs for sold-data display.

### 7. Consent-Based Contact
- Add tour requests and agent-intro requests.
- Add contact preferences and explicit consent records.
- Add admin/referral workflow only after consent is proven end-to-end.

### 8. Valuation And Intelligence
- Add rule-based comp estimate.
- Add backtesting harness.
- Add model-backed estimate only when accuracy and uncertainty are acceptable.

### 9. Launch Hardening
- Add monitoring, rate limits, security tests, data deletion, feed runbooks, accessibility checks, and performance budgets.

## Test Plan
Backend:
- Geospatial search unit and integration tests.
- Listing event diff tests.
- Sold-data display rule tests.
- Consent workflow tests.
- Auth and saved-state authorization tests.
- Ingestion idempotency tests.

Frontend:
- Search filter and map/list interaction tests.
- Mobile bottom sheet tests.
- Listing gallery and detail layout tests.
- Saved homes/searches tests.
- Tour/intro consent tests.
- SEO metadata snapshot tests.

Performance:
- Search query benchmarks with realistic density.
- Listing detail response benchmarks.
- Lighthouse checks for search, listing, city, and neighborhood pages.
- Image payload and layout stability checks.

Data quality:
- Duplicate detection tests.
- Geocode validation.
- Feed schema validation.
- Comp relevance evaluation.
- Valuation backtests before public model launch.

## Open Decisions
- Final product name and brand.
- First target region.
- Exact MLS/sold-data access path.
- Map provider: Mapbox vs MapLibre stack.
- Auth provider: Supabase Auth vs Clerk/Auth.js.
- Hosting stack after the first scaffold.
- Whether to introduce a separate search engine before launch or keep PostGIS longer.
