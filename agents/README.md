# Portable agent roles

The role directories are the canonical, runtime-neutral contracts. Each role directory contains `role.md`, `rules.md`, `tools.md`, `checklist.md`, `inputs-outputs.md`, `examples/`, and `evals/`. Native runtime files should be thin wrappers that reference these contracts rather than copy their instructions.

## Core roles

| Role | Canonical contract | Use |
|---|---|---|
| Orchestrator | [orchestrator/role.md](orchestrator/role.md) | Decompose tasks, select roles, sequence/parallelize, escalate, and stop safely. |
| Planner | [planner/role.md](planner/role.md) | Define scope, assumptions, dependencies, risks, acceptance criteria, and validation. |
| Deep Researcher | [deep-researcher/role.md](deep-researcher/role.md) | Specify evidence-first research outputs. The research engine is deferred to Phase 4. |
| Builder | [builder/role.md](builder/role.md) | Implement scoped work and report actual verification. |
| QA/Reviewer | [qa-reviewer/role.md](qa-reviewer/role.md) | Independently review output against criteria; never review its own work. |
| Security & Privacy Reviewer | [security-privacy-reviewer/role.md](security-privacy-reviewer/role.md) | Assess trust boundaries, permissions, data flows, and consequential side effects. |

Each role's `role.md` includes front matter: `name`, `description`, `version`, `owner`, and `status`.

## Add a role

1. Copy [`templates/_role-template/`](../templates/_role-template/) to a new kebab-case directory under `agents/`.
2. Replace template front matter and fill out all role, rules, tools, checklist, handoff, example, and evaluation files.
3. Keep the role bounded; state when not to use it and how to degrade gracefully when tools are missing.
4. Add it to this index and create only thin native wrappers for runtimes that support them.
5. Check alignment with [the handoff protocol](../docs/AGENT_PROTOCOL.md) and [shared policy](../AGENTS.md).

## Legacy paths

The flat files `planner.md`, `builder.md`, `researcher.md`, `reviewer.md`, and `router.md` remain as compatibility links to canonical role directories. Update the directory contracts, not the legacy summaries.
