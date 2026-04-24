# Eqar Technical Architecture Plan

## Summary
Build Eqar as a production-capable, Canada-first AI real-estate co-pilot for agents using a Next.js dashboard, FastAPI backend, Supabase auth/database/storage, and an OpenAI-first but provider-agnostic LLM/tool orchestration layer.

The architecture should optimize for speed of delivery now and expansion later: deterministic real-estate tools before predictive ML, country packs instead of hardcoded Canada-only logic, secure document ingestion, auditable calculations, and clean boundaries between chat, tools, data, and model providers.

Chosen defaults:
- Frontend: Next.js + TypeScript.
- Backend: FastAPI + Python.
- Auth/database/storage: Supabase.
- First LLM provider: OpenAI behind an adapter.
- Deployment: Vercel frontend, Render backend/API/worker, Supabase managed services.
- Retrieval: Supabase Postgres with `pgvector`.
- Background jobs: Redis-backed queue on Render for document parsing, embeddings, and long-running analysis.

## Core Architecture
- Monorepo layout:
  - `apps/web`: Next.js dashboard.
  - `apps/api`: FastAPI backend.
  - `packages/shared`: shared schemas/types generated from API contracts where useful.
  - `docs`: planning, agent context, architecture docs.
  - `infra`: deployment notes, Supabase migrations, environment templates.
- Frontend responsibilities:
  - Agent login, dashboard shell, chat UI, upload UI, saved analyses, export/share views.
  - Never call LLM providers directly from the browser.
  - Use Supabase client only for auth/session; protected app data should go through FastAPI unless direct Supabase access is intentionally allowed by RLS.
- Backend responsibilities:
  - Verify Supabase JWTs on every protected request.
  - Own LLM orchestration, tool routing, calculator execution, document ingestion, export generation, and audit/provenance records.
  - Expose OpenAPI docs for all API routes.
- Data/storage responsibilities:
  - Supabase Auth for users.
  - Postgres for workspaces, chats, messages, files, tools, calculations, analyses, audit logs, and country-pack metadata.
  - Supabase Storage for uploaded source documents and generated exports.
  - `pgvector` for document chunks and embeddings.

## Product/Data Model
- Use a multi-tenant SaaS model from day one:
  - `workspaces`: brokerage/team/personal workspace.
  - `workspace_members`: user role and permissions.
  - `projects`: client/property/deal workspace grouping.
  - `conversations` and `messages`: chat state and model/tool traces.
  - `documents`: uploaded files and parsed metadata.
  - `document_chunks`: text chunks, embeddings, source offsets, page numbers.
  - `analysis_runs`: saved agent workflows such as property analysis or buyer scenario.
  - `tool_runs`: calculator/tool inputs, outputs, version, latency, and provenance.
  - `country_packs`: country/province configuration, formulas, assumptions, tax tables, disclaimers.
- Roles:
  - `owner`: workspace billing/admin.
  - `agent`: normal product user.
  - `assistant_viewer`: future read-only/team support role.
- Initial country pack:
  - `CA` country pack with `ON` province support first.
  - Keep formulas and defaults versioned so saved calculations can explain which assumptions were used.
- Billing:
  - Data model should include subscription fields and usage counters, but Stripe checkout is deferred.

## LLM, Tools, And Retrieval
- Implement an internal `LLMProvider` interface:
  - `complete(messages, tools, response_schema, metadata)`.
  - `embed(texts, metadata)`.
  - `summarize_document(chunks, instructions)`.
  - First implementation: OpenAI.
  - Future implementations: Claude or other closed-source providers.
- Implement a `ToolRegistry`:
  - Tools declare name, description, JSON input schema, JSON output schema, permissions, country/province availability, and version.
  - The orchestrator validates all tool inputs before execution.
  - Numeric real-estate answers must use tool outputs when a relevant tool exists.
- Mandatory v1 tools:
  - Mortgage payment calculator.
  - Ontario land transfer tax calculator.
  - Buyer carrying-cost calculator.
  - Cap-rate and cash-flow calculator.
  - Listing-prep generator using structured property facts.
  - Document Q&A retriever over uploaded files.
- Retrieval pipeline:
  - Upload file to Supabase Storage.
  - Queue parse job.
  - Extract text with page/source metadata.
  - Chunk text with stable chunk IDs.
  - Generate embeddings.
  - Store chunks in `document_chunks`.
  - At answer time, retrieve top chunks by vector similarity plus metadata filters for workspace/project/document.
- Answer modes:
  - Draft mode: faster, agent-reviewed, fewer formal constraints.
  - Export/share mode: requires cited source documents, assumptions, disclaimers, tool provenance, and no uncited legal/financial claims.
- Prompting rules:
  - System prompts must state Eqar is not legal, financial, mortgage, or licensed real-estate advice.
  - The assistant must ask for missing calculator inputs instead of inventing them.
  - The assistant must expose assumptions clearly when estimates are unavoidable.

## Security, Compliance, And Reliability
- Authentication:
  - Browser authenticates with Supabase.
  - FastAPI validates Supabase JWT signature, expiry, issuer, and user ID.
  - Every database access is scoped by workspace/project membership.
- Authorization:
  - Use backend authorization checks plus Supabase RLS for defense in depth.
  - Users cannot access documents, chats, analyses, or exports outside their workspace.
- Secrets:
  - Store OpenAI, Supabase service role, Redis, and deployment secrets in platform environment variables only.
  - Never expose service-role keys to the frontend.
- Upload security:
  - Enforce file type allowlist: PDF, CSV, TXT, DOCX initially.
  - Enforce file size limits.
  - Virus/malware scanning should be added before public launch.
  - Strip active content where possible and never execute uploaded content.
- Data privacy:
  - Treat client names, financials, property documents, and conversations as sensitive.
  - Log metadata and errors, not raw private document text, unless explicitly needed for debugging.
  - Add deletion flow design early: deleting a document must remove storage object, chunks, embeddings, and derived references where legally safe.
- LLM safety:
  - Do not send unnecessary workspace data to LLM providers.
  - Keep model calls scoped to selected conversation/project/document context.
  - Store model/tool traces for debugging and provenance, but redact secrets and sensitive tokens.
- Reliability:
  - Background jobs must be idempotent.
  - Tool runs should be deterministic and versioned.
  - Failed parsing/embedding jobs should retry with bounded attempts and show user-visible status.
  - Long-running analysis should be asynchronous with polling or server-sent events.

## Performance And Efficiency
- Use streaming responses for chat so agents see answers quickly.
- Use background workers for parsing, embeddings, exports, and long analyses.
- Cache:
  - Country-pack constants and tax tables in memory with version keys.
  - Embeddings by document chunk hash.
  - Tool results where inputs, tool version, and country-pack version match.
- Keep prompts lean:
  - Retrieve only relevant chunks.
  - Summarize long documents into reusable project memory after ingestion.
  - Do not dump entire uploaded documents into chat context.
- Database efficiency:
  - Index tenant keys: `workspace_id`, `project_id`, `conversation_id`, `document_id`.
  - Add vector indexes for embeddings.
  - Store large raw text/chunks separately from lightweight message records.
- Frontend speed:
  - Use server-rendered dashboard shell where useful.
  - Keep chat as a focused client component.
  - Lazy-load heavy upload/analysis panels.
  - Use optimistic UI for message creation and upload status.
- Cost control:
  - Track token usage, embedding usage, tool latency, and provider cost per workspace.
  - Add soft workspace usage limits before billing launches.
  - Prefer deterministic calculators over LLM reasoning for numeric work.

## Implementation Milestones
- Milestone 1: Foundation
  - Scaffold monorepo with Next.js, FastAPI, shared lint/test setup, environment templates, and README commands.
  - Configure Supabase Auth, Postgres connection, storage bucket, and initial migrations.
  - Deploy empty frontend/backend to Vercel/Render.
- Milestone 2: Authenticated Dashboard
  - Implement login/logout, protected dashboard, workspace bootstrap, and API JWT verification.
  - Add basic project list and conversation shell.
- Milestone 3: Chat + LLM Adapter
  - Implement OpenAI provider behind `LLMProvider`.
  - Add chat endpoints, streaming response, message persistence, and model error handling.
  - Add usage logging per message.
- Milestone 4: Deterministic Tools
  - Implement mortgage, Ontario land transfer tax, carrying-cost, cap-rate, and cash-flow tools.
  - Add tool registry, schema validation, tool run persistence, and provenance display.
- Milestone 5: Document Upload + Q&A
  - Implement upload flow, parser worker, chunking, embeddings, vector retrieval, and cited document answers.
  - Add document processing statuses and retry handling.
- Milestone 6: Agent Workflows
  - Add saved analyses for listing prep, property analysis, buyer scenario, and client message drafts.
  - Add export/share mode with disclaimers, citations, and calculation assumptions.
- Milestone 7: Hardening
  - Add rate limits, audit logs, error monitoring, file scanning plan, role checks, RLS tests, and usage limits.
  - Add production deployment checklist and security review.

## Test Plan
- Backend unit tests:
  - Calculator formulas with known Ontario/Canada examples.
  - Tool schema validation and invalid input handling.
  - Country-pack versioning and provenance output.
- Backend integration tests:
  - Supabase JWT verification.
  - Workspace authorization boundaries.
  - Chat endpoint persists messages and tool traces.
  - Document upload creates parse jobs and searchable chunks.
- LLM orchestration tests:
  - Numeric questions call tools instead of free-form answers.
  - Missing inputs trigger clarification.
  - Export/share mode includes citations, assumptions, disclaimers, and tool provenance.
- Security tests:
  - Cross-workspace access attempts fail.
  - Service-role secrets are never available to frontend.
  - Unsupported uploads are rejected.
  - Prompt-injection text inside uploaded docs cannot override system/tool rules.
- Frontend tests:
  - Login flow, protected dashboard, chat streaming, upload status, saved analyses, and export mode.
  - Responsive dashboard layouts for desktop and mobile.
- Performance tests:
  - Chat first-token latency target under 2 seconds for normal tool-free responses.
  - Calculator tool response target under 500 ms.
  - Document Q&A retrieval target under 1 second after ingestion.
  - Upload ingestion handled asynchronously without blocking chat.

## Assumptions
- The first production-capable version prioritizes a useful agent dashboard over public widgets, tenant portals, investor-only workflows, or billing.
- OpenAI is the first provider, but the code must not make OpenAI-specific assumptions outside the provider adapter.
- Canada/Ontario ships first; broader country support is enabled through country-pack boundaries, not a fully generic global compliance engine in v1.
- Supabase is the source of truth for auth, database, storage, and vector search unless a concrete limitation appears.
- MLS/CRM integrations remain future work.
- Predictive ML remains future work until Eqar has reliable datasets, evaluation metrics, uncertainty handling, and legal/commercial justification.
