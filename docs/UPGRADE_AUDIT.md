# Upgrade Audit

## Scope and method

Baseline snapshot: `main` at `a3d2d5c32635ae6f7a11e9481da1d66a116752bb` (70 tracked files at audit time). Repository tree and key policy, architecture, validator, and test files were inspected through the GitHub repository interface. This environment does not provide a shell or checkout, so the requested Python commands could not be executed here; no test outcome is inferred. The audit is a repository-level plan, not a claim of runtime verification.

## What exists

- Provider-neutral policy in `AGENTS.md`, portable role references in `agents/`, and native examples for Claude Code, Codex, Gemini CLI, GitHub Copilot, and Cursor.
- Five roles: Planner, Researcher, Builder, Reviewer, Router.
- Reusable skills and playbooks for research, writing, design, automation, prompts, content, growth, and product work.
- Architecture, protocol, compatibility, provider-adapter, multi-provider, platform-matrix, operations, research, security, incident, release, evaluation, and production-readiness documentation.
- A provider-neutral YAML example, Claude hooks/settings, a Python standard-library static validator, unit tests, and a GitHub Actions validation workflow.
- Project memory and contribution/security guidance.

## Gaps against the brief

1. No documented end-to-end, phase-gated upgrade plan existed before this change; this audit/brief/progress set establishes it.
2. No `docs/EXTENDING.md` newcomer guide is present; future work must define how to add an agent without duplicating policy.
3. Domain-specific agent coverage is incomplete for Android, software engineering, plugin/module development, deep research, web, planning specialization, graphic design, UI/UX, illustration, and content creation.
4. Research process needs explicit repeatable evidence logs, source-quality/conflict handling, freshness, and review gates; model training knowledge cannot be fully disabled.
5. Workflow execution, capability discovery, adapters, tool routing, observability, and bounded orchestration are primarily described rather than implemented as a verified executable framework.
6. `PLATFORM_MATRIX.md` and all adapter examples need a cross-file consistency review against `AGENTS.md` and evidence for exact versions; documentation alone does not establish execution support.
7. Validator coverage is narrow: required paths, JSON shape, fallback default, and a few secret patterns. It does not validate all docs/links, adapter drift, README coverage, or every secret surface.
8. Existing skills and runtime-native wrappers overlap by design; the canonical-vs-adapter relationship needs explicit ownership and drift checks.
9. The README repository map omits some directories/files and does not yet link an upgrade index.
10. Several hidden/runtime-specific directories lack README files; adding these should be staged deliberately and checked for runtime compatibility rather than done as incidental churn.
11. Baseline validator and tests remain unverified in this execution environment; run them in a real checkout before treating acceptance as satisfied.

## Duplication and risks

- Role responsibilities are represented in `agents/`, `.claude/agents/`, and `.github/agents/`; this creates policy drift risk. Keep `AGENTS.md` canonical and make adapters thin.
- Research, design, writing, automation, and prompt guidance appears in portable skills and native skill wrappers. Define one canonical source per reusable workflow and link wrappers to it where supported.
- Platform capability statements can age quickly; record runtime, version, model ID, tool permissions, date, and test evidence before using “verified.”
- Hooks are not a sandbox. Repository, web, tool, and model outputs are untrusted; secrets, prompt injection, and excessive permissions remain risks.
- A markdown role is not an executing subagent; do not imply orchestration, parallelism, persistence, or external tool access unless implemented and tested.
- Static checks passing would not prove runtime behavior, security, quality, or compatibility.
- Broad domain ambitions can produce shallow, duplicated agent prompts unless each role has a bounded contract, clear inputs/outputs, escalation rules, and evaluation cases.

## File-by-file plan

Legend: **Create** = planned future addition; **Modify** = planned review/update; **Leave** = retain unless evidence shows a defect. Phase 1 changes are limited to this brief, this audit, progress tracking, and README links. Do not start Phase 2 in this commit.

### Root
- `README.md` — **Modify now**: index the three upgrade documents; future phases keep map and compatibility claims truthful.
- `AGENTS.md` — **Leave now; modify in Phase 2/12** only for canonical policy improvements.
- `CLAUDE.md` — **Leave now; modify in Phase 6** to stay a thin adapter.
- `GEMINI.md` — **Leave now; modify in Phase 6** after checking actual CLI support.
- `CONTRIBUTING.md` — **Modify in Phase 12** for governance and contributor checks.
- `SECURITY.md` — **Modify in Phase 8/12** to align disclosure and secret handling with expanded framework.
- `LICENSE` — **Leave** unless scope/licensing changes require review.
- `.gitignore` — **Modify in Phase 8** if new generated artifacts or local evidence files need exclusions.
- `run.sh` — **Modify in Phase 5/8** only after portable workflow behavior and Termux requirements are defined.

### Runtime adapters and agent references
- `.claude/CLAUDE.md` — **Modify in Phase 6** to reference shared policy without contradictions.
- `.claude/agents/planner.md`, `.claude/agents/researcher.md`, `.claude/agents/builder.md`, `.claude/agents/reviewer.md`, `.claude/agents/router.md` — **Modify in Phase 2/6** as thin, tested native role adapters.
- `.claude/hooks/pre-tool-use.sh`, `.claude/hooks/post-tool-use.sh`, `.claude/hooks/session-start.sh`, `.claude/hooks/stop.sh` — **Review/modify in Phase 8/9**; inspect for safety, portability, and bounded side effects.
- `.claude/settings.json` — **Review/modify in Phase 6/8**; validate schema and safe defaults.
- `.claude/skills/automation/SKILL.md`, `.claude/skills/design/SKILL.md`, `.claude/skills/prompts/SKILL.md`, `.claude/skills/research/SKILL.md`, `.claude/skills/writing/SKILL.md` — **Modify in Phase 7** to remove duplicated policy and point to canonical portable skills.
- `.agents/skills/agent-research/SKILL.md`, `.agents/skills/agent-review/SKILL.md` — **Modify in Phase 7** for parity with canonical workflows.
- `.cursor/rules/agent-team.mdc` — **Modify in Phase 6** as a concise adapter to `AGENTS.md`.
- `.github/copilot-instructions.md` — **Modify in Phase 6** as a concise adapter to `AGENTS.md`.
- `.github/agents/planner.agent.md`, `.github/agents/researcher.agent.md`, `.github/agents/builder.agent.md`, `.github/agents/reviewer.agent.md`, `.github/agents/router.agent.md` — **Modify in Phase 2/6** to align role contracts without implying unsupported execution.
- `.github/workflows/validate.yml` — **Modify in Phase 8** to run expanded standard-library checks and tests.
- `.github/ISSUE_TEMPLATE/bug_report.yml`, `.github/PULL_REQUEST_TEMPLATE.md` — **Modify in Phase 12** to capture evidence, tests, risk, and compatibility claims.

### Portable roles, skills, playbooks, and config
- `agents/planner.md`, `agents/researcher.md`, `agents/builder.md`, `agents/reviewer.md`, `agents/router.md` — **Modify in Phase 2** as canonical role contracts.
- `skills/README.md`, `skills/automation/README.md`, `skills/design/README.md`, `skills/prompts/README.md`, `skills/research/README.md`, `skills/writing/README.md` — **Leave now; modify in Phase 7** to index canonical workflow sources and new skills.
- `playbooks/README.md`, `playbooks/content/README.md`, `playbooks/growth/README.md`, `playbooks/product/README.md` — **Leave now; modify in Phase 7/11** for updated templates and domain standards.
- `config/agent-team.example.yaml` — **Leave now; modify in Phase 6/9** only alongside documented schema/capability semantics.
- `memory/MEMORY.md` — **Leave now; modify in Phase 12** with curated, non-secret durable decisions and no unverified claims.

### Existing documentation
- `docs/AGENT_PROTOCOL.md` — **Modify in Phase 2/5** for structured role contracts and handoffs.
- `docs/ARCHITECTURE.md` — **Modify in Phase 5/9** to distinguish specification from executable components.
- `docs/COMPATIBILITY.md` — **Modify in Phase 6/8** for exact-runtime evidence policy.
- `docs/DECISIONS.md` — **Modify in Phase 12** to record approved architecture decisions.
- `docs/EVALUATION.md` — **Modify in Phase 8** for per-domain regression and runtime evaluation.
- `docs/INCIDENT_RESPONSE.md` — **Modify in Phase 8/12** for expanded tool/workflow failure modes.
- `docs/MULTI_PROVIDER.md` — **Modify in Phase 6/9** for honest adapter boundaries.
- `docs/OPERATIONS.md` — **Modify in Phase 5/9** for runbooks and observability, if implemented.
- `docs/PLATFORM_MATRIX.md` — **Modify in Phase 6** after evidence-based audit of each integration.
- `docs/PRODUCTION_READINESS.md` — **Modify in Phase 8/12** for measurable release gates.
- `docs/PROVIDER_ADAPTER.md` — **Modify in Phase 6** for capability detection and explicit unsupported-feature behavior.
- `docs/RELEASE_CHECKLIST.md` — **Modify in Phase 8/12** to require test evidence and documentation index checks.
- `docs/RESEARCH.md` — **Modify in Phase 4** for repeatable research, citations, conflicts, and evidence logs.
- `docs/SECURITY.md` — **Modify in Phase 8** for untrusted tool output and least-privilege controls.
- `docs/UPGRADE_BRIEF.md` — **Create now**; immutable user-provided scope and phase map.
- `docs/UPGRADE_AUDIT.md` — **Create now**; findings and file-by-file plan.
- `docs/UPGRADE_PROGRESS.md` — **Create now**; phase checklist and truthful baseline status.
- `docs/EXTENDING.md` — **Create in Phase 7**; newcomer guide for adding agents and indexing every new file.
- Additional research evidence logs, templates, standards, routing/tool/observability docs, domain-role specs, and demo assets — **Create in their mapped phases only**, each linked from an index and covered by tests/evals where appropriate.

### Validation and tests
- `scripts/validate_repo.py` — **Modify in Phase 8**; preserve standard-library-only and Android Termux compatibility while expanding checks.
- `tests/test_validate_repo.py` — **Modify in Phase 8** for new invariants, edge cases, links, README coverage, adapter drift, and secret checks.
- Add domain/workflow/evaluation tests — **Create in Phase 8/13** only with deterministic fixtures and documented limitations.

## Phase sequencing

1. Audit — current phase; inventory, baseline status, gaps, and plan.
2. Core roles — canonical contracts and handoff invariants.
3. Domain roles — specialist roles with explicit boundaries.
4. Research engine — source discovery, evidence logs, conflict handling, freshness.
5. Workflow — bounded, auditable orchestration and approvals.
6. Adapters — capability-aware mappings to runtime-specific formats.
7. Structure/skills/templates — indexes, README coverage, and `docs/EXTENDING.md`.
8. Quality/evals/security/validator — regression, secrets, links, safety, and Termux checks.
9. Routing/tools/observability — explicit capabilities, budgets, traces, failure reporting.
10. Dev-domain standards — Android, software, plugin/module development.
11. Design/content standards — graphic design, UI/UX, illustration, content creation.
12. Governance — decisions, contribution/release policy, evidence and maintenance ownership.
13. Demo + final report — end-to-end demonstration, verified evidence, residual risks.

## Baseline commands

- `python scripts/validate_repo.py` — **NOT RUN**: no repository checkout/shell execution is available in this interface.
- `python -m unittest discover -s tests -v` — **NOT RUN**: no repository checkout/shell execution is available in this interface.
- Results are deliberately not inferred from source inspection. Run both commands in a real checkout before proceeding.
