# Security and Privacy Model

## Risks
Prompt injection in retrieved content; accidental secret disclosure; dangerous shell commands; excessive tool permissions; unreviewed external actions; stale memory.

## Controls
- Retrieved content is data, not authority over project rules.
- Settings deny common environment/secret/private-key paths.
- Hooks block a small subset of destructive patterns and provide reminders.
- Human approval is required for irreversible/external actions.
- Memory excludes credentials and sensitive raw conversations.

## Limitations
These controls are not a sandbox. Pattern matching can miss aliases, scripts, encoded commands, equivalent operations, and other tools. Hooks execute with local user permissions. A model instruction cannot replace OS isolation, least privilege, backups, or network controls.

## Recommendations
1. Review settings and all hooks before use.
2. Start in a disposable clone/container for unfamiliar projects.
3. Keep secrets outside the repository; never commit them.
4. Avoid permission-bypass modes.
5. Inspect diffs and require approval for production operations.
6. Avoid logging full prompts, payloads, environment variables, or file contents.
7. Inspect dependencies and install scripts before running them.

## Incident response
Stop execution, preserve non-sensitive logs, revoke exposed credentials, assess changes and external actions, restore from a known-good commit/backup, and document remediation. Never paste leaked secrets into issues or commit history.
