# Upgrade Progress

## Phase checklist

- [x] Phase 1 — Audit: repository inventory, gap analysis, duplication/risks, file-by-file plan, and baseline status documented.
- [x] Phase 2 — Core roles: portable template, six canonical role contracts, handoff protocol, role index, and thin native wrappers reviewed/updated.
- [x] Phase 3 — Domain roles: nine bounded specialist contracts, role-specific criteria, research obligations, independent Reviewer handoffs, refusal/escalation rules, and thin Claude Code/GitHub Copilot wrappers.
- [x] Phase 4 — Research engine: tiered registry, freshness thresholds, evidence protocol/templates, ethics/no-web rules, Community Pulse, worked cross-check, Deep Researcher integration and indexes. CI validator/unit tests passed.
- [x] Phase 5 — Workflow: canonical stage contracts, simplification/escalation rules, eight role-referencing pipelines, decision record, and indexes updated.
- [ ] Phase 6 — Adapters
- [ ] Phase 7 — Structure/skills/templates
- [ ] Phase 8 — Quality/evals/security/validator
- [ ] Phase 9 — Routing/tools/observability
- [ ] Phase 10 — Dev-domain standards
- [ ] Phase 11 — Design/content standards
- [ ] Phase 12 — Governance
- [ ] Phase 13 — Demo + final report

## Phase 5 changes

- Added `docs/WORKFLOW.md` defining Understand → Research → Plan → Decide → Build → Self-review → Independent review → Test → Document → Handoff → Retrospective.
- Each stage specifies owner, entry/exit criteria, output artifact, and failure/rollback behavior; documented simple-task shortcuts, parallelization constraints, human escalation, and stop conditions.
- Added `workflows/README.md` and eight pipelines: website build, Android app build, plugin/module build, UI/UX design sprint, brand identity project, content campaign, deep research report, and bug fix. Pipelines reference existing role contracts, specify handoffs/gates, and identify safe parallelizable work without duplicating role instructions.
- Recorded ADR-005 in `docs/DECISIONS.md`; linked workflow docs in root README and updated repository map.
- Validation attempt: `git clone` could not resolve github.com in the available shell, so neither `python scripts/validate_repo.py` nor `python -m unittest discover -s tests -v` could execute locally. The GitHub connector exposes no push-run listing/dispatch action, and the commit status endpoint returned no statuses; therefore validator/unit-test results remain **unverified**, not passed. The repository's push-triggered Actions workflow should run in GitHub, but its result must be checked there.

## Phase 4 changes

- Added research/sources.md with four source tiers, per-domain source lists and freshness thresholds.
- Added research/PROTOCOL.md for question definition, multi-tier search, evidence capture, independent cross-checks, version/date applicability, conflicts, staleness, confidence and conclusions.
- Added evidence-log/report templates, worked W3C source-date cross-check and research/logs index.
- Added skills/community-pulse for pain-point research, deduplication, anecdote/pattern weighting and privacy safeguards.
- Linked Deep Researcher and Research Skill to protocol/templates; updated docs/RESEARCH.md, root/skills indexes and progress.
- Official references checked via live search on 2026-10-28; consequential claims require opening the exact source and logging metadata.
- Phase 5 workflow was not started.

## Phase 3 changes

- Added domain role contracts under `agents/`: web developer, Android developer, software developer, plugin/module developer, UI/UX designer, graphic designer/branding, illustrator/visual artist, content creator, and automation/AI tools specialist.
- Followed `templates/_role-template/` structure for role.md, rules.md, tools.md, checklist.md, inputs-outputs.md, examples, and evaluation cases.
- Each role defines scope, when to use/not use, research obligations referencing `docs/RESEARCH.md` as the Phase 4 protocol, an explicit QA/Reviewer handoff, refusal/escalation boundaries, and completion criteria.
- Added thin Claude Code and GitHub Copilot wrappers referencing canonical portable contracts; wrappers do not claim execution or capabilities not verified.
- Updated `agents/README.md` with all core and domain roles, scope summaries, template guidance, and Phase 4 boundary.
- Phase 4 research engine was not started.

## Validation results

- Repository writes were made through the GitHub API; this environment does not provide a checkout/shell for local `python scripts/validate_repo.py` or `python -m unittest discover -s tests -v`. These commands are **not locally run** and no local pass is claimed.
- GitHub Actions validation for implementation commit [9e2ac83](https://github.com/squiraldot/Agent-Team/commit/9e2ac8316e77393322bc2048984ac554262505e1) passed: repository validator, validator unit tests, shell syntax, Claude settings JSON, and YAML parsing all succeeded. The README index-only follow-up commit [ce45188](https://github.com/squiraldot/Agent-Team/commit/ce451889c305831b6ad0017a68eb6be07ba891e7) also passed the same workflow.
- Local shell execution was unavailable here; CI executed the validator and tests in a real checkout. Static validation and unit tests do not establish runtime agent execution, platform compatibility, or security assurance.

## Scope boundary

Phase 5 only. Do not begin Phase 6 or any later phase in this change.
