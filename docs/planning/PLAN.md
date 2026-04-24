# Eqar Product Plan

## Summary
Eqar will be a Canada-first AI real-estate co-pilot for agents, delivered as a web SaaS dashboard. It will use a closed-source LLM provider through an adapter layer, plus trusted real-estate tools for calculations, document/data analysis, and agent workflows.

The first version will target real-estate agents, not tenants or investors directly. It will feel like an agent command center: chat-based, data-aware, and able to produce property analyses, listing prep, client-ready drafts, affordability/carrying-cost calculations, and document Q&A.

## Key Product Decisions
- First user: real-estate agents.
- First surface: private agent dashboard.
- Market focus: Canada first, with architecture prepared for future country-specific data packs.
- Output posture: mixed mode.
  - Default outputs are agent-reviewed drafts.
  - Explicit export/share outputs include stronger disclaimers, cited inputs, and calculation provenance.
- Monetization: per-agent SaaS, planned in the data model but Stripe/subscription checkout deferred until the core product is useful.
- Differentiator: not "just a chatbot"; Eqar should route real-estate tasks through deterministic tools, formulas, uploaded data, public/API data, and eventually ML models.

## Implementation Direction
- Build as a web SaaS with a FastAPI backend and Supabase for auth, Postgres, file storage, and persisted user data.
- Use a provider-agnostic LLM layer so OpenAI, Claude, or another closed model can be swapped via configuration.
- Implement a tool orchestration layer where the LLM can call structured real-estate tools instead of inventing answers.
- Implement Canada as the first country pack, with country-specific assumptions isolated behind adapter/config boundaries.
- Support two v1 data lanes:
  - Manual/uploaded data: PDFs, CSVs, listing sheets, notes, and property documents.
  - Public/API data: rates, tax tables, public property or market references where available.
- Core v1 tool bundle:
  - Listing prep: descriptions, showing notes, seller talking points, pricing rationale, marketing copy.
  - Property analysis: comparable summary, rent/carrying-cost estimates, cap-rate/cash-flow scenarios, risk notes.
  - Buyer workflow: affordability, monthly carrying cost, mortgage assumptions, closing-cost estimate, land transfer tax.
  - Client communication: email/SMS-style drafts, objection handling, follow-up messages.
  - Document Q&A: grounded answers from uploaded listings, disclosures, leases, inspection notes, and agent notes.
- Use deterministic calculators and rule-based tools first. Defer predictive ML until data quality and evaluation are strong enough, except for clearly labeled experimental prototypes if added later.

## Test Plan
- Unit-test all calculators with known Canadian examples, including mortgage payment, land transfer tax, closing costs, cash-flow, and cap-rate calculations.
- Add integration tests for LLM tool calls to ensure the assistant uses tools for numeric answers instead of free-form guessing.
- Test document Q&A with uploaded sample files and require answers to cite source snippets or uploaded documents.
- Test mixed-mode output behavior:
  - Draft mode can be flexible.
  - Export/share mode must include disclaimers, cited assumptions, and calculation provenance.
- Add acceptance tests for core dashboard flows: sign in, upload data, ask a question, run an analysis, save the result, and export/share a reviewed answer.

## Assumptions
- The first build prioritizes product usefulness over billing automation.
- Canada-specific logic should be implemented first, but not hardcoded in a way that blocks future country packs.
- Eqar should avoid presenting itself as legal, financial, mortgage, or licensed real-estate advice.
- MLS/CRM integrations are future work unless easy public/API access is available during implementation.
