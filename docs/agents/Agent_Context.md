# Agent Context - Eqar

This file is shared working memory for AI coding agents on the Eqar project, including Codex and Claude Code. Use it to keep track of progress, discoveries, mistakes, decisions, open questions, and future thoughts so agents do not repeat the same work or silently inherit bad assumptions.

This file should be incremented over time. Do not only rewrite the latest summary. Preserve useful history so future agents can understand how the project thinking changed.

## How Agents Should Use This File
- Read this file before making meaningful project changes.
- Add a new journal entry after important discoveries, architectural choices, bugs, reversals, or completed milestones.
- Update the current snapshot only when it is materially stale, and leave a journal entry explaining the change.
- Treat this as living context, not absolute truth.
- If something here seems wrong, outdated, risky, or based on a bad assumption, fix it directly when safe.
- If changing it would affect product direction, architecture, security, data handling, or user intent, ask the user one focused question first.
- Do not preserve mistakes just because another agent wrote them.
- Do not let this file become a dumping ground. Keep entries concise, useful, and dated when helpful.
- Prefer appending over replacing. If an old thought is wrong, mark it as corrected in a later entry instead of deleting it unless it contains secrets or harmful content.
- Future thoughts are allowed. Label them as hypotheses, ideas, or recommendations, not settled decisions.

## Entry Format
Use this format when adding to the journal:

```md
### YYYY-MM-DD - Agent Name - Short Title
- Type: progress | decision | discovery | correction | risk | future-thought
- Context: What happened or what was learned.
- Impact: Why it matters for future work.
- Next: What the next agent should consider.
```

If a single update covers several things, keep one dated heading and use short bullets.

## Project Snapshot
- Project name: Eqar.
- Meaning: English rendering of the Arabic word for real estate.
- Current stage: early planning / blank-slate implementation.
- Current repo state: planning and agent guidance docs exist; no application source code has been scaffolded yet.
- Intended product: AI real-estate co-pilot for agents, starting in Canada.

## Current Product Direction
Eqar is planned as a Canada-first web SaaS dashboard for real-estate agents. It should combine a closed-source LLM backbone with trusted real-estate tools, calculators, document analysis, and eventually ML models.

The product should not be positioned as a generic chatbot. Its edge is that it can call structured real-estate tools for calculations, scenarios, and grounded answers instead of guessing.

Primary user for v1:
- Real-estate agents.

Primary v1 surface:
- Private agent dashboard.

Future expansion:
- Tenant workflows.
- Investor workflows.
- Arabic/bilingual workflows.
- Additional countries through country-specific data/config adapters.

## Current Technical Direction
- Backend: FastAPI.
- Platform/data foundation: Supabase for auth, Postgres, storage, and persisted user data.
- LLM strategy: provider-agnostic adapter layer so OpenAI, Claude, or another closed model can be swapped by configuration.
- Data strategy:
  - Canada-first country pack.
  - Manual/uploaded data support.
  - Public/API data support where reliable and legally usable.
  - Future country packs should be possible without hardcoding everything into Canadian logic.
- Tooling strategy:
  - Start with deterministic calculators, rule-based tools, RAG/document Q&A, and clear formulas.
  - Defer predictive ML until the project has enough data quality, evaluation, and uncertainty handling.

## Important Product Decisions Already Made
- First user is agents, not tenants or investors.
- First UI is an agent dashboard, not an embeddable website widget.
- Canada is the first market, but the architecture should anticipate other countries.
- Eqar should support both manual uploads and selected public/API data.
- Outputs use mixed mode:
  - Default mode: agent-reviewed drafts.
  - Export/share mode: stronger disclaimers, cited assumptions, source references, and calculation provenance.
- Monetization is expected to be per-agent SaaS, but billing should be planned later rather than built first.

## Known Risks And Guardrails
- Real estate has legal, financial, mortgage, and licensing risk. Eqar should avoid presenting itself as legal, financial, mortgage, or licensed real-estate advice.
- Numeric answers should come from tools/calculators whenever possible, not free-form LLM reasoning.
- Client-shareable outputs need citations, assumptions, disclaimers, and clear provenance.
- MLS and CRM integrations may be valuable but are likely blocked by permissions, compliance, and partner access. Treat them as future work unless easy access is confirmed.
- Do not hardcode secrets or credentials. Use environment variables.
- Do not design country expansion in a way that makes Canada-specific assumptions impossible to replace later.

## Mistakes Or Corrections Log
- No implementation mistakes recorded yet.
- If an agent discovers that a prior assumption is wrong, add a short note here with the correction and what changed.

## Progress Log
- Created `CLAUDE.md` before Codex involvement. It defines high-autonomy project behavior for Claude.
- Created `CODEX.md` to mirror the Claude guidance while adapting it for Codex workflows.
- Created `PLAN.md` with the initial Eqar product plan.
- Created this `Agent_Context.md` as shared memory for Codex and Claude Code.
- Organized project documents into `docs/agents` and `docs/planning`, with `README.md` as the root index.
- Created `docs/planning/TECHNICAL_ARCHITECTURE.md` with the detailed technical architecture plan.
- Scaffolded the foundation monorepo with `apps/web`, `apps/api`, `packages/shared`, and `infra`.
- Created `docs/agents/design.md` as the shared UI design skill for Codex and Claude Code.

## Open Questions
- Exact frontend stack has not been chosen.
- Exact Supabase schema has not been designed.
- Initial LLM provider has not been chosen.
- Initial Canadian public/API data sources have not been selected.
- The first implementation milestone has not been scoped beyond the product plan.

## Suggested Next Step
Define the first build milestone as a thin vertical slice:
- Agent login.
- Chat dashboard.
- One provider-backed LLM adapter.
- One deterministic calculator tool.
- One document upload and Q&A path.
- One saved analysis record.

This should prove the core architecture before adding many real-estate tools.

## Incremental Journal

### 2026-04-24 - Codex - Initial Shared Context Created
- Type: progress
- Context: Created `Agent_Context.md` after the user requested a shared memory file for Codex and Claude Code.
- Impact: Both agents now have a common place to understand current project direction, known risks, open questions, and prior decisions.
- Next: Future agents should append to this journal after meaningful progress instead of only editing the current snapshot.

### 2026-04-24 - Codex - Product Direction Consolidated
- Type: decision
- Context: The initial plan positions Eqar as a Canada-first real-estate agent co-pilot with a private dashboard, provider-agnostic LLM layer, deterministic real-estate tools, uploads, and selected public/API data.
- Impact: This should guide first implementation choices unless the user changes direction.
- Next: The first technical plan should define a thin vertical slice rather than attempting the whole command center at once.

### 2026-04-24 - Codex - Append-Only Memory Preference
- Type: correction
- Context: The user clarified that this file should not merely be updated; it should be incremented so agents can look into the past and write future thoughts.
- Impact: Agents should preserve historical thinking, corrections, and recommendations. Do not overwrite away context unless removing secrets, invalid dangerous instructions, or noise.
- Next: Add dated entries for future discoveries, mistakes, and design recommendations.

### 2026-04-24 - Codex - Documentation Directory Organization
- Type: progress
- Context: Moved agent guidance files into `docs/agents` and the product plan into `docs/planning`. Added root `README.md` as an easy access map.
- Impact: The repo root is now cleaner and ready for future application source code, while planning and agent context remain easy to find.
- Next: If future tooling expects `CLAUDE.md` or `CODEX.md` at the repo root, consider adding lightweight root pointer files instead of duplicating full content.

### 2026-04-24 - Codex - Technical Architecture Plan Added
- Type: decision
- Context: Added `docs/planning/TECHNICAL_ARCHITECTURE.md` after technical planning. The plan standardizes on Next.js, FastAPI, Supabase, OpenAI-first provider adapter, Vercel/Render deployment, `pgvector`, and Redis-backed background jobs.
- Impact: Future implementation should follow this plan unless a later correction supersedes it.
- Next: Start with the foundation milestone: monorepo scaffold, environment templates, Supabase setup, and empty deployable web/API apps.

### 2026-04-24 - Codex - Foundation Scaffold Implemented
- Type: progress
- Context: Added the monorepo foundation: Next.js dashboard scaffold in `apps/web`, FastAPI scaffold in `apps/api`, shared TypeScript contracts in `packages/shared`, Supabase migration/env docs in `infra`, and root npm scripts.
- Impact: The project now has runnable frontend/backend foundations and deterministic calculator tests.
- Next: Move into the authenticated dashboard milestone: Supabase project setup, JWT verification against real tokens, workspace bootstrap, and persistent conversation records.

### 2026-04-24 - Codex - Dependency Audit Follow-Up
- Type: risk
- Context: Upgraded the web app from Next.js 14 to Next.js 16.2.4 to remove high-severity audit findings. npm still reports a moderate PostCSS advisory through Next's pinned `postcss@8.4.31`. A direct patched `postcss@8.5.10` dev dependency and npm override were added, but npm still retains Next's pinned transitive copy. `npm audit fix --force` suggests a breaking downgrade path and was intentionally not run.
- Impact: Do not treat audit as fully clean yet. Revisit when Next releases a patched dependency chain or when npm's advisory/fix path changes.
- Next: Before production, rerun `npm audit`, check Next release notes, and remove the override/direct PostCSS dependency if Next resolves the transitive advisory.

### 2026-04-24 - Codex - Uncodixify Design Skill Added
- Type: decision
- Context: Added `docs/agents/design.md` from the user's Uncodixify guidance and linked it from both Codex and Claude instructions.
- Impact: Future frontend work should avoid generic AI dashboard patterns: hero blocks, eyebrow labels, glass panels, gradient decoration, fake metric grids, pill overload, and oversized radii.
- Next: The current `apps/web` dashboard scaffold predates this design skill and likely needs a redesign pass before serious product UI work continues.

### 2026-04-24 - Codex - Frontend Redesign Applied
- Type: progress
- Context: Reworked the initial `apps/web` dashboard to follow `docs/agents/design.md`. Removed eyebrow labels, metric-card grid, decorative sidebar note, rounded pills, fake progress bars, and gradient-style hierarchy. Replaced the layout with a plain sidebar, toolbar, work queue table, chat panel, and document table.
- Impact: The frontend now better matches the project UI standard before deeper product workflows are built.
- Next: Keep future UI changes grounded in real data and workflow tables/forms rather than decorative cards or filler panels.

### 2026-04-24 - Codex - Local Env Files Created
- Type: progress
- Context: Moved the user's Supabase values out of the tracked root `.env.example` into ignored service-local files: `apps/api/.env` and `apps/web/.env.local`. Normalized Supabase URLs to the base project URL instead of the `/rest/v1/` endpoint. Restored `.env.example` to placeholder values only.
- Impact: Local development can now read real Supabase settings while keeping committed templates free of project secrets. `EQAR_AUTH_DISABLED` remains `true` for local testing until the frontend auth flow sends Supabase access tokens.
- Next: Before live auth testing, set `EQAR_AUTH_DISABLED=false`, implement/verify frontend Supabase login, and confirm backend JWT validation against a real session token.

## Future Thoughts And Hypotheses

### Thin Vertical Slice Is Probably The Best First Build
- Type: future-thought
- Thought: The first implementation should prove the full architecture with the smallest useful workflow: auth, chat, one LLM provider adapter, one calculator, one upload/Q&A path, and one saved analysis.
- Why it matters: This tests the core product loop without overbuilding the full real-estate tool suite too early.
- Caution: Avoid turning the first milestone into a large platform build before the agent workflow feels valuable.

### Country Packs Should Be Real, But Not Over-Engineered
- Type: future-thought
- Thought: Canada-specific logic should live behind a country/module boundary from the start, but the first version does not need a fully generic global rules engine.
- Why it matters: The user wants future global support, but premature abstraction could slow the MVP.
- Caution: Use a simple adapter/config pattern first; generalize after a second country or serious data source appears.

### Calculators Need Provenance
- Type: future-thought
- Thought: Any calculation shown to agents or clients should store its inputs, assumptions, formula/tool version, and data source references.
- Why it matters: This reduces hallucination risk and supports client-share/export mode.
- Caution: Do not let the LLM produce numeric conclusions without structured tool output when a calculator exists.
