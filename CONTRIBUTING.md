# Contributing to Agent-Team

Thank you for improving Agent-Team. The goal is portable, safe, evidence-based agent workflows—not a claim that every AI runtime behaves identically.

## Before opening a change

1. Read `AGENTS.md`, `docs/ARCHITECTURE.md`, `docs/SECURITY.md`, [IP and licensing](docs/IP_AND_LICENSING.md), [versioning](docs/VERSIONING.md), [migration](MIGRATION.md), and relevant compatibility documentation.
2. Resolve conflicting agent recommendations using [docs/CONFLICT_RESOLUTION.md](docs/CONFLICT_RESOLUTION.md); retain evidence for both positions and record consequential outcomes in `docs/DECISIONS.md`. Escalate unresolved material/high-risk decisions to a human.
3. Check dependency/asset licences, attribution, and applicable AI-content disclosure rules before distributing work; see `docs/IP_AND_LICENSING.md`.
4. For changes to role/skill contracts or config, follow SemVer, deprecation, and adapter-compatibility rules in `docs/VERSIONING.md` and migration steps in `MIGRATION.md`.
2. Search for an existing pattern before introducing a new file format or dependency.
3. Keep shared policy provider-neutral; place runtime-specific syntax in the corresponding native directory.
4. For platform-specific claims, link the official source and note version limitations.
5. For behavior changes, add tests. For docs-only changes, check internal links and ensure claims match the implementation.

## Validation

Run:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
bash -n run.sh
for file in .claude/hooks/*.sh; do bash -n "$file"; done
python -m json.tool .claude/settings.json >/dev/null
```

These checks are static and do not validate real provider behavior. Native runtime smoke tests must be reported separately.

## Pull requests

A good PR explains:
- the problem and intended outcome;
- key design decisions and alternatives;
- changed paths and behavior;
- tests run with exact results;
- security/privacy implications;
- compatibility impact and documentation updates;
- limitations and follow-up work.

Do not include API keys, private customer data, full sensitive traces, or unreviewed generated content. Avoid claiming production readiness without deployment-specific evidence.
