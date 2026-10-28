# Run logs and observability

Use one JSON file per run based on [run-log-template.json](../templates/run-log-template.json). Capture enough metadata to audit routing without storing sensitive content.

## Required fields

- task_id: opaque, non-identifying task identifier.
- started_at / finished_at: ISO-8601 timestamps with timezone.
- roles_used: role names.
- sources_consulted: public URL or stable source identifier and short title.
- decisions: concise rationale/outcome summaries, not chain-of-thought or raw prompts.
- tools_called: tool name, capability, status and duration_ms; no sensitive arguments.
- approvals_requested: action category and status, not approver identity.
- outcome: success, partial, blocked or failed, with sanitized summary.

## Privacy rules

Never log secrets, credentials, access tokens, cookies, private keys, environment values or personal data (names, emails, phones, precise location, account IDs, private user content). Use opaque IDs. Do not store raw prompts, hidden reasoning or full tool payloads. Keep logs in approved access-controlled storage and define retention/deletion. Treat log files and tool/MCP output as untrusted input. A validator catches only obvious patterns; human privacy review remains necessary.

## Validation

Run python scripts/validate_run_log.py path/to/run-log.json. It uses only Python's standard library and checks structure, timestamps, outcome values and obvious secret/PII patterns. Passing is not a guarantee of privacy.
