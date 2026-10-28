# Agent-Team

**A model-agnostic, multi-runtime AI agent team** for planning, research, drafting/implementation, review, and routing.

Agent-Team separates portable team policy from runtime-specific adapters. It aims to be a maintainable framework starter with role contracts, security practices, quality gates, evaluation cases, and platform-specific configuration examples.

## Important compatibility note

No project can guarantee compatibility with literally every model and every historical/future version. Providers and runtimes differ in model IDs, tool calling, context limits, web access, parallel agents, approvals, and API behavior. Agent-Team provides portable instructions and native examples; a combination is **verified** only after testing the exact runtime, version, model ID, client surface, and permissions.

## Quick start

```bash
git clone https://github.com/squiraldot/Agent-Team.git
cd Agent-Team
python scripts/validate_repo.py
python scripts/sync_platforms.py --check
python -m unittest discover -s tests -v
bash run.sh
```

Then:
1. Read [AGENTS.md](AGENTS.md), the provider-neutral source of shared policy.
2. Choose the native integration for your runtime.
3. Review all settings and hook scripts before enabling them.
4. Verify the exact runtime version, provider, model ID, tools, and approval behavior before important work.

## Platform integrations

- **Claude Code:** [CLAUDE.md](CLAUDE.md), `.claude/agents/`, `.claude/skills/`, `.claude/settings.json`
- **OpenAI Codex:** [AGENTS.md](AGENTS.md), `.agents/skills/`
- **Gemini CLI:** [GEMINI.md](GEMINI.md); confirm support for each native feature in your installed version
- **GitHub Copilot:** [.github/copilot-instructions.md](.github/copilot-instructions.md), [.github/agents/](.github/agents/)
- **Cursor:** [.cursor/rules/agent-team.mdc](.cursor/rules/agent-team.mdc)
- **Other runtimes / direct provider APIs:** import the shared policy through their documented mechanism; API execution requires a real adapter.

## Team roles

| Role | Responsibility |
|---|---|
| Planner | Scope, assumptions, dependencies, risks, acceptance criteria, validation plan |
| Researcher | Primary-source evidence, dates, conflicts, uncertainty, citations |
| Builder | Scoped implementation, tests, and honest verification report |
| Reviewer | Independent correctness, security, privacy, regression, and completeness review |
| Router | Choose plan, research, build, review, clarify, or stop based on task complexity and risk |

Domain specialists now cover [web development](agents/web-developer/role.md), [Android](agents/android-developer/role.md), [software engineering](agents/software-developer/role.md), [plugins/modules](agents/plugin-module-developer/role.md), [UI/UX](agents/ui-ux-designer/role.md), [graphic design/branding](agents/graphic-designer-branding/role.md), [illustration/visual art](agents/illustrator-visual-artist/role.md), [content creation](agents/content-creator/role.md), and [automation/AI tools](agents/automation-ai-tools-specialist/role.md). See the complete [portable role index](agents/README.md) for scope and handoff contracts.

For simple tasks, skip unnecessary roles. Role files are portable responsibilities; a Markdown prompt does not itself create an executing subagent.

## Model routing configuration

[config/agent-team.example.yaml](config/agent-team.example.yaml) is a provider-neutral **template**, not a universal CLI config. A runtime adapter must validate and translate it into a chosen provider's API/configuration.

- Use runtime defaults for easy setup; pin exact model IDs when reproducibility matters.
- Treat moving aliases such as `latest` as provider-dependent.
- Cross-provider fallback is disabled by default because it may transfer code/context to another vendor.
- Unsupported capabilities must be reported, not silently simulated.
- Never put API keys or credentials in this repository.

## Production-minded controls

- Quality gates: [docs/QUALITY_GATES.md](docs/QUALITY_GATES.md)
- Evaluation scenarios: [evals/README.md](evals/README.md)
- Tool routing and capabilities: [docs/TOOLS_AND_MCP.md](docs/TOOLS_AND_MCP.md)
- Run-log schema and validation: [docs/RUN_LOG.md](docs/RUN_LOG.md), [scripts/validate_run_log.py](scripts/validate_run_log.py), and [templates/run-log-template.json](templates/run-log-template.json)

- Shared task/handoff contract: [docs/AGENT_PROTOCOL.md](docs/AGENT_PROTOCOL.md)
- Production readiness and release gates: [docs/PRODUCTION_READINESS.md](docs/PRODUCTION_READINESS.md)
- Security and privacy model: [docs/SECURITY.md](docs/SECURITY.md) and [SECURITY.md](SECURITY.md)
- Evaluation and regression scenarios: [docs/EVALUATION.md](docs/EVALUATION.md)
- Platform capability matrix: [docs/PLATFORM_MATRIX.md](docs/PLATFORM_MATRIX.md)
- Incident response: [docs/INCIDENT_RESPONSE.md](docs/INCIDENT_RESPONSE.md)
- Contributor workflow: [CONTRIBUTING.md](CONTRIBUTING.md)
- Automated static validation: [scripts/validate_repo.py](scripts/validate_repo.py) and [GitHub Actions workflow](.github/workflows/validate.yml)

## Repository map

```text
Agent-Team/
├── AGENTS.md / CLAUDE.md / GEMINI.md
├── .agents/skills/              # Codex-compatible reusable skills
├── .claude/agents/              # Claude-native specialist definitions
├── .claude/skills/              # Claude-native skill wrappers
├── .claude/hooks/               # Claude-specific lifecycle hooks
├── .github/agents/              # Copilot custom-agent examples
├── .github/workflows/           # CI validation
├── .cursor/rules/               # Cursor rules
├── agents/                      # portable core and domain role contracts
├── playbooks/                   # content, product, growth
├── skills/                      # reusable workflow docs
├── templates/                   # PRD, design, engineering, and release templates
├── CHANGELOG.md                 # versioned project changes
├── research/                    # tiered sources, protocol, logs, templates
├── config/                      # provider-neutral example config
├── scripts/ and tests/           # validator, adapter sync, and unit tests
├── docs/                        # architecture, research, security, quality gates, operations
├── examples/demo-project/       # research-to-handoff landing-page pipeline proof
├── evals/                       # role-specific scenario specifications
├── workflows/                   # eight domain-specific delivery pipelines
└── memory/MEMORY.md              # curated project memory, no secrets
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Multi-provider guide](docs/MULTI_PROVIDER.md)
- [Platform capability matrix](docs/PLATFORM_MATRIX.md)
- [Compatibility and version policy](docs/COMPATIBILITY.md)
- [Provider adapter contract](docs/PROVIDER_ADAPTER.md)
- [Platform adapter index](docs/ADAPTERS.md)
- [Generic runtime adapter guide](docs/GENERIC_ADAPTER.md)
- [Agent handoff protocol](docs/AGENT_PROTOCOL.md)
- [Professional workflow and stage contracts](docs/WORKFLOW.md)
- [Workflow pipeline catalog](workflows/README.md)
- [Portable agent roles and domain specialists](agents/README.md)
- [Development standards](docs/standards/README.md): [web](docs/standards/web.md), [Android](docs/standards/android.md), [plugins/modules](docs/standards/plugins-modules.md), and [software engineering](docs/standards/software.md)
- [Production readiness](docs/PRODUCTION_READINESS.md)
- [Security and privacy](docs/SECURITY.md)
- [Evaluation strategy](docs/EVALUATION.md)
- [Tool capabilities, MCP configuration, and degraded modes](docs/TOOLS_AND_MCP.md)
- [Run logs and observability](docs/RUN_LOG.md)
- [Research notes and sources](docs/RESEARCH.md)
- [Research engine protocol and source registry](research/README.md)
- [Community Pulse skill](skills/community-pulse/README.md)
- [Operations and troubleshooting](docs/OPERATIONS.md)
- [Incident response](docs/INCIDENT_RESPONSE.md)
- [Release checklist](docs/RELEASE_CHECKLIST.md)
- [Contributing](CONTRIBUTING.md)
- [Architecture decisions](docs/DECISIONS.md)
- [Upgrade brief](docs/UPGRADE_BRIEF.md)
- [Upgrade audit and file-by-file plan](docs/UPGRADE_AUDIT.md)
- [Upgrade progress and open issues](docs/UPGRADE_PROGRESS.md)
- [Final upgrade report and global acceptance audit](docs/UPGRADE_REPORT.md)
- [End-to-end landing-page demo](examples/demo-project/README.md)
- [Playbooks](playbooks/README.md)
- [Skills](skills/README.md)
- [Templates](templates/README.md)
- [Five-minute extension guide](docs/EXTENDING.md)
- [Changelog and semantic versioning](CHANGELOG.md)
- [Project memory](memory/MEMORY.md)

## Research basis

The design reflects documented differences between native agent formats. Start with [OpenAI Codex customization](https://learn.chatgpt.com/docs/customization/overview), [Anthropic Claude Code guidance](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more), [Google Gemini CLI docs](https://github.com/google-gemini/gemini-cli/blob/main/docs/index.md), [GitHub Copilot custom instructions](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions), and [VS Code agent customization](https://code.visualstudio.com/docs/agent-customization/custom-instructions). Open-source design references include [LangGraph](https://github.com/langchain-ai/langgraph), [CrewAI](https://github.com/crewAIInc/crewAI), [OpenHands](https://github.com/All-Hands-AI/OpenHands), and [SWE-agent](https://github.com/SWE-agent/SWE-agent). See [research notes](docs/RESEARCH.md) for limitations and revalidation steps.

## Security

Hooks and prompt instructions are not a security sandbox. Review scripts, use least privilege, keep secrets out of Git, and require human approval for publishing, messaging, deployments, purchases, deletions, and production changes. Read [Security](docs/SECURITY.md).

## License

MIT; see [LICENSE](LICENSE).


## Governance and design deliverables
- [UI/UX standard](docs/standards/ui-ux.md)
- [Graphic design and branding standard](docs/standards/graphic-branding.md)
- [Illustration standard](docs/standards/illustration.md)
- [Content creation standard](docs/standards/content.md)
- [Handoff specification](templates/handoff-spec.md)
- [Image brief template](templates/image-brief.md)
- [Brand-kit template](templates/brand-kit/README.md)
- [Conflict resolution](docs/CONFLICT_RESOLUTION.md)
- [IP and licensing](docs/IP_AND_LICENSING.md)
- [Versioning policy](docs/VERSIONING.md)
- [Migration guide](MIGRATION.md)

## Design, content, and deliverables
- [Standards](docs/standards/README.md)
- [Deliverable formats](docs/DELIVERABLE_FORMATS.md)
- [Workflow pipelines](workflows/README.md)
- [Templates](templates/README.md)
