# Submodule Mode Audit

**Branch:** feat/submodule-mode  
**Audit date:** 2026-10-28  
**Scope:** Read-only inventory before implementation. No installer, bootstrap, validator, adapter, or test code has been changed in this step.

## Executive summary

Agent-Team currently behaves as a standalone repository, not as a framework mounted inside another repository. Its canonical instructions and native adapter files use paths that make sense when Agent-Team itself is the project root. The validator, sync script, shell preflight, tests, documentation links, and curated memory also treat the checked-out Agent-Team directory as the working project. Simply adding this repository as a Git submodule would leave AI tools reading the host repository's root files without a reliable pointer to the nested framework, while running existing scripts would validate or write within the submodule itself.

The design must keep three locations distinct:

- **Host root:** the user's project, its own instructions, source code, tests, and project-specific configuration.
- **Framework root:** the pinned Agent-Team submodule (default .agent-team/), treated as read-only during installation and host work.
- **Host-local state:** .agent-team-local/ in the host root, never inside the submodule.

The installer should generate only managed blocks in host-owned bootstrap files, never replace unrelated user content, and never use symlinks.

## Inventory: assumptions and impact

| Area / file | Current root assumption | Submodule-mode impact / required treatment |
|---|---|---|
| AGENTS.md | Describes policy for the repository currently open; links and framework paths are relative to the Agent-Team root. | Host AI tools need a root-level bootstrap that explicitly instructs them to read <submodule-path>/AGENTS.md first. Preserve host project-specific rules and state that those win for project-specific decisions. |
| CLAUDE.md, GEMINI.md | Generated adapters link to AGENTS.md in the same root. | Host copies must resolve to the configured submodule path, not a host-root AGENTS.md that may belong to the user. Preserve existing host content outside the managed block. |
| .cursor/rules/agent-team.mdc | Says to follow repository-root AGENTS.md; framework paths are not configurable. | Host bootstrap must point at the submodule's canonical policy. Keep Cursor front matter valid and distinguish workflow policy from host-specific rules. |
| .github/copilot-instructions.md | Relative link ../AGENTS.md assumes the adapter and canonical policy share Agent-Team's root layout. | Generate a host-root compatible managed block pointing to the configured submodule. Existing instructions must remain intact. |
| .claude/CLAUDE.md | Uses ../AGENTS.md, ../agents/, and ../docs/WORKFLOW.md based on its current in-repository location. | If a host already has this path, merge only the managed block. Every framework reference in that block must resolve through the submodule path. |
| .claude/skills/ and .agents/skills/ | Existing skills are framework-owned files at native runtime paths, not host-aware stubs. | Provide thin stubs only for supported platforms, linking to the pinned submodule skill/workflow source. Avoid copying the whole skill tree or overwriting user skills. |
| scripts/sync_platforms.py | ROOT = Path(__file__).resolve().parents[1]; generated targets are fixed relative paths inside the repository. sync() writes complete files and --check compares complete files against generated content. | Existing sync behavior is for maintaining Agent-Team's own adapters, not a safe host installer. Keep framework sync separate from host bootstrap generation. Extend --check to detect drift in framework bootstrap templates. |
| scripts/validate_repo.py | ROOT is fixed to the parent repository. REQUIRED, index checks, role-contract checks, link checks, and config checks expect the complete Agent-Team tree. Recursive scans run beneath that root; local links resolve against that root and links escaping it are rejected. | Continue validating the framework tree when invoked in the submodule. Do not mistake host-root files or host-local state for framework files. Installer validation should separately check the host/submodule relationship and managed blocks. |
| scripts/validate_run_log.py | Accepts one explicit JSON path; the schema is generic, but documentation and examples assume paths inside this repository. | Host run logs must live under host .agent-team-local/runs/. The installer must not write operational logs into the framework. |
| tests/test_validate_repo.py | Imports the validator by resolving scripts/validate_repo.py from the test file; several tests assert against global validator.ROOT and the checked-out repository's real files. Temporary fixtures mimic framework paths. | Add installer tests using a separate temporary host and submodule directory. Keep framework-validator tests distinct from host integration tests. |
| tests/test_validate_run_log.py | Resolves scripts/validate_run_log.py and templates/run-log-template.json relative to the test file's repository root. | Keep the fixture framework-owned; document that host-generated run logs are separate and stored in host-local state. |
| tests/test_sync_platforms.py | Imports the sync script from the framework tree and checks generated adapters in a temporary root containing a fake AGENTS.md. | Add bootstrap-template drift coverage without changing the distinction between framework adapter sync and host installation. |
| run.sh | Computes its own directory, then cd's to it and checks fixed framework paths including memory/MEMORY.md; runs framework validation/tests there. | Running it from a host should not silently validate the host as if it were Agent-Team. Document it as framework self-check; host users run installer and --check instead. |
| memory/MEMORY.md | Curated memory is stored in the Agent-Team repository and links to its canonical docs. | This is framework-maintainer memory, not user-project memory. Host-specific memory belongs under .agent-team-local/memory/; never write it into the pinned submodule. |
| docs/RUN_LOG.md and templates/run-log-template.json | Describe run logs but do not define a host-state location contract. | Document host-local .agent-team-local/runs/ and keep the framework template read-only. |
| docs/WORKFLOW.md, role contracts, skills, research docs, quality gates, and other framework Markdown | Relative links (for example ../memory/MEMORY.md, ../agents/, ../docs/) assume a coherent Agent-Team checkout. | Bootstrap must instruct agents to resolve framework assets relative to the configured submodule root. Do not rewrite every canonical framework link to be host-root relative. |
| config/agent-team.example.yaml | Example configuration is stored under framework config/; it is a template, not a host configuration loader. | Bootstrap should reference <submodule-path>/config/... and not imply the example is automatically applied to the host runtime. |
| templates/, research/, agents/, skills/, playbooks/, workflows/, evals/, examples/ | These directories are framework assets. Links among them assume their current repository-relative locations. | Treat as immutable sources in the pinned submodule. Runtime evidence, decisions, and memory generated for a host belong under .agent-team-local/. |
| examples/demo-project/run-log.json and demo evidence/decision files | Checked-in sample artifacts for the framework demo, not runtime host state. | Keep them as examples and distinguish them from host-local operational records. |
| .github/workflows/validate.yml | Checks out the framework repository with default checkout behavior, then runs framework validation, adapter sync, and tests. Checkout does not request recursive submodules. | Framework CI should keep validating Agent-Team itself. Add installer tests and, where practical, a local-submodule integration test that does not require external network access. Host-project CI consuming Agent-Team must check out submodules recursively. |
| README.md, docs/OPERATIONS.md, docs/ADAPTERS.md, docs/PLATFORM_MATRIX.md, docs/VERSIONING.md, MIGRATION.md | Instructions are written primarily for cloning/running Agent-Team as the working repository; the platform matrix describes native entry-point paths in this repository. | Add a submodule quick start and detailed guide. Clarify pinned revision, host-owned local state, and platform testing evidence. |
| Paths derived from __file__ in scripts and tests | Correct for framework-owned scripts/tests, but insufficient to locate a separate host from an arbitrary working directory. | Installer must accept explicit/default host target, resolve the configured submodule path inside that target, validate paths, and never infer that framework root is host root. |
| Git submodule checkout state | Not covered by current installer/docs. | A submodule checkout is a gitlink pinned by the host repository; the worktree may appear empty until initialized. Updates are explicit, reviewed, and committed by the host as a gitlink change. Detached HEAD is normal for a pinned submodule. |

## Existing behavior confirmed by source inspection

- The framework has one canonical shared policy in AGENTS.md; native adapter files are generated by scripts/sync_platforms.py.
- Current generated adapters contain hard-coded root-relative references and are written as complete files by the sync script.
- scripts/validate_repo.py is a framework-tree validator with required-file, role, front-matter, index, link, placeholder, secret, and config checks. Its ROOT is not configurable via the CLI today.
- The unit-test suite uses standard-library unittest, temporary directories, and unittest.mock; no third-party test dependency is needed for installer tests.
- The workflow currently runs on pushes to main, pull requests, and manual dispatch. Its checkout step does not request recursive submodules.
- docs/PLATFORM_MATRIX.md explicitly states no exact runtime/model/client combination was tested during the documented upgrade. Submodule bootstrap entries must preserve that evidence standard.

## Design consequences for implementation

1. Keep framework self-maintenance (sync_platforms.py, validator, canonical roles, framework memory) scoped to the submodule root.
2. Make host integration a separate installer API: target root, configurable submodule path, platform selection, dry run, check, uninstall, clear diagnostics, and proper exit codes.
3. Generate host-root files from dedicated templates/host-bootstrap/ templates. Each generated block must use stable <!-- agent-team:begin --> and <!-- agent-team:end --> delimiters and resolve framework links from the host root.
4. For an existing host file, change only the managed block if both delimiters are present and well-formed. If a file exists without a managed block, preserve it and append a clearly delimited managed block only when safe; never replace the whole file. Fail clearly on malformed or duplicate markers.
5. Treat .agent-team-local/ as host-owned writable state with documented memory/, evidence/, runs/, and decisions/ directories. Installer and uninstall must not delete user data.
6. Avoid symlinks and third-party packages; use standard-library file and path operations compatible with Android Termux.
7. Ensure sync_platforms.py --check checks canonical host-bootstrap templates for drift as well as existing generated framework adapters.
8. Keep framework validation and host validation separate. Tests should cover idempotency, existing-file preservation, dry-run, drift, safe uninstall, bad paths, missing submodule, malformed markers, and platform selection.
9. A real local Git submodule test should create a temporary host repository, add the local Agent-Team repository with git -c protocol.file.allow=always submodule add, run the installer and --check, and capture exact command output. Source/API inspection alone is insufficient evidence.
10. Update README, detailed guide, upgrade progress, versioning, migration, indexes, and CI only after this audit is reviewed and implementation begins.

## Verification boundary

This audit is based on source files fetched from the feat/submodule-mode branch. A local git clone https://github.com/squiraldot/Agent-Team.git attempt failed because this execution environment could not resolve github.com. No repository code has been executed locally in this step, and no installer, submodule integration, or AI-platform behavior is claimed as tested.

## Audit outcome

The highest-risk assumption is the collision between the host project's own root-level instructions and Agent-Team's existing generated root adapters. The implementation should solve that with additive managed blocks and explicit submodule-relative links, while preserving the pinned framework tree and keeping all mutable host state outside it.
