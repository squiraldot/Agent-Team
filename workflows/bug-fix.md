# Bug-fix pipeline

**Use for:** a reported defect or regression with a reproducible or investigable failure.

## Ordered roles and handoffs

1. **Orchestrator** — [agents/orchestrator/role.md](../agents/orchestrator/role.md): impact, severity, affected versions/users, scope and safety/production constraints.
2. **Planner** — [agents/planner/role.md](../agents/planner/role.md): expected vs actual behavior, reproduction plan, likely boundaries, acceptance test and rollback path.
3. **Deep Researcher** — [agents/deep-researcher/role.md](../agents/deep-researcher/role.md), when behavior depends on external API, version change, or unfamiliar system: evidence log or explicit not-needed rationale.
4. **Relevant domain developer** — choose the matching existing role, such as [Software Developer](../agents/software-developer/role.md), [Web Developer](../agents/web-developer/role.md), [Android Developer](../agents/android-developer/role.md), or [Plugin/Module Developer](../agents/plugin-module-developer/role.md): reproduce before editing; isolate root cause; add a failing regression test where practical; fix the smallest causal change.
5. **Builder self-review** — inspect diff and adjacent paths; run focused tests and broader relevant regression checks.
6. **QA/Reviewer** — [agents/qa-reviewer/role.md](../agents/qa-reviewer/role.md): independently verify reproduction, regression test, fix scope, and possible side effects.
7. **Security & Privacy Reviewer** — [agents/security-privacy-reviewer/role.md](../agents/security-privacy-reviewer/role.md), if the defect touches trust boundaries, auth, secrets, permissions, user data or privileged operations.
8. **Domain developer / Builder** — resolve findings, rerun failed and regression checks, update docs if behavior/interface changed.
9. **Orchestrator** — handoff root cause, change, exact commands/results, limitations and rollback instructions.

## Quality gates

- Capture expected/actual behavior and reproducible evidence before changing code, unless an urgent safe mitigation is needed.
- Prefer a regression test that fails before and passes after the fix.
- Do not mask a symptom with broad retries, swallowed errors, or unrelated refactors.
- Test failures must be investigated; if environment prevents execution, say so and provide reproduction instructions.
- Production hotfixes, data repair, deployment or rollback actions require human approval where they affect external systems.

## Parallelizable work

One worker may investigate a distinct failure hypothesis while another prepares isolated test fixtures, but only after reproduction steps and ownership are clear. Do not have multiple workers patch the same root cause concurrently.
