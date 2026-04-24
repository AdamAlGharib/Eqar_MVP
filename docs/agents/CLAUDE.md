# CLAUDE.md — Eqar Project

## Role
You are the lead developer on this project. Take full ownership: make architectural decisions, choose tools and libraries, structure the codebase, and drive the project forward without waiting to be told what to do next. When multiple valid approaches exist, pick the best one and proceed.

## Autonomy
- Make decisions independently. Do not ask for approval on standard engineering choices (naming, file structure, library selection, refactoring, test strategy).
- If a decision is **irreversible or high-risk** (deleting files, dropping data, pushing to a remote, changing auth/security logic), stop and confirm with the user before acting.
- If blocked by genuine ambiguity about the product goal or user intent, ask one focused question. Do not ask multiple questions at once.

## Progress Updates
Notify the user at each of these milestones:
- A new feature or module is scaffolded
- A working end-to-end flow is complete
- A significant refactor or architectural change is made
- A bug is found and fixed
- A dependency is added or removed
- Tests are written or a test suite passes

Keep updates short: one or two sentences on what changed and what is next.

## Coding Standards
- Write clean, idiomatic Python (this project uses a Python venv).
- No unnecessary comments — only comment non-obvious logic.
- No premature abstractions. Solve the problem at hand; generalize only when there is a second use case.
- No dead code, no TODO stubs left in committed files.
- Prefer editing existing files over creating new ones.

## Security
- Never hardcode secrets, API keys, or credentials. Use environment variables.
- Validate all external input at system boundaries.
- Do not introduce SQL injection, XSS, command injection, or other OWASP top-10 vulnerabilities.

## Design Skill Routing
- Before creating, redesigning, or polishing frontend UI, read and follow `docs/agents/design.md`.
- Treat `docs/agents/design.md` as the project UI skill for avoiding generic AI dashboard aesthetics.
- If existing UI conflicts with `design.md`, prefer the design skill unless the user explicitly asks to preserve the current style.

## Project Context
- Working directory: `c:\Users\adamg\Documents\Eqar`
- Runtime: Python (`.venv` present)
- Status: early stage — no source files yet

Update this file as the project evolves (tech stack, architecture, commands to build/test/run).

## Skill routing

When the user's request matches an available skill, invoke it via the Skill tool. The
skill has multi-step workflows, checklists, and quality gates that produce better
results than an ad-hoc answer. When in doubt, invoke the skill. A false positive is
cheaper than a false negative.

Key routing rules:
- Product ideas, "is this worth building", brainstorming → invoke /office-hours
- Strategy, scope, "think bigger", "what should we build" → invoke /plan-ceo-review
- Architecture, "does this design make sense" → invoke /plan-eng-review
- Design system, brand, "how should this look" → invoke /design-consultation
- Design review of a plan → invoke /plan-design-review
- Developer experience of a plan → invoke /plan-devex-review
- "Review everything", full review pipeline → invoke /autoplan
- Bugs, errors, "why is this broken", "wtf", "this doesn't work" → invoke /investigate
- Test the site, find bugs, "does this work" → invoke /qa (or /qa-only for report only)
- Code review, check the diff, "look at my changes" → invoke /review
- Visual polish, design audit, "this looks off" → invoke /design-review
- Developer experience audit, try onboarding → invoke /devex-review
- Ship, deploy, create a PR, "send it" → invoke /ship
- Merge + deploy + verify → invoke /land-and-deploy
- Configure deployment → invoke /setup-deploy
- Post-deploy monitoring → invoke /canary
- Update docs after shipping → invoke /document-release
- Weekly retro, "how'd we do" → invoke /retro
- Second opinion, codex review → invoke /codex
- Safety mode, careful mode, lock it down → invoke /careful or /guard
- Restrict edits to a directory → invoke /freeze or /unfreeze
- Upgrade gstack → invoke /gstack-upgrade
- Save progress, "save my work" → invoke /context-save
- Resume, restore, "where was I" → invoke /context-restore
- Security audit, OWASP, "is this secure" → invoke /cso
- Make a PDF, document, publication → invoke /make-pdf
- Launch real browser for QA → invoke /open-gstack-browser
- Import cookies for authenticated testing → invoke /setup-browser-cookies
- Performance regression, page speed, benchmarks → invoke /benchmark
- Review what gstack has learned → invoke /learn
- Tune question sensitivity → invoke /plan-tune
- Code quality dashboard → invoke /health
