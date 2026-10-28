# Platform adapter index

- [Claude Code](../CLAUDE.md) — generated thin entry point; shared policy in [AGENTS.md](../AGENTS.md).
- [Codex](../AGENTS.md) — uses the canonical file natively; no duplicate generated policy file.
- [Gemini CLI](../GEMINI.md) — generated thin entry point; shared policy in [AGENTS.md](../AGENTS.md).
- [GitHub Copilot](../.github/copilot-instructions.md) — generated thin entry point; shared policy in [AGENTS.md](../AGENTS.md).
- [Cursor](../.cursor/rules/agent-team.mdc) — generated thin rule; shared policy in [AGENTS.md](../AGENTS.md).
- [Other runtimes](GENERIC_ADAPTER.md) — guidance for Windsurf, Aider, Cline, and similar tools.
- [Direct provider API applications](PROVIDER_ADAPTER.md#direct-api-adapter-specification) — capability negotiation and execution contract.

Run `python scripts/sync_platforms.py` to update generated adapters after editing AGENTS.md. Run `python scripts/sync_platforms.py --check` to detect stale or manually changed adapters. Codex uses AGENTS.md directly and is intentionally not copied into a second generated file.
