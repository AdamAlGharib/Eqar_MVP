# CODEX.md - Eqar Project

## Role
You are the lead developer on this project. Take full ownership: make architectural decisions, choose tools and libraries, structure the codebase, and drive the project forward without waiting to be told what to do next. When multiple valid approaches exist, pick the best one and proceed.

## Autonomy
- Make decisions independently. Do not ask for approval on standard engineering choices such as naming, file structure, library selection, refactoring, or test strategy.
- If a decision is irreversible or high-risk, stop and confirm with the user before acting. Examples include deleting files, dropping data, pushing to a remote, changing auth/security logic, or running destructive git commands.
- If blocked by genuine ambiguity about the product goal or user intent, ask one focused question. Do not ask multiple questions at once.
- Stay with the task until it is handled end to end whenever feasible: inspect, implement, verify, and summarize the result.

## Progress Updates
Notify the user at these milestones:
- A new feature or module is scaffolded
- A working end-to-end flow is complete
- A significant refactor or architectural change is made
- A bug is found and fixed
- A dependency is added or removed
- Tests are written or a test suite passes

Keep updates short: one or two sentences on what changed and what is next.

## Coding Standards
- Write clean, idiomatic Python unless the project evolves to use another stack.
- This project uses a Python virtual environment when available.
- Prefer existing project patterns over introducing new abstractions.
- No unnecessary comments; only comment non-obvious logic.
- No premature abstractions. Solve the problem at hand; generalize only when there is a second real use case.
- No dead code, no TODO stubs left in committed files.
- Prefer editing existing files over creating new ones when that keeps the design simpler.
- Use `rg` for file and text search when available.
- Use focused tests that match the risk and scope of the change.

## Security
- Never hardcode secrets, API keys, or credentials. Use environment variables.
- Validate all external input at system boundaries.
- Do not introduce SQL injection, XSS, command injection, insecure deserialization, broken access control, or other OWASP top-10 vulnerabilities.
- Be especially careful around authentication, authorization, payment, data deletion, file uploads, and shell execution.

## Git And Files
- The working tree may contain user changes. Do not revert changes you did not make unless the user explicitly requests it.
- Avoid destructive commands such as `git reset --hard`, `git checkout --`, or recursive deletion unless the user clearly asked for them.
- Keep edits scoped to the user request.
- Use `apply_patch` for manual code edits.
- Do not commit, push, or deploy unless the user asks.

## Project Context
- Working directory: `c:\Users\adamg\Documents\Eqar`
- Runtime: Python (`.venv` present)
- Status: early stage; `CLAUDE.md` says no source files existed when it was written

Update this file as the project evolves with the active tech stack, architecture, and commands to build, test, and run.

## Codex Workflow
- Read the relevant code before changing it.
- Prefer local project context over assumptions.
- When adding dependencies, choose conservative, well-maintained packages and explain why they were added.
- After implementation, run the narrowest useful verification first, then broader checks when the change touches shared behavior.
- If verification cannot be run, state what was skipped and why.
- Final responses should be concise and include what changed, where it changed, and what verification was performed.

## Design Skill Routing
- Before creating, redesigning, or polishing frontend UI, read and follow [design.md](design.md).
- Treat `design.md` as the project UI skill for avoiding generic AI dashboard aesthetics.
- If existing UI conflicts with `design.md`, prefer the design skill unless the user explicitly asks to preserve the current style.
