# Release Checklist

Use this checklist when publishing a tagged release or describing a revision as production-ready for a specific deployment.

## Before release

- [ ] Scope and intended user-facing changes are documented.
- [ ] `AGENTS.md` remains the canonical policy and native adapters do not contradict it.
- [ ] All links, paths, examples, configuration keys, and supported feature claims are checked.
- [ ] Static validation passes: `python3 scripts/validate_repo.py`.
- [ ] Unit tests pass: `python3 -m unittest discover -s tests -v`.
- [ ] Shell syntax checks pass for `run.sh` and every hook.
- [ ] Claude settings JSON parses.
- [ ] Any behavior change has appropriate regression coverage.
- [ ] Security/privacy impact is reviewed; no credentials or sensitive test fixtures were introduced.
- [ ] Native runtime smoke tests are run for every platform being advertised as verified.
- [ ] Evaluation results are recorded for model/routing/prompt changes.
- [ ] Known gaps and skipped checks are explicit.
- [ ] Incident and rollback procedures are suitable for the target deployment.

## Compatibility record

For each claimed supported combination, record:
- runtime/client and exact version;
- provider and exact model ID;
- configuration revision and enabled tools;
- approval/permission mode;
- smoke/evaluation test identifiers and results;
- test date and operator;
- limitations and data-transfer implications.

## Release notes

Include:
- user-visible changes;
- breaking changes or migration steps;
- security-relevant changes;
- validation commands and actual outcomes;
- compatibility changes;
- known issues and workarounds.

## Rollback

For a documentation/config-only release, identify the previous known-good commit/tag and revert strategy. For a deployed adapter/service, also document version rollback, credential rotation, state migration recovery, and operator notification. Do not deploy or publish without explicit owner authorization.
