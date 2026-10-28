# Upgrade Progress

## Phase checklist

- [x] Phase 1 — Audit: repository inventory, gap analysis, duplication/risks, file-by-file plan, and baseline status documented.
- [x] Phase 2 — Core roles: portable template, six canonical role contracts, handoff protocol, role index, and thin native wrappers reviewed/updated.
- [ ] Phase 3 — Domain roles
- [ ] Phase 4 — Research engine
- [ ] Phase 5 — Workflow
- [ ] Phase 6 — Adapters
- [ ] Phase 7 — Structure/skills/templates
- [ ] Phase 8 — Quality/evals/security/validator
- [ ] Phase 9 — Routing/tools/observability
- [ ] Phase 10 — Dev-domain standards
- [ ] Phase 11 — Design/content standards
- [ ] Phase 12 — Governance
- [ ] Phase 13 — Demo + final report

## Phase 2 changes

- Completed the reusable `templates/_role-template/` contract, including good/bad examples and starter evaluation cases.
- Confirmed canonical roles: Orchestrator, Planner, Deep Researcher, Builder, QA/Reviewer, and Security & Privacy Reviewer.
- Aligned `docs/AGENT_PROTOCOL.md` terminology and routing guidance with the canonical roles and handoff contract.
- Updated `agents/README.md` as the role index and template entry point.
- Native Claude Code and GitHub Copilot agent files reference portable role files instead of duplicating role policy.
- Scope held at Phase 2; no domain roles or research engine were started.

## Validation results

CI run for implementation commit [782ccd2](https://github.com/squiraldot/Agent-Team/commit/782ccd2e5db465e2d64cf5da28a662673532b4c5): [all workflow checks passed](https://github.com/squiraldot/Agent-Team/actions/runs/40656001733).

| Check | Result | Evidence |
|---|---|---|
| `python scripts/validate_repo.py` | PASS | GitHub Actions step “Validate repository structure and configuration” succeeded. |
| `python -m unittest discover -s tests -v` | PASS | GitHub Actions step “Run validator unit tests” succeeded. |
| Shell syntax, Claude settings JSON, YAML parsing | PASS | Remaining workflow steps succeeded. |

These are CI results for the implementation commit, not claims of runtime agent execution or security assurance.

## Files touched in Phase 2

- `templates/_role-template/examples/good.md`
- `templates/_role-template/examples/bad.md`
- `templates/_role-template/evals/cases.md`
- `docs/AGENT_PROTOCOL.md`
- `docs/UPGRADE_PROGRESS.md`
- `agents/README.md`

Existing role contracts, role index, and native wrappers were inspected and retained where already aligned; no unnecessary rewrites were made.

## Open issues

- [ ] Verify whether existing documentation and platform claims match currently supported runtime versions.
- [ ] Add `docs/EXTENDING.md` in Phase 7 and link every future file from an index.
- [ ] Define broader adapter-drift, link, secret, and Termux acceptance checks in Phase 8.

## Scope boundary

Phase 2 only. Do not begin Phase 3 until explicitly requested.
