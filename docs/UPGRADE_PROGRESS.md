# Upgrade Progress

## Phase checklist

- [x] Phase 1 — Audit: repository inventory, gap analysis, duplication/risks, file-by-file plan, and baseline status documented.
- [ ] Phase 2 — Core roles
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

## Baseline test results

| Command | Result | Notes |
|---|---|---|
| `python scripts/validate_repo.py` | NOT RUN | This GitHub-only interface has no checkout or shell execution. |
| `python -m unittest discover -s tests -v` | NOT RUN | This GitHub-only interface has no checkout or shell execution. |

No pass/fail result is claimed. Run both commands in a local checkout or CI before Phase 2.

## Open issues

- [ ] Execute and record both baseline commands in an environment with repository checkout and Python.
- [ ] Verify whether existing documentation and platform claims match currently supported runtime versions.
- [ ] Establish a single source of truth for role and skill content before expanding adapters.
- [ ] Define measurable research evidence, domain evaluation, adapter-drift, link, secret, and Termux acceptance checks.
- [ ] Add `docs/EXTENDING.md` in Phase 7 and link every future file from an index.
- [ ] Add README files to all applicable top-level folders in the structure phase, without treating hidden runtime config directories as universally README-driven unless appropriate.
- [ ] Keep all implementation phases blocked until Phase 1 baseline commands are actually run and reviewed.

## Scope boundary

Phase 1 only. Phase 2 has not started.