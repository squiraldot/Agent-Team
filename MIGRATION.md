# Migration Guide

This guide covers portable role/skill contracts, configuration schemas/examples, and runtime adapters. It does not imply every migration is tested on every runtime.

## Before migrating
1. Read [versioning](docs/VERSIONING.md), [conflict resolution](docs/CONFLICT_RESOLUTION.md), [platform matrix](docs/PLATFORM_MATRIX.md), and [release checklist](docs/RELEASE_CHECKLIST.md).
2. Record current Git revision, local changes, runtime/client version, provider/model ID, tools, permission mode, and customizations. Never record credentials.
3. Identify MAJOR changes, deprecated fields, changed defaults, security/privacy impact, and adapter limitations.
4. Safely back up user-owned configuration without copying secrets into issues or the repository.

## Procedure
1. Update canonical `AGENTS.md`, role/skill contracts, and config schema/examples from a known revision.
2. Apply documented field/default changes explicitly; do not blindly overwrite local customizations.
3. Update each runtime adapter to a compatible contract version; adapters remain thin and policy-consistent.
4. Run `python3 scripts/validate_repo.py`, `python3 -m unittest discover -s tests -v`, `python3 scripts/sync_platforms.py --check`, shell syntax checks, and JSON validation as applicable.
5. Run relevant eval scenarios and exact-runtime smoke tests for every compatibility claim. Static checks do not prove runtime support.
6. Inspect approval gates, permissions, fallback/data transfer, and unsupported tools.
7. Record exact results, skipped checks, limitations, rollback revision, and owner approval before rollout.

## Breaking changes and deprecations
Follow [docs/VERSIONING.md](docs/VERSIONING.md). Breaking changes require migration notes and release-note entries; preserve a compatibility shim where feasible. Deprecations name the replacement, first affected version/date, compatibility path, and removal window if approved. If migration is unsafe, ambiguous, or unvalidated, pause and escalate to the Orchestrator/human decision owner rather than guessing.

## Migration record
- From revision/version:
- To revision/version:
- Runtime/client, version, provider/model:
- Changed contracts/config fields:
- Steps applied and local customizations:
- Validation commands and exact results:
- Runtime/eval scenarios and results:
- Skipped checks / limitations:
- Rollback revision and procedure:
- Operator / approver / date:
