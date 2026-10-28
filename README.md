# Agent-Team

**A model-agnostic, multi-runtime AI agent team** for planning, research, drafting/implementation, review, and routing.

Agent-Team separates portable team policy from runtime-specific adapters. The same role definitions and workflows can be used with many model families, while each coding agent or API integration uses its own native configuration.

## Important compatibility note

No project can guarantee compatibility with literally every model and every historical/future version. Providers and runtimes differ in model IDs, tool calling, context limits, vision, web search, parallel agents, approvals, and API behavior. Agent-Team aims for portable instructions and adapter-based integration; a combination is **verified** only after it is tested.

## Quick start

1. Clone:
   ```bash
   git clone https://github.com/squiraldot/Agent-Team.git
   cd Agent-Team
   ```
2. Read [AGENTS.md](AGENTS.md), the provider-neutral shared policy.
3. Choose the native adapter for your coding agent:
   - Claude Code: [CLAUDE.md](CLAUDE.md), `.claude/agents/`, `.claude/skills/`, `.claude/settings.json`
   - OpenAI Codex / compatible agents: `AGENTS.md`
   - Gemini CLI: [GEMINI.md](GEMINI.md)
   - GitHub Copilot: [.github/copilot-instructions.md](.github/copilot-instructions.md)
   - Cursor: [.cursor/rules/agent-team.mdc](.cursor/rules/agent-team.mdc)
   - Other runtimes: import `AGENTS.md` through their documented instructions mechanism.
4. Review runtime settings and hook scripts before enabling them.
5. Run structural preflight:
   ```bash
   bash run.sh
   ```
6. Verify the exact runtime version, provider, model ID, tool permissions, and approval behavior before using on important work.

## Providers and model families

The shared policy is intended for hosted or local models from OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek, Qwen, and other providers, including OpenAI-compatible APIs and local runtimes such as Ollama and LM Studio—when the selected runtime supports them.

No provider or model is automatically configured just because it appears in this list. Supply credentials securely, use a supported runtime/adapter, and verify the exact model ID and required capabilities. Do not place API keys in repository files.

## Team roles

| Role | Responsibility |
|---|---|
| Planner | Requirements, assumptions, dependencies, risks, acceptance criteria |
| Researcher | Current evidence, sources, dates, conflicts, uncertainty |
| Builder | Draft/implementation and focused checks |
| Reviewer | Independent review of correctness, safety, completeness |
| Router | Select next step: plan, research, build, review, clarify, or stop |

For simple tasks, skip unnecessary roles. These are portable responsibilities; native agent execution depends on the runtime.

## Model routing configuration

[config/agent-team.example.yaml](config/agent-team.example.yaml) is a provider-neutral **template**, not a universal CLI config. It includes per-role model overrides, capability-first routing, optional fallback, privacy controls, and approval requirements. A runtime adapter must translate it into the chosen provider's API/configuration.

- Use runtime defaults for easy setup.
- Pin an exact model ID when reproducibility matters.
- Treat `latest` as a moving alias if the provider supports it.
- Cross-provider fallback is disabled by default because it may transmit code/context to another vendor.
- Unsupported features should be reported clearly, never silently simulated.

## Repository map

```text
Agent-Team/
├── AGENTS.md                    # shared, provider-neutral policy
├── CLAUDE.md                    # Claude Code entry point
├── GEMINI.md                    # Gemini CLI entry point
├── .github/copilot-instructions.md
├── .cursor/rules/agent-team.mdc
├── .claude/
│   ├── agents/                  # Claude-native subagent definitions
│   ├── skills/                  # Claude-native skill wrappers
│   ├── hooks/                   # Claude-specific lifecycle hooks
│   └── settings.json
├── agents/                      # portable role prompt references
├── playbooks/                   # content, product, growth
├── skills/                      # reusable procedures
├── config/agent-team.example.yaml
├── memory/MEMORY.md
├── docs/                        # architecture, operations, security, compatibility
└── run.sh                       # structural/syntax preflight
```

## Documentation

- [Multi-provider guide](docs/MULTI_PROVIDER.md)
- [Compatibility and version policy](docs/COMPATIBILITY.md)
- [Provider adapter contract](docs/PROVIDER_ADAPTER.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Security and privacy](docs/SECURITY.md)
- [Research sources](docs/RESEARCH.md)
- [Operations and troubleshooting](docs/OPERATIONS.md)
- [Architecture decisions](docs/DECISIONS.md)
- [Playbooks](playbooks/README.md)
- [Skills](skills/README.md)
- [Project memory](memory/MEMORY.md)

## Research basis

The multi-runtime approach is based on documented differences between native agent formats. See [Anthropic's Claude Code guidance](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more), [OpenAI Codex documentation](https://learn.chatgpt.com/docs/cli/reference), [Google Gemini CLI documentation](https://ai.google.dev/gemini-api/docs/cli), [GitHub Copilot custom agents](https://docs.github.com/en/copilot/concepts/customizations/custom-agents), and [VS Code agent customization guidance](https://code.visualstudio.com/docs/agent-customization/custom-instructions). The linked documentation may evolve; verify it before upgrades.

## Security

Hooks and prompt instructions are not a security sandbox. Review scripts, use least privilege, keep secrets out of Git, and require human approval for publishing, messaging, deployments, purchases, deletions, and production changes. Read [Security](docs/SECURITY.md).

## License

MIT; see [LICENSE](LICENSE).
