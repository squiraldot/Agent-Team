# Agent-Team

A practical, extensible Claude Code agent team for planning, research, drafting/implementation, review, and routing. The repository follows the structure in the reference diagram while placing agent and skill definitions in Claude Code's recognized `.claude/` locations so they can actually be discovered.

## What is included

| Component | Purpose |
|---|---|
| `.claude/CLAUDE.md` | Project-level operating rules and completion criteria |
| `CLAUDE.md` | Root instructions loaded by Claude Code |
| `.claude/settings.json` | Model preference, deny rules, and lifecycle hooks |
| `.claude/agents/` | Five recognized specialist subagents |
| `.claude/skills/` | Reusable prompt, research, writing, design, and automation skills |
| `.claude/hooks/` | Startup reminder, narrow command guardrail, post-edit reminder, completion reminder |
| `agents/` | Readable specialist prompt reference copies |
| `playbooks/` | Repeatable content, product, and growth workflows |
| `skills/` | Skill index and expanded human-readable guidance |
| `memory/MEMORY.md` | Curated durable project decisions; never secrets |
| `docs/` | Architecture, security, research, operations, and decision records |
| `run.sh` | Structural and shell syntax preflight |

## Quick start

1. Clone the repository:
   ```bash
   git clone https://github.com/squiraldot/Agent-Team.git
   cd Agent-Team
   ```
2. Review `CLAUDE.md`, `.claude/settings.json`, and every hook in `.claude/hooks/` before enabling them.
3. Confirm the configured model `claude-opus-5-5` is available to your Claude Code version/account/provider. Change it if necessary.
4. Install `jq` if you want the sample pre-tool hook to inspect JSON input.
5. Run the preflight:
   ```bash
   bash run.sh
   ```
6. Start Claude Code in the repository and try a harmless task. Check that the agents are available before relying on the workflow.

## How to use the team

For a multi-step request, ask the planner to define deliverables and acceptance criteria. Delegate current factual research to the researcher. Have the builder create the deliverable, then ask the reviewer to independently challenge it. Use the router to decide whether to revise, clarify, accept, or stop. Small tasks do not need every role.

Example requests:
- “Use planner, then researcher to verify the current API docs. Return findings with URLs before implementing.”
- “Use builder to implement the agreed change. Do not deploy. Run the narrowest relevant tests.”
- “Review this diff independently. Report only actionable findings, grouped by severity.”
- “Use the content playbook to draft an evidence-backed technical article; do not publish.”

## Folder map

```text
Agent-Team/
├── CLAUDE.md
├── README.md
├── .claude/
│   ├── CLAUDE.md
│   ├── settings.json
│   ├── agents/       # Claude Code subagents
│   ├── hooks/        # lifecycle shell scripts
│   └── skills/       # SKILL.md procedures
├── agents/           # readable prompt references
├── playbooks/
│   ├── content/
│   ├── product/
│   └── growth/
├── skills/
│   ├── prompts/
│   ├── research/
│   ├── writing/
│   ├── design/
│   └── automation/
├── memory/MEMORY.md
├── docs/
└── run.sh
```

## Safety model

Hooks and permission rules are helpful guardrails, **not a security sandbox**. The sample command hook only catches a narrow set of patterns. Review all scripts, run unfamiliar projects in a disposable clone/container, keep secrets out of Git, and require explicit approval for publishing, messaging, deployment, payments, and destructive operations. See [Security](docs/SECURITY.md).

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Security and privacy](docs/SECURITY.md)
- [Research sources and revalidation checklist](docs/RESEARCH.md)
- [Operations and troubleshooting](docs/OPERATIONS.md)
- [Architecture decisions](docs/DECISIONS.md)
- [Playbooks](playbooks/README.md)
- [Reusable skills](skills/README.md)
- [Project memory policy](memory/MEMORY.md)

## Research basis

The design draws on Anthropic's guidance for [CLAUDE.md, skills, hooks, and subagents](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more), the [Claude Code subagent documentation](https://code.claude.com/docs/en/sub-agents), [hooks documentation](https://code.claude.com/docs/en/hooks), [settings documentation](https://code.claude.com/docs/en/settings), and the [Claude Opus 5.5 model overview](https://platform.claude.com/docs/en/models/opus-5-5/overview). See [Research Notes](docs/RESEARCH.md) for date/version caveats.

## License

MIT; see [LICENSE](LICENSE).
