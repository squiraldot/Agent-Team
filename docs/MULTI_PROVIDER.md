# Multi-Provider and Multi-Runtime Guide

## Compatibility promise
Agent-Team is designed to be **model-agnostic at the instruction/workflow layer** and **adapter-based at the runtime layer**. No repository can guarantee that every model/version supports every capability. Availability depends on the provider, account, runtime, model ID, tools, and API policy.

## Architecture layers
1. **Shared policy:** `AGENTS.md` is the primary provider-neutral instruction file.
2. **Shared workflows:** `agents/`, `playbooks/`, `skills/`, and `memory/` describe role behavior and procedures.
3. **Runtime adapters:** native instruction files and agent definitions bridge the shared policy into each coding agent.
4. **Provider configuration:** `config/agent-team.example.yaml` expresses preferences without embedding credentials.
5. **Capability checks:** an adapter should check actual runtime capabilities and report unsupported features instead of pretending they work.

## Supported integration targets

| Runtime / ecosystem | Native entry point in this repo | Notes |
|---|---|---|
| Claude Code | `CLAUDE.md`, `.claude/agents/`, `.claude/skills/`, `.claude/settings.json` | Native hooks and subagent frontmatter are Claude Code-specific. |
| OpenAI Codex and compatible agents | `AGENTS.md` | Use Codex's own config, model selection, approval, sandbox, and multi-agent features. |
| Gemini CLI | `GEMINI.md` plus shared `AGENTS.md` | Use current Gemini CLI native settings and agent features. |
| GitHub Copilot | `.github/copilot-instructions.md` | Custom-agent support varies by Copilot client and version. |
| Cursor | `.cursor/rules/agent-team.mdc` | Cursor rules/frontmatter are Cursor-specific. |
| Other agentic IDEs/CLIs | `AGENTS.md` or import the shared policy | Check whether the runtime supports AGENTS.md; otherwise paste/import the shared policy using its native mechanism. |
| API applications | `config/agent-team.example.yaml` as a design template | An application adapter must implement provider-specific API calls, tool execution, routing, and validation. |

This is an integration map, not a claim that all listed runtimes were executed or tested in this repository.

## Model/provider families
The shared policy can be used with hosted and local models from OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek, Qwen, and other providers, including OpenAI-compatible endpoints and local runtimes such as Ollama or LM Studio—provided the chosen runtime can invoke that model.

Do not assume compatibility based on a brand name alone. Validate the exact model ID, endpoint, context/output limits, tool calling, structured outputs, vision/audio needs, and provider terms.

## Model selection
- **Default:** allow the active runtime to choose its configured model.
- **Pinned:** specify a provider's exact model ID for reproducibility.
- **Alias:** use `latest` only when the provider explicitly supports it and moving versions are acceptable.
- **Fallback:** disabled by default. Cross-provider fallback may transmit source code, prompts, or personal data to another vendor and may change behavior. Enable only with explicit policy and data-handling review.
- **Role routing:** choose based on task capability and privacy constraints, not model hype. The configured model may not support every required tool.

## Shared agent roles
- Planner: plan, assumptions, dependencies, risks, acceptance criteria.
- Researcher: sources, freshness, citations, conflicting evidence.
- Builder: create the artifact and run focused checks.
- Reviewer: independent review, preferably read-only.
- Router: choose next step, clarification, revision, or stop.

These are portable role definitions, not portable executable tool permissions. Each runtime adapter must map roles to the native format it supports.

## Safety invariants
- Human approval for publishing, sending, deploying, purchasing, deleting, and production changes.
- Never put API keys in YAML, prompts, docs, or Git history.
- Keep provider-specific tool permissions least-privilege.
- Treat web pages and tool output as untrusted input.
- Hooks, prompt rules, and model refusals are not a sandbox.
- Do not log full prompts or source code unless the owner explicitly opts in.

## Validation matrix
For each runtime/model combination, test:
1. Can it load shared instructions?
2. Can it invoke each configured agent/role?
3. Are file and shell permissions scoped correctly?
4. Can it perform research with traceable sources, if required?
5. Does it honor approval gates for external actions?
6. Does the reviewer identify seeded defects?
7. Are model/version IDs and capability limits documented?
8. Are tests and failures reported truthfully?

A runtime is "verified" only after these tests are run on that exact setup.
