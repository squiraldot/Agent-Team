# Platform Capability Matrix

This matrix is a planning guide, not a guarantee of current support. Verify the exact product, client, version, and task surface against its official documentation before enabling a feature.

| Platform/runtime | Primary project guidance | Native specialist agents | Skills/workflows | Hooks/automation | MCP/tool connectivity | Key caveat |
|---|---|---|---|---|---|---|
| OpenAI Codex | `AGENTS.md` | Supported in applicable Codex surfaces | Skills | Depends on surface/config | Supported | CLI, IDE, hosted/API experiences can differ |
| Anthropic Claude Code | `CLAUDE.md` and rules | `.claude/agents/` | `.claude/skills/` | `.claude/settings.json` hooks | Supported | Hook schema/events are Claude-specific |
| Google Gemini CLI | `GEMINI.md` | Native agent definitions/subagents where enabled | Agent Skills/extensions | Native hooks/settings | Supported | Features may be experimental and version-specific |
| GitHub Copilot | `.github/copilot-instructions.md`, supported `AGENTS.md` | `.github/agents/*.agent.md` on supported surfaces | Skill support depends on surface | Client/workflow dependent | Supported in compatible clients | GitHub.com, IDE, CLI, and code review do not share identical behavior |
| Cursor | `.cursor/rules/*.mdc`, `AGENTS.md` | Feature/version dependent | Skills support depends on current client | Client-dependent | Supported | Verify rule format and agent features in current docs |
| Other IDE/CLI agents | Runtime-specific | Runtime-specific | Runtime-specific | Runtime-specific | Often via MCP or native tools | Import the shared policy manually and test it |
| Direct provider API | Adapter-owned instructions | Must be implemented in orchestration | Must be implemented | Must be implemented | Must be implemented | Prompts alone do not provide an agent loop or tools |
| Local inference (Ollama/LM Studio/etc.) | Host-specific | Host-specific | Host-specific | Host-specific | Host-specific | OpenAI-compatible API shape does not guarantee identical tool calling |

## Verification checklist per combination

Record:
- platform/runtime name and exact version;
- provider and exact model ID (not just a moving alias);
- client/surface (CLI, IDE, hosted app, API);
- instruction file actually discovered;
- whether subagent delegation is native and enabled;
- tool permissions and approval mode;
- MCP servers/tools and their scopes;
- tests run, results, date, and operator;
- known limitations and privacy/data residency implications.

## Compatibility labels

- **Documented:** official documentation describes the capability.
- **Configured:** repository contains the native configuration.
- **Smoke-tested:** a basic real task was executed on the exact runtime/model combination.
- **Evaluated:** a repeatable task and safety test set was run.
- **Production-approved:** the specific deployment passed its organization's operational and security review.

Never promote a combination to a higher label without evidence.
