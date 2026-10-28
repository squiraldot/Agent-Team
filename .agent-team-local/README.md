# Agent-Team host-local state

This directory belongs to the host project, not the Agent-Team submodule. Keep Agent-Team pinned and read-only. This scaffold intentionally stores no secrets or runtime history.

- memory/: curated, non-sensitive host-project decisions and durable lessons.
- evidence/: source notes and evidence logs, with dates and URLs.
- runs/: sanitized run logs; never include credentials, raw sensitive prompts, or personal data.
- decisions/: concise architecture/product decisions and approval records.

The installer creates missing directories but never overwrites this README or existing user data. Review retention and access permissions for generated records.