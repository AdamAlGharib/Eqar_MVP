# Eqar Product Plan

## Summary
Eqar is a Canada-first, buyer-trust real estate search and market intelligence product.

The product is not an agent dashboard and not a lead-gen skin over MLS listings. The wedge is simple: give Canadian buyers the information they actually need to make decisions, especially sold prices, listing history, comparable sales, price changes, market context, and low-friction tour or agent help only when they explicitly ask for it.

Working positioning:
- Search like a buyer, not like a lead.
- No agent harassment. No hidden lead capture. No fake scarcity.
- Serious data depth in a fast, mobile-first interface.

## Product Thesis
Canadian real estate search is still split between three imperfect options:
- Realtor.ca has brand awareness and broad listing coverage, but limited decision support and historically gated sold-price visibility.
- HouseSigma has strong data depth for serious buyers and investors, but the experience can still be made more approachable, faster, and more transparent.
- Zoo Casa proved the buyer-friendly search wedge, then drifted toward lead capture and lost the sharpness of the original promise.

Eqar should occupy the trust gap: the search product that behaves like it is on the buyer's side.

The long-term product combines:
- Sold price transparency.
- Listing and relisting history.
- Neighborhood and school context with clear sources.
- Comparable sale tools that work without dark-pattern signup walls.
- Predicted sale price and estimate ranges with honest confidence bands.
- Map-first search that is fast on mobile.
- Tour booking and agent referral only after explicit user intent.

## Primary Users
- Serious buyers who are actively comparing homes, prices, neighborhoods, and timing.
- Buyer-investors who need price history, rental assumptions, cap-rate signals, and repeatable comp workflows.
- Sellers who want to understand local comps before talking to an agent.

Secondary users:
- Casual browsers who land through SEO neighborhood or listing pages.
- Buyer agents who receive explicit referrals or tour requests.

Agents are service providers in this product, not the primary customer. The primary customer is the buyer or market researcher.

## Non-Negotiable Product Principles
- Buyer trust first: no unsolicited agent contact, no silent lead routing, no fake "required" signup unless a legal/data partner rule truly requires it.
- Sold data is a core product feature, not a teaser.
- Account creation should unlock convenience, not basic comprehension.
- If sold data must be gated by region or licensing terms, say that plainly and keep the gate minimal.
- Every estimate needs provenance: source, date, model version, assumptions, and uncertainty.
- Search must feel fast on a mid-range phone on cellular data.
- Map and listing pages must be useful before login.
- SEO pages must answer real buyer questions, not produce thin location spam.
- Monetization must not invert the product incentives.

## Differentiation
Eqar should be measured against the best parts of existing products, not against the weakest incumbent.

Must beat Zoo Casa on:
- Trust posture.
- Mobile performance.
- Listing detail depth.
- Photo gallery quality.
- Relisting and price-change visibility.
- Clearer buyer workflows.

Must approach or beat HouseSigma on:
- Sold price access where licensed.
- Listing history and price-change timelines.
- Comparable sale tooling.
- Estimated sale price and confidence bands.
- Neighborhood data depth.

Must beat Realtor.ca on:
- Decision support.
- Sold/comparable context.
- Map UX.
- Transparency around data and agent contact.

## V1 Product Scope
V1 should prove the wedge with a narrow but real buyer workflow:

1. Search homes on a fast map-first interface.
2. Open a listing detail page that feels serious and data-rich.
3. See listing history, price drops, relisting signals, and comparable sold homes where data access permits.
4. Save homes and searches.
5. Get alerts for price changes, relists, sold updates, and new matching listings.
6. Request a tour or buyer agent introduction only through explicit action.

The first market should be one Canadian metro area or province where data access can be handled responsibly. Ontario is the likely first target if licensing and data access are viable, but the technical design should allow a different first region if practical access is better elsewhere.

## V1 Features
Core search:
- Map-first search with viewport search, polygon draw, location search, and saved boundaries.
- Filters for price, beds, baths, property type, parking, status, days on market, sold date, lot size, interior size, and open houses when available.
- Sorts for newest, price, recent price drop, days on market, estimated deal strength, and sold recency where applicable.
- Mobile bottom-sheet listing results with smooth map/list interaction.

Listing detail:
- High-performance photo gallery.
- Clear property facts and source timestamp.
- Price history and event timeline.
- Listing, relisting, suspension, termination, sold, and price-change events when available.
- Comparable sold homes with distance, date, property similarity, and adjustment notes.
- School and neighborhood context with source links or source labels.
- Monthly carrying-cost estimate with editable assumptions.
- "Contact" and "book tour" actions that are explicit and separate from browsing.

Sold and comp tools:
- Sold price visibility where licensed.
- Comparable sale map and table.
- Simple comp filters: sold date range, distance, beds/baths, property type, size range, age, parking, and lot type.
- Exportable comp summary later, with provenance and disclaimers.

SEO and market pages:
- Neighborhood pages for active listings, sold trends, price bands, days-on-market trends, and recent comparable sales.
- City and neighborhood guides that are data-backed rather than generic.
- Indexable listing pages when permitted by listing data rules.

User account:
- Saved homes.
- Saved searches.
- Alerts.
- Contact preferences.
- Explicit consent log for any agent/referral contact.

Operational admin:
- Data ingestion status.
- Feed health monitoring.
- Listing deduplication review.
- Compliance/audit logs for sold-data display and user consent.

## Out Of Scope For Initial Build
- A generic AI real-estate chatbot.
- Agent CRM workflows.
- Seller lead capture funnels.
- Native mobile app before the mobile web product proves retention.
- Nationwide MLS coverage before one region works deeply.
- Predictive valuation claims without calibrated error bands and backtesting.
- Scraping that violates site terms, MLS rules, or data-provider agreements.

## Monetization
Primary monetization should preserve buyer trust:
- Transparent referral fees when a user explicitly asks for an agent introduction and a transaction closes.
- Tour-booking or showing coordination partnerships where allowed.
- Optional premium buyer/investor analytics later, only if the free product remains useful.

Avoid:
- Selling raw leads.
- Triggering agent outreach from browsing behavior.
- Hiding basic market context behind manipulative signup walls.
- Optimizing UI for email capture over buyer comprehension.

## Data Strategy
The product lives or dies on legal, durable data access.

Priority data sources:
- Licensed MLS/IDX/VOW feeds by region.
- Board-approved sold data access where available.
- Public municipal or provincial datasets where legally usable.
- School boundary and performance data from official or licensed sources.
- Geocoding, parcel, and neighborhood boundary sources with clear licensing.

Data design goals:
- Store source, license context, retrieval time, and display permission for every record.
- Separate raw source records from normalized product records.
- Preserve listing event history instead of overwriting listings in place.
- Maintain region-specific rules for what can be shown publicly, behind account, or not at all.

## Milestones
### Milestone 0: Data And Compliance Discovery
- Pick the first target region.
- Identify practical MLS, sold-data, school, and geospatial data paths.
- Document display rules for active listings, sold listings, listing photos, and historical events.
- Define the minimum viable licensed data contract for launch.

### Milestone 1: Product Foundation
- Scaffold monorepo, frontend, backend, database migrations, and deployment environments.
- Create the core domain model for properties, listings, events, media, geographies, users, saved searches, and consent.
- Seed with permitted sample or internal demo data.

### Milestone 2: Map Search MVP
- Build mobile-first map/list search.
- Implement location search, viewport search, filters, sorting, and listing cards.
- Add saved homes and saved searches.
- Hit strict performance budgets before adding more features.

### Milestone 3: Listing Detail And SEO
- Build serious listing detail pages with photos, property facts, event timeline, and carrying-cost estimate.
- Build city and neighborhood SEO pages backed by real data.
- Add metadata, canonical URLs, and structured data where allowed.

### Milestone 4: Sold Data And Comparables
- Add sold listings where licensed.
- Build comp map/table workflow.
- Add listing history graphs and price-change/relisting signals.
- Add audit logging for sold-data display.

### Milestone 5: Estimates And Market Intelligence
- Start with simple rule-based estimates and transparent assumptions.
- Add model-backed predicted sale price only after evaluation and calibration.
- Show confidence bands, model version, training window, and comparable evidence.

### Milestone 6: Explicit Tour And Agent Workflow
- Add tour requests and buyer-agent introductions.
- Add explicit contact consent and preferences.
- Build referral tracking without leaking browsing behavior.

### Milestone 7: Hardening And Launch
- Add monitoring, alerting, feed health checks, rate limits, abuse protections, and privacy flows.
- Run accessibility, SEO, performance, security, and mobile QA.
- Launch one region deeply before expanding coverage.

## Success Metrics
Product trust:
- Zero unsolicited contact incidents.
- High percentage of users who understand why and when an agent can contact them.
- Low bounce on listing detail pages.

Search quality:
- Search response under 300 ms p95 for normal map/list queries after cache warmup.
- Listing detail API under 500 ms p95 excluding image CDN.
- Mobile LCP under 2.5 seconds on core pages.

Market intelligence:
- Sold-data coverage by region.
- Comp result relevance.
- Estimate median absolute percentage error by geography and property type.
- Alert precision for saved searches.

Growth:
- Organic sessions to neighborhood and listing pages.
- Saved search conversion.
- Return visits per active buyer.
- Tour/request-agent conversion from explicit intent actions only.

## Risks
- MLS and sold-data access may be slower, narrower, or more restrictive than desired.
- Display rules may vary materially by board, province, data partner, or listing status.
- A weak data supply would make the product feel like a prettier search UI rather than a real wedge.
- SEO pages can become thin if they are not backed by real local data.
- Valuation estimates can create trust and liability risk if they are overconfident.
- Map performance can degrade quickly with naive clustering or oversized listing payloads.
- Monetization pressure can recreate the lead-gen incentives the product is meant to avoid.

## Test Plan
- Unit-test mortgage, carrying-cost, tax, and estimate helper formulas.
- Test search filtering, polygon matching, sorting, pagination, and geospatial edge cases.
- Test listing event reconstruction from source feed changes.
- Test sold-data visibility rules by region and user state.
- Test consent flows so no agent/referral record can be created without explicit user action.
- Test listing detail pages on mobile for gallery performance, layout stability, and no text overlap.
- Test SEO pages for canonical URLs, structured metadata, and non-thin content.
- Backtest valuation models by time period and geography before showing model-backed estimates.
- Add privacy/security tests for cross-user saved searches, favorites, alerts, and contact preferences.

## Current Assumptions
- Eqar remains the working name until the user chooses a final brand.
- The first product is a public buyer-facing web app, not a private agent SaaS.
- Canada is the first market.
- One region should be launched deeply before national expansion.
- Data access and compliance must be solved before real MLS/sold-data launch.
- Mobile web comes before native mobile, but the architecture should not block a future native app.
