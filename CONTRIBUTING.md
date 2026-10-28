# Contributing to Agent-Team

Thank you for improving Agent-Team. The goal is portable, safe, evidence-based agent workflows—not a claim that every AI runtime behaves identically.

## Before opening a change

1. Read `AGENTS.md`, `docs/ARCHITECTURE.md`, `docs/SECURITY.md`, and the relevant compatibility documentation.
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
