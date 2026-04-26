# Eqar MVP

Eqar is a Canada-first buyer-facing real estate search and market intelligence product.

The active product direction is a trust-first search platform for buyers, sellers, and market researchers:
- Map-first property search.
- Sold price visibility where licensed.
- Listing history and relisting timelines.
- Comparable sale tooling.
- Neighborhood and school context.
- Fast mobile listing detail pages.
- Explicit tour or agent-introduction requests only.

This repository is currently in planning reset. The previous agent AI co-pilot implementation has been removed because it no longer matches the product.

## Start Here
- [Product Plan](docs/planning/PLAN.md)
- [Technical Architecture](docs/planning/TECHNICAL_ARCHITECTURE.md)
- [Data And Compliance Plan](docs/planning/DATA_AND_COMPLIANCE.md)
- [Agent Context](docs/agents/Agent_Context.md)
- [UI Guidance](docs/agents/design.md)

## Next Build Step
Resolve the first launch region and data access path, then scaffold the first vertical slice with permitted demo data:
- Next.js map/list search.
- FastAPI search and listing APIs.
- PostgreSQL/PostGIS schema.
- Listing detail with photo gallery, facts, event timeline, and source timestamp.
- Saved homes and saved searches behind auth.
