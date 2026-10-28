# Website build pipeline

**Use for:** a new website or substantial site feature. For a single isolated defect, use [bug-fix](bug-fix.md).

## Ordered roles and handoffs

1. **Orchestrator** — [agents/orchestrator/role.md](../agents/orchestrator/role.md): task brief, scope boundaries, risk, approval gates.
2. **Planner** — [agents/planner/role.md](../agents/planner/role.md): page map, user flows, technical plan, acceptance criteria, test/rollback plan.
3. **Deep Researcher** — [agents/deep-researcher/role.md](../agents/deep-researcher/role.md) with [Web Developer](../agents/web-developer/role.md): evidence for framework/API versions, browser support, accessibility, SEO, hosting constraints. Pass a dated evidence log or explicit not-needed rationale.
4. **UI/UX Designer** — [agents/ui-ux-designer/role.md](../agents/ui-ux-designer/role.md): user flows, responsive states, component/design specs. Pass annotated design decisions and edge states.
5. **Web Developer** — [agents/web-developer/role.md](../agents/web-developer/role.md): implement in small vertical slices; pass diff, run/build instructions, tests, configuration and migration notes.
6. **QA/Reviewer** — [agents/qa-reviewer/role.md](../agents/qa-reviewer/role.md): independent review report against acceptance criteria.
7. **Security & Privacy Reviewer** — [agents/security-privacy-reviewer/role.md](../agents/security-privacy-reviewer/role.md): required for auth, personal data, payments, uploads, admin, or external integrations; pass risk findings and mitigations.
8. **Builder / Web Developer** — resolve findings, run checks, update documentation and index.
9. **Orchestrator** — handoff summary: artifacts, exact test evidence, known gaps, and any pending approval.

## Quality gates

- Requirements and responsive states are testable; accessibility and error/loading/empty states are considered.
- Dependency/API choices are version-aware and evidence-backed where material.
- Build, lint, unit/integration tests, and browser/manual checks run when available; report exact environment and skipped checks.
- Secrets stay out of source; auth/data/payment paths receive security review.
- Deploy, publish, or change production only after explicit human approval.

## Parallelizable work

Researcher can research hosting/API constraints while UI/UX Designer maps flows after scope is stable. QA can prepare a test matrix while implementation proceeds. Keep design and code contracts explicit; do not concurrently edit the same files. Parallel execution is conditional on verified runtime support.
