# Architecture

## Purpose and non-goals

Agent-Team is a repository-level specification and set of native configuration examples for planning, research, implementation, review, and routing. It is designed to work at the instruction/workflow layer across multiple coding-agent runtimes.

It is **not currently** a universal provider API gateway, durable distributed orchestrator, managed service, secure sandbox, or proof that every model/runtime combination is compatible.

## Layered architecture

```text
User request
    |
    v
Router / Planner ---- clarify with user when requirements materially affect outcome
    |
    +---- Researcher (current/evidence-sensitive claims)
    |
    +---- Builder (scoped artifact or code change)
    |
    +---- Reviewer (independent acceptance/security/evidence check)
    |
    v
Human approval for consequential external or irreversible actions
    |
    v
Handoff: artifacts + evidence + tests + limitations
```

### Layer 1 — Shared policy

- `AGENTS.md` is the provider-neutral source of truth.
- `agents/` contains role prompt references.
- `playbooks/` and `skills/` contain reusable workflows.
- `docs/AGENT_PROTOCOL.md` defines portable handoff expectations.

### Layer 2 — Native runtime adapters

- Claude Code: `CLAUDE.md`, `.claude/agents/`, `.claude/skills/`, `.claude/settings.json`, and `.claude/hooks/`.
- OpenAI Codex: `AGENTS.md` and `.agents/skills/`.
- Gemini CLI: `GEMINI.md` plus runtime-specific settings and agent definitions where supported.
- GitHub Copilot: `.github/copilot-instructions.md` and `.github/agents/*.agent.md` examples.
- Cursor: `.cursor/rules/`.

Native configuration examples do not imply that every runtime supports the same hooks, tools, parallelism, model IDs, or approval semantics. See `docs/PLATFORM_MATRIX.md`.

### Layer 3 — Configuration and capabilities

`config/agent-team.example.yaml` describes provider-neutral preferences. It is not consumed automatically by each CLI. A future executable adapter must parse it, validate it, discover capabilities, translate only supported settings, and fail visibly when a required capability is missing.

### Layer 4 — Validation and operations

- `scripts/validate_repo.py`: static repository/configuration checks.
- `tests/`: deterministic unit tests for the validator.
- `.github/workflows/validate.yml`: CI execution of static checks.
- `docs/EVALUATION.md`: model/runtime evaluation plan and test matrix.
- `docs/PRODUCTION_READINESS.md`: release gates and operational metrics.
- `docs/INCIDENT_RESPONSE.md`: incident containment and recovery.

Passing static checks does not prove agent behavior or security.

## Design principles

1. **One canonical policy:** keep common requirements in `AGENTS.md`; native files should be thin, consistent adapters.
2. **Capability-first:** select tools and models by verified capabilities, not brand assumptions.
3. **Least privilege:** give each runtime the minimum access needed for the task.
4. **Explicit state:** hand off structured outputs rather than relying on implicit conversation memory.
5. **Bounded autonomy:** limit retries, steps, cost, delegation depth, and side effects.
6. **Evidence over confidence:** claims require sources, tests, or direct observation.
7. **Independent review:** high-risk changes require a reviewer distinct from the builder where feasible.
8. **Human authority:** external and irreversible actions require explicit approval.
9. **Portable core, native edges:** do not flatten real runtime differences into false compatibility promises.
10. **Auditable completion:** report changed paths, commands, actual results, and remaining gaps.

## Trust boundaries

Treat user-supplied files, repository content, web pages, tool outputs, model output, MCP responses, and logs as untrusted data. They may contain prompt injection or misleading instructions. Only the applicable trusted policy and user authorization define permitted actions.

Hooks are process automation, not a general security boundary. Use OS/container isolation, restricted credentials, network policy, and backups for risky work.

## Failure modes

- Missing capability: stop or offer an alternative; do not fake execution.
- Invalid config: fail early with an actionable message.
- Repeated tool failure: stop after a bounded retry budget.
- Conflicting evidence: surface the conflict and uncertainty.
- Partial execution: report completed and incomplete steps separately.
- Approval missing: pause before the consequential action.
- Context loss: recover from durable artifacts and source control rather than inventing prior state.
