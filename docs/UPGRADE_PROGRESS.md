# Upgrade Progress

## Phase checklist

- [x] Phase 1 — Audit: repository inventory, gap analysis, duplication/risks, file-by-file plan, and baseline status documented.
- [x] Phase 2 — Core roles: portable template, six canonical role contracts, handoff protocol, role index, and thin native wrappers reviewed/updated.
- [x] Phase 3 — Domain roles: nine bounded specialist contracts, role-specific criteria, research obligations, independent Reviewer handoffs, refusal/escalation rules, and thin Claude Code/GitHub Copilot wrappers.
- [x] Phase 4 — Research engine: tiered registry, freshness thresholds, evidence protocol/templates, ethics/no-web rules, Community Pulse, worked cross-check, Deep Researcher integration and indexes. CI validator/unit tests passed.
- [x] Phase 5 — Workflow: canonical stage contracts, simplification/escalation rules, eight role-referencing pipelines, decision record, and indexes updated.
- [x] Phase 6 — Adapters: official docs reviewed and dated, thin generated adapters, drift checker and unit tests, generic/direct-API specs, matrix, CI check, and indexes updated.
- [x] Phase 7 — Structure/skills/templates: reusable skill catalog, PRD/design/tech/test/PR/retrospective/release templates, canonical Phase 4 research-template link, five-minute extension guide, indexes, and changelog
- [x] Phase 8 — Quality/evals/security/validator: role scenario suite, scoring/regression protocol, quality gates, expanded static validator and unit tests, CI checks, security and memory policies
- [x] Phase 9 — Routing/tools/observability
- [x] Phase 10 — Dev-domain standards
- [x] Phase 11 — Design/content standards
- [ ] Phase 12 — Governance
- [ ] Phase 13 — Demo + final report


## Phase 10 changes

- Added `docs/standards/README.md` and four standards: web, Android, plugins/modules, and software engineering. Each covers evidence-backed stack defaults and alternatives, conventions, sample structure, testing, security, accessibility/performance where relevant, release checks, pitfalls, source access dates, unverified items, and a revalidation date of 2027-01-28.
- Followed `research/PROTOCOL.md`: consulted official MDN, Chrome for Developers, Android Developers/Google Play, WordPress Developer Resources, Python and GitHub documentation, and OWASP. Current, volatile policy claims (notably Play target API) are explicitly marked for rechecking. Exact project-specific toolchain/framework versions remain UNVERIFIED rather than guessed.
- Linked standards from all four matching domain roles and the website-build, Android-app-build, plugin-module-build, and bug-fix pipelines. Updated root/docs/workflow indexes and extended repository index validation with a focused unit test.
- Verification limitation: this GitHub API interface has no checkout or shell, so `python scripts/validate_repo.py` and `python -m unittest discover -s tests -v` could not be executed here. No local test pass is claimed; check CI for the final commit before relying on validation. Phase 11 was not started.

## Phase 8 changes

- Added `evals/` scenario specifications for Planner, Researcher, Builder, Reviewer, Router, Security & Privacy Reviewer, and domain specialists. Cases include inputs, expected behavior, 0–2 rubrics, and red flags for fabricated sources, skipped research, self-review, injection, and unsafe side effects.
- Expanded `docs/EVALUATION.md` with scoring and regression workflow; added `docs/QUALITY_GATES.md` covering research, design, code, security, content, and release criteria.
- Extended `scripts/validate_repo.py` with required role-contract checks, YAML front-matter/SemVer validation, relative Markdown link checks, secret-pattern scanning, unresolved placeholder checks, and index coverage checks. Added focused unit tests for each helper.
- Updated CI to retain validator, adapter `--check`, unit tests, shell syntax, and config parsing; workflow already ran these commands, so its command coverage remains intact.
- Updated `docs/SECURITY.md` for least privilege, untrusted fetched/tool content, no repository secrets, and explicit human approvals for high-impact actions. Rewrote `memory/MEMORY.md` with allowed format, prohibited data, and pruning rules.
- Added `docs/README.md` and linked quality gates and role evaluations from the root README.
- Verification limitation: this interface has no checkout/shell and exposes no workflow-dispatch action. Validator and unit tests have **not been executed here**; CI status for the latest commit was not available. Do not treat acceptance as verified until the commands run in CI or a local checkout.


- Final check status: validator and unit tests could not be executed in this GitHub-file-only session; no CI pass is claimed. The workflow is configured to run `python scripts/validate_repo.py`, `python scripts/sync_platforms.py --check`, and `python -m unittest discover -s tests -v` on pushes/PRs. Phase 9 remains untouched.

## Phase 7 changes

- Added nine reusable skills with YAML front matter, trigger conditions, steps, checklists, failure modes, and links to canonical shared guidance.
- Added templates for PRD, design brief, technical specification, test plan, PR description, retrospective, and release notes. The research-report template links to the Phase 4 canonical file rather than duplicating it.
- Added `docs/EXTENDING.md` with exact commands and five-minute steps for agents, skills, playbooks, and platform adapters; updated README and skill indexes; added SemVer/CHANGELOG conventions.
- Added README pointers for missing root-level folders and normalized metadata in existing portable skills and playbooks. Existing paths were retained.
- Each newly added skill directory has a README pointer to its canonical `SKILL.md`; procedures remain single-source.
- Validation note: this environment exposes GitHub file APIs but no repository checkout/shell. The requested validator and unit-test commands have not yet run in a checkout; do not treat Phase 7 acceptance as fully verified until CI/local execution confirms them.

## Phase 6 changes

- Reviewed official Claude Code, Codex, Gemini CLI, GitHub Copilot, and Cursor documentation before editing; source URLs and access date (2026-10-28) are recorded in `docs/RESEARCH.md`.
- Added standard-library-only `scripts/sync_platforms.py` with deterministic generation and `--check` drift detection. Root `AGENTS.md` remains the only shared policy source; Codex consumes it natively and intentionally has no duplicate generated file.
- Converted Claude Code, Gemini CLI, Copilot, and Cursor entry points to generated thin references with an AGENTS SHA-256 marker. Cursor YAML frontmatter remains at file start.
- Added six unit tests for generation, synchronized check, missing/manual-edited adapters, stale policy digest, missing canonical policy, and CLI exit codes; all six passed in an isolated local harness. Added `--check` to GitHub Actions.
- Added `docs/ADAPTERS.md`, `docs/GENERIC_ADAPTER.md`, direct-API requirements in `docs/PROVIDER_ADAPTER.md`, updated `docs/PLATFORM_MATRIX.md`, `docs/MULTI_PROVIDER.md`, and README indexes.
- Full repository validator and complete test suite could not be executed against a checkout: `git clone` failed because github.com DNS resolution is unavailable in this environment. No full-suite pass is claimed; GitHub Actions should verify the pushed commits.

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

Phase 6 only. Do not begin Phase 7 or any later phase in this change.


## Phase 9 changes

- Expanded config/agent-team.example.yaml to schema version 2 with fast/balanced/deep-reasoning tiers, per-role model IDs, fallback order, input/output token caps, per-task cost caps, iteration limits, and timeouts. Cross-provider fallback remains disabled by default; exact model-ID pinning and moving-alias risks are documented.
- Added docs/TOOLS_AND_MCP.md: role capability requirements, missing-tool/degraded-mode behavior, untrusted MCP/tool output rules, and minimal Claude Code, Codex, Gemini CLI, and VS Code/Copilot examples linked to official docs checked 2026-10-28.
- Added a privacy-minimal run-log template and docs/RUN_LOG.md, plus stdlib-only scripts/validate_run_log.py and unit tests for schema, timestamps, secret/PII patterns, and CLI failure.
- Updated repository/docs/config/scripts/tests indexes and extended static validation for routing invariants and index coverage.
- Tightened `scripts/validate_repo.py` routing checks to require per-role model IDs and validate tier names, fallback tier names/order, positive token/iteration/timeout limits, and positive cost budgets; added regression tests for invalid fallback tiers and primary-tier self-fallback.
- Added Tools/MCP and Run Logs/Observability to the root README index. Official platform configuration references were checked on 2026-10-28: [Claude Code MCP](https://docs.anthropic.com/en/docs/claude-code/mcp), [Codex MCP](https://developers.openai.com/codex/mcp/), [Gemini CLI MCP](https://geminicli.com/docs/tools/mcp-server/), [VS Code MCP configuration](https://code.visualstudio.com/docs/agents/reference/mcp-configuration), and [GitHub Copilot MCP](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/extend-copilot-with-tools-and-context/extend-copilot-chat-with-mcp). Examples are documentation-based, not live-tested integrations.
- Verification limitation: this GitHub-file-only interface has no repository checkout or shell, so `python scripts/validate_repo.py` and `python -m unittest discover -s tests -v` cannot be run locally here. Check the CI status for the final commit before treating validation as passed. Phase 10 was not started.


## Phase 11 changes
- Added UI/UX, branding, illustration and content standards; deliverable format guide; brand-kit, handoff and image-brief templates.
- Linked standards from indexes and relevant roles/pipelines. Sources accessed 2026-10-28; revalidation target 2027-01-28.
- Validator and unit tests could not run in this API-only session without a checkout/shell. Check CI for the final commit; no pass is claimed.

## Scope boundary
Phase 11 only. Do not begin Phase 12 or Phase 13.
