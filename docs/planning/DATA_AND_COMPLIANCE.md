# Data And Compliance Plan

## Why This Exists
Eqar's product wedge depends on data depth: sold prices, listing history, comparables, photos, schools, neighborhoods, and market stats. That data has licensing and display constraints in Canada. The product should be designed so compliance is not an afterthought or a late rewrite.

## Core Rule
Do not build the real production product on data we cannot legally store, transform, display, cache, or index.

Use permitted seed/demo data during development. Replace it with licensed data only after the rules are understood and modeled.

## First Region Decision
Pick one launch region before real ingestion work.

Evaluate regions by:
- Active listing feed access.
- Sold-data access.
- Historical listing-event access.
- Photo/media display rights.
- Address display rules.
- SEO/indexing permissions.
- Cost and timeline.
- Ability to launch a useful buyer product with depth.

Ontario is a likely candidate because of market size and buyer demand, but it should not be assumed if another region has a faster compliant data path.

## Data Categories
### Active Listings
Needed fields:
- Source listing ID.
- Address or display-safe location.
- Price.
- Status.
- Property type.
- Beds, baths, parking.
- Interior size, lot size, age where available.
- Description.
- Brokerage/listing agent attribution if required.
- Listing date and update time.
- Media references and display rules.

Questions to answer:
- Can listings be displayed publicly?
- Can listing pages be indexed?
- How fresh must the data be?
- What attribution is required?
- How should delisted/expired records be handled?

### Sold Listings
Needed fields:
- Sold price.
- Sold date.
- List price at sale.
- Prior listing events where available.
- Property attributes at time of sale.
- Address/display-safe location.
- Source and permission metadata.

Questions to answer:
- Can sold price be shown publicly?
- Is authentication required?
- Can sold data appear on SEO pages?
- Can sold records be used in comps or model training?
- Are there retention limits?
- Are screenshots/exports allowed?

### Listing History
Needed events:
- Listed.
- Price change.
- Relisted.
- Suspended.
- Terminated.
- Expired.
- Sold.
- Open house.
- Media update.

Questions to answer:
- Does the data source provide history directly?
- If not, can Eqar reconstruct history from snapshots?
- Can reconstructed history be displayed?
- Can historical photos be retained or displayed?

### Media
Questions to answer:
- Can images be cached locally?
- Can thumbnails be generated?
- Can images be shown after listing status changes?
- What attribution is required?
- Are there CDN or hotlink restrictions?

### Schools And Neighborhoods
Prefer official or licensed sources.

Questions to answer:
- What is the source for school boundaries?
- Are scores/ratings licensed or public?
- How often do boundaries update?
- Can school data be shown as decision support without overclaiming?

## Permission Model
Every listing-like record should be tied to display rules.

Suggested rule fields:
- `region_code`
- `source_feed_id`
- `record_type`
- `rule_version`
- `can_show_public`
- `requires_auth`
- `can_show_price`
- `can_show_sold_price`
- `can_show_address`
- `can_show_media`
- `can_cache_media`
- `can_index_seo`
- `can_use_for_comps`
- `can_use_for_model_training`
- `retention_days`
- `required_attribution`

The UI and API should call policy helpers rather than hardcoding these checks.

## Development Data
Use one or more of:
- Hand-authored seed listings.
- Synthetic listings.
- Publicly licensed geospatial boundaries.
- Small internal fixtures for listing-event timelines.

Development data should:
- Be obviously non-production or permitted.
- Include active, sold, relisted, price-drop, and terminated examples.
- Include imperfect data cases for testing.
- Include multiple geographies and property types.

## Compliance Work Before Launch
- Confirm data source contracts.
- Document display rules.
- Implement rule table and tests.
- Verify required attribution in UI.
- Verify data retention and deletion behavior.
- Verify sold-data gates, if any.
- Verify SEO indexing rules.
- Verify media caching rights.
- Verify model-training rights if valuation work uses source data.
- Create a feed incident runbook.

## Product Trust Requirements
- Users should know when and why account creation is required.
- Sold-data restrictions should be explained plainly.
- Viewing or saving data must not create an agent lead.
- Tour and agent-introduction requests require explicit consent.
- Consent records must be stored with text/version and timestamp.

## Risks
- A region may allow active listing display but restrict sold data too heavily for the wedge.
- Sold data may be usable for logged-in users but not SEO.
- Photo caching rules may make performance harder.
- Listing history may need reconstruction from snapshots, which requires reliable feed frequency.
- Model training may be restricted by provider terms.

## Immediate Next Step
Create a short data-source decision memo for the first region:
- Candidate region.
- Data provider options.
- Access timeline.
- Required agreements.
- Display constraints.
- Development fallback.
- Launch recommendation.
