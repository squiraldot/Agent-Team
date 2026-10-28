# Extending Agent-Team

This guide is the five-minute path for adding a portable agent, skill, playbook, or platform adapter. Keep [AGENTS.md](../AGENTS.md) canonical; link to shared policy instead of copying it. See [role contracts](../agents/README.md), [skills](../skills/README.md), [playbooks](../playbooks/README.md), [workflows](../workflows/README.md), and [adapter sync](ADAPTERS.md).

## Before editing

```bash
git switch -c feat/add-kebab-case-item
python scripts/validate_repo.py
python scripts/sync_platforms.py --check
python -m unittest discover -s tests -v
```

Use lowercase kebab-case for new directory and file names. Use SemVer for maintained artifacts: MAJOR for incompatible contract changes, MINOR for backward-compatible capabilities, PATCH for compatible corrections. Every role, skill, and playbook starts with YAML front matter containing `name`, `description`, `version`, `owner`, and `status`. Update [CHANGELOG.md](../CHANGELOG.md) for user-visible changes.

## Add a new agent (about 5 minutes)

1. Copy `templates/_role-template/` to `agents/<kebab-case-name>/`.
2. Fill in `role.md`, `rules.md`, `tools.md`, `checklist.md`, `inputs-outputs.md`, examples, and evals. Put required front matter in the canonical role entry point.
3. State scope, trigger/non-trigger conditions, inputs/outputs, boundaries, failure/escalation, and completion criteria. Link shared research and handoff policy.
4. Add one row to `agents/README.md`; add runtime wrappers only when that runtime supports them, and keep them thin references.
5. Validate links and tests; add a changelog entry.

## Add a new skill (about 5 minutes)

1. Create `skills/<kebab-case-name>/SKILL.md` and include the five front-matter fields.
2. Add **Trigger conditions**, **Steps**, **Checklist**, and **Failure modes** sections. Make the steps actionable and the checklist verifiable.
3. Add a `README.md` in the skill directory that links to `SKILL.md`; keep the procedure in one canonical location.
4. Add the skill to `skills/README.md`. Link to research, role, and template references rather than copying their content.

## Add a new playbook (about 5 minutes)

1. Create `playbooks/<kebab-case-name>/README.md` or a kebab-case Markdown file within the relevant existing category.
2. Include the required front matter and document purpose, trigger, inputs, ordered steps, gates, failure/rollback, and outputs.
3. Reference canonical roles, skills, and [workflow stage contracts](WORKFLOW.md); do not reproduce their instructions.
4. Add a link to `playbooks/README.md` and a changelog entry.

## Add a platform (about 5 minutes)

1. Verify the platform's current official docs and note access date, exact client/runtime, version, and feature limits in [research notes](RESEARCH.md).
2. Create a minimal adapter that points to `AGENTS.md`; explicitly list unsupported features. Never claim runtime execution until tested on the exact version/model/permissions.
3. Update [platform matrix](PLATFORM_MATRIX.md) and [adapter index](ADAPTERS.md). Run `python scripts/sync_platforms.py --check`; use the sync script for generated adapters instead of hand-editing them.
4. Add a test or documented manual verification for the adapter behavior, and note limitations.

## Final checks and commit

```bash
python scripts/validate_repo.py
python scripts/sync_platforms.py --check
python -m unittest discover -s tests -v
git diff --check
git status --short
git add <specific-paths>
git commit -m "feat: add <kebab-case-item>"
```

If a check fails, fix the cause and rerun all checks. Do not report a check as passed unless the command actually ran. Link every new artifact from its owning index and update `CHANGELOG.md`. Do not start a later upgrade phase without explicit scope approval.
