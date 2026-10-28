# Operations Guide

## Scope

This guide covers local setup and validation for the repository's templates. It does not configure every provider automatically or deploy a hosted agent service.

## Prerequisites

- Git
- Bash
- Python 3.10+ recommended for the static validator and unit tests
- The specific coding-agent runtime you plan to use, installed and authenticated separately
- `jq` is required when using the configured Claude Code Bash pre-tool hook; without it, the hook intentionally blocks Bash commands rather than silently skipping inspection. It is optional for other integrations.

## First-time setup

1. Clone the repository.
2. Read `README.md`, `AGENTS.md`, `docs/SECURITY.md`, and `docs/PLATFORM_MATRIX.md`.
3. Inspect all native settings and hook scripts before enabling them.
4. Choose the integration matching your runtime; do not copy Claude settings into another CLI.
5. Run the preflight and tests:

   ```bash
   python3 scripts/validate_repo.py
   python3 -m unittest discover -s tests -v
   bash run.sh
   ```

6. Open the project in the target runtime and verify that it actually discovers the expected instructions and native agent files.
7. Run a harmless read-only task, then a controlled file-edit task in a disposable branch.
8. Record the runtime version, provider, exact model ID, tool permissions, approval mode, and observed result before describing the combination as tested.

## Recommended task workflow

- Route trivial requests directly.
- Plan multi-file work and define acceptance criteria.
- Research current claims using primary sources.
- Implement within the agreed scope and add regression coverage for behavior changes.
- Review the actual diff independently.
- Run project-specific tests and inspect their output.
- Ask for approval before consequential external or irreversible actions.
- Hand off changed paths, evidence, test results, limitations, and next steps.

## Troubleshooting

### Agent or skill not discovered
- Confirm the exact native path and frontmatter expected by the installed runtime.
- Check that the runtime/client version supports the feature.
- Restart/reload only if the product docs require it.
- Do not infer support from the presence of a Markdown file.

### Hook does not run
- Check the runtime's current event names, payload schema, matcher syntax, executable path, and permissions.
- Inspect stderr and exit status.
- Test with a harmless fixture in a disposable repository.
- Never treat a hook as a sandbox.

### Preflight fails
- Read the first failing path or assertion.
- Confirm that all required files are committed.
- Run the Python validator and unit tests independently to isolate the cause.
- Do not bypass the check without documenting why.

### Provider/model unavailable
- Confirm account access, exact model ID, region/endpoint, quota, and current provider docs.
- Avoid silently substituting another model.
- If fallback is intentionally enabled, confirm data-transfer policy and log which provider was selected without logging sensitive prompt content.

### Tool loop or repeated failures
- Stop the run, preserve redacted diagnostics, and inspect the last successful step.
- Reduce task scope or tool permissions.
- Set finite retry, step, and cost limits in the actual runtime/adapter.
- Add a regression test when the root cause is understood.

## Routine maintenance

- Review upstream docs and runtime changelogs before major upgrades.
- Re-run static validation after config/hook changes.
- Run the evaluation matrix after prompt, model, routing, or tool changes.
- Review secrets scanning and dependency changes.
- Keep compatibility claims tied to recorded evidence.
- Curate memory: preserve stable decisions and useful references, not secrets or raw sensitive conversations.

## Operational reporting template

```text
Runtime/version:
Provider/model ID:
Client/surface:
Configuration revision:
Task and acceptance criteria:
Commands/checks run:
Observed results:
Files/artifacts changed:
Approval gates exercised:
Known gaps:
Follow-up owner:
```

## Limitations

Static validation confirms only the checks it executes. It does not prove correctness, provider compatibility, resistance to prompt injection, or security. Production readiness must be assessed for the concrete deployment; see `docs/PRODUCTION_READINESS.md`.
