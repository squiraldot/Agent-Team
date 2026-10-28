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
| Provider SDK / managed agent APIs (e.g. OpenAI Agents SDK/API, Google ADK, Mistral Agents API) | Adapter/application-owned | Framework-specific | Framework-specific | Framework-specific | Provider/framework-specific | These are executable frameworks/services, not merely instruction files; orchestration, state, tools, and deployment are implemented differently |
| Direct provider APIs (including DeepSeek tool calling and other model endpoints) | Adapter-owned instructions | Must be implemented in orchestration unless provided by the chosen API | Must be implemented or supplied by framework | Must be implemented | API-specific | Prompts alone do not provide a full agent loop; tool schemas and continuation semantics vary |
| OpenAI-compatible endpoints | Adapter-owned | Usually application-owned | Application-owned | Application-owned | Endpoint-specific | Compatibility often covers request shape, not every tool-call, streaming, structured-output, or context feature |
| Local inference (Ollama/LM Studio/etc.) | Host-specific | Host-specific | Host-specific | Host-specific | Host-specific | OpenAI-compatible API shape does not guarantee identical tool calling or model capability |

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


## Provider API and framework references

These links illustrate the diversity of executable agent platforms. They are not proof that Agent-Team has implemented or tested an adapter for them.

- **OpenAI Agents SDK / Agents API:** the SDK runs an agent loop in the application; the managed Agents API runs a managed harness. Official guidance covers specialist handoffs, tools, guardrails, state, and tracing.  
  https://developers.openai.com/api/docs/guides/agents/sdk  
  https://developers.openai.com/api/docs/guides/agents-api/overview  
  https://developers.openai.com/api/docs/guides/agents/orchestration
- **Google Agent Development Kit (ADK):** supports multi-agent composition, workflow agents, tools, evaluation, and deployment options.  
  https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk
- **Mistral Agents API:** models, instructions, tools, agents, conversations, and handoffs are represented through Mistral's own API objects and schemas.  
  https://docs.mistral.ai/studio/agents/agents-api  
  https://docs.mistral.ai/studio/agents/agent-tools
- **DeepSeek API:** tool calling uses its API's supported message/tool semantics; compatibility with OpenAI/Anthropic formats does not mean every feature behaves identically. Check the current tool-call and integration guides.  
  https://api-docs.deepseek.com/guides/tool_calls/  
  https://api-docs.deepseek.com/quick_start/agent_integrations/

## Adapter acceptance checklist

Before a provider adapter is considered usable, test:
- authentication and secret loading without logging credentials;
- model ID validation and capability discovery;
- tool-call schema mapping and malformed-call handling;
- multi-turn tool continuation and stop conditions;
- timeout, retry, rate-limit, and partial-failure behavior;
- streaming and structured output if required;
- human approval and idempotency for external side effects;
- trace redaction, retention, and provider data-transfer policy;
- a minimal task test and the safety/regression suite.

An endpoint that accepts an OpenAI-style request is not automatically a production-ready agent runtime.
