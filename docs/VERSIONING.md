# Versioning Policy

Use Semantic Versioning `MAJOR.MINOR.PATCH` for published role contracts, skills, and configuration schemas/templates. Use valid prerelease identifiers (e.g. `1.2.0-rc.1`) for experimental releases. Git commit hashes do not replace declared contract versions.

## Version meanings
- **MAJOR:** incompatible input/output contract; removed/renamed required field; safety/approval change; changed default with behavioral impact; migration required.
- **MINOR:** backward-compatible capability, optional field, or additive config/template option.
- **PATCH:** backward-compatible clarification, typo/link fix, or correction not changing contract meaning.
- **0.y.z:** pre-stable; explicitly document compatibility expectations and breaking changes.

## Roles, skills, and config
- Version canonical portable role/skill contracts first; adapters stay thin and reference the canonical policy.
- Contract changes to permissions, escalation, required evidence, or output schema are behavior changes even when stored in Markdown.
- Version config schemas separately from example values. Reject invalid safety-critical values instead of silently changing their meaning. Additive optional keys are MINOR only when old consumers safely ignore them; changed defaults, required keys, fallback/privacy semantics, or interpretation are MAJOR.
- Keep secrets out of examples. Add schema validation and regression tests for material changes.

## Deprecation process
1. Identify replacement and impact; search references, adapters, and consumers.
2. Mark the old item **deprecated** and state replacement, first deprecated version/date, compatibility path, and removal window if approved.
3. Keep shims/warnings where feasible. Never invent a removal date; say **not scheduled** if none is approved.
4. Add migration steps and tests for old/new behavior.
5. Remove after the announced window in a MAJOR release, except urgent security/legal cases with rationale and notice.
6. Update indexes, changelog, migration guide, adapters, tests, and decision record.

## Adapter backward compatibility
- `AGENTS.md` and canonical contracts are authoritative; adapters must not contradict them.
- Preserve supported inputs/outputs within a MAJOR version or document a shim and deprecation window.
- Report unsupported runtime features; never silently simulate or drop behavior affecting safety/correctness.
- Gate runtime-specific syntax/features on exact version evidence; do not claim universal compatibility.
- For canonical changes, check every adapter, config example, index, and eval. Document limitations if a runtime cannot express a rule; never silently weaken policy.
- Record runtime/model identifiers, test date/results, permissions, and limitations. Static checks are not runtime verification.

## Release checklist
- [ ] Contract/schema version and compatibility impact reviewed.
- [ ] Breaking changes and migration steps documented.
- [ ] Deprecations identify replacement and removal status/window.
- [ ] Adapters and references checked for drift.
- [ ] Validator, tests, relevant evals and claimed runtime tests recorded honestly.
- [ ] Changelog, indexes, `MIGRATION.md`, and `docs/DECISIONS.md` updated as applicable.
