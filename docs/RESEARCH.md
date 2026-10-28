# Research Notes: Agent-Team Design

**Research snapshot:** 2026-10-28. Official documentation changes frequently; verify current behavior before adopting a platform feature. This is a design synthesis, not a claim that every feature was tested in this repository.

## Research question

How should a repository define a useful agent team across multiple AI coding platforms without pretending their runtime features are identical?

## Primary-source findings

### Shared instructions, skills, and subagents

- **OpenAI Codex:** customization separates persistent project instructions (`AGENTS.md`), reusable skills, MCP connections, and subagents. Skills can include instructions, scripts, references, and assets. This supports keeping the portable core concise and moving repeatable procedures into skills.  
  Source: https://learn.chatgpt.com/docs/customization/overview
- **Anthropic Claude Code:** official guidance distinguishes `CLAUDE.md`, rules, skills, hooks, and subagents by loading behavior, authority, and execution timing. Hooks are suitable for deterministic lifecycle checks; natural-language instructions alone are not enforcement.  
  Source: https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more
- **Google Gemini CLI:** its docs describe project context, settings, hooks, extensions, skills, model selection, sandboxing, telemetry, and subagents. Gemini-native files and settings should be used where Gemini CLI is the target rather than assuming Claude configuration transfers.  
  Sources: https://github.com/google-gemini/gemini-cli/blob/main/docs/index.md ; https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md ; https://github.com/google-gemini/gemini-cli/blob/main/docs/hooks/reference.md
- **GitHub Copilot / VS Code:** repository-wide instructions and path-specific instructions have different scopes; custom agent definitions are distinct from instruction files. Support depends on client and feature, so compatibility should be stated per surface.  
  Sources: https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions ; https://docs.github.com/en/copilot/concepts/customizations/custom-agents ; https://code.visualstudio.com/docs/agent-customization/custom-instructions
- **Cursor:** project rules and AGENTS.md are supported instruction mechanisms, while MCP connects external systems. Use current Cursor docs for exact rule frontmatter and settings.  
  Sources: https://cursor.com/docs ; https://cursor.com/docs/mcp

### Executable agent SDKs and provider APIs

- **OpenAI Agents SDK / Agents API:** official docs distinguish application-owned orchestration from a managed harness, and describe handoffs versus agents-as-tools, guardrails, state, and tracing. The project should not conflate a prompt template with an executable agent loop. Sources: https://developers.openai.com/api/docs/guides/agents/sdk ; https://developers.openai.com/api/docs/guides/agents-api/overview ; https://developers.openai.com/api/docs/guides/agents/orchestration
- **Google Agent Development Kit (ADK):** supports workflow agents for predictable sequential/parallel/loop patterns, agent-coordinated routing, tools, evaluation, and deployment. This reinforces separating deterministic workflow control from model-driven delegation. Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk
- **Mistral Agents API:** its API models agents, instructions, tools, and conversations as provider-specific objects; tool categories include search, code execution, function calling, and connectors. An adapter must map those objects explicitly. Sources: https://docs.mistral.ai/studio/agents/agents-api ; https://docs.mistral.ai/studio/agents/agent-tools
- **DeepSeek tool calling:** the API documents tool-call behavior and compatibility paths. An OpenAI/Anthropic-compatible request shape is not a promise that all continuation, strict schema, streaming, or thinking-mode behavior is identical. Sources: https://api-docs.deepseek.com/guides/tool_calls/ ; https://api-docs.deepseek.com/quick_start/agent_integrations/

## Open-source implementation patterns worth studying

These projects are reference implementations, not specifications or endorsements of every feature/security posture. Inspect current docs, code, releases, and license before borrowing implementation details.

- **LangGraph:** its persistence documentation separates thread-scoped checkpoints from longer-lived stores. The transferable lesson is to distinguish resumable task/session state from curated cross-task memory, and to design interruption/recovery explicitly rather than assuming chat history is durable. Sources: https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/persistence.mdx ; https://github.com/langchain-ai/langgraph
- **CrewAI:** current docs describe agents, crews, flows, structured outputs, guardrails, persistence/resume, and human-in-the-loop patterns. The transferable lesson is to define task state, outputs, routing, and approval boundaries explicitly. Repository/docs: https://github.com/crewAIInc/crewAI
- **OpenHands:** architecture docs separate user interface, agent server, event/state handling, runtime interfaces, and execution environments. The transferable lesson is to keep UI/orchestration, model interaction, and sandbox/runtime boundaries distinct. Local runtime access can expose the host workspace; use isolated execution for untrusted tasks. Sources: https://github.com/OpenHands/docs/blob/main/openhands/usage/architecture/backend.mdx ; https://github.com/All-Hands-AI/OpenHands
- **SWE-agent:** its Agent-Computer Interface uses constrained, purpose-built file/search/edit feedback and can validate edits before allowing them. The transferable lesson is that tool design and concise, structured observations can improve reliability; prompts alone are not the whole agent system. Sources: https://github.com/SWE-agent/SWE-agent/blob/main/docs/background/aci.md ; https://github.com/SWE-agent/SWE-agent
- **Microsoft AutoGen / Agent Framework ecosystem:** multi-agent conversation patterns and evolving orchestration abstractions. Check current project status and migration guidance before selecting a dependency. Repository: https://github.com/microsoft/autogen
- **OpenAI agent evaluations:** OpenAI recommends using traces, graders, datasets, and eval runs to find workflow-level regressions, including tool selection and handoff failures. The transferable lesson is to evaluate whole workflows, not only final text. Source: https://developers.openai.com/api/docs/guides/agent-evals
- **Model Context Protocol:** a standard protocol for exposing tools/resources/prompts across compatible clients and servers; MCP is a connection mechanism, not a guarantee that a tool is safe. Specification: https://modelcontextprotocol.io/

## Synthesis: decisions for this repository

1. Keep `AGENTS.md` the canonical shared policy; platform-specific files should be small wrappers and avoid conflicting copies.
2. Separate portable role descriptions from native subagent files. A role prompt does not itself create a parallel agent.
3. Make capability checks explicit: web research, file edits, shell, structured output, parallel agents, hooks, and approvals vary by runtime.
4. Keep human approval for high-impact external side effects, even if a model claims an action is safe.
5. Treat hooks as deterministic guardrails only within their configured event and runtime. They are not a general sandbox.
6. Store secrets outside Git; minimize logging and cross-provider data transfer.
7. Evaluate task outcomes and safety boundaries with a versioned regression set.
8. Distinguish static validation, runtime smoke testing, evaluation, and production operations in all claims.
9. Keep provider routing configuration descriptive until an adapter actually validates and executes it.
10. Record exact runtime/model combinations before marking them verified.

## Limitations and confidence

- Official docs establish documented concepts for their product versions, not universal cross-platform behavior.
- Community repositories change quickly; this snapshot does not replace reviewing their current source and releases.
- No live test was performed for every provider/model/runtime combination by writing this document.
- This repository defines portable instructions, templates, and validation assets; it does not yet implement a universal provider API gateway or durable distributed orchestrator.

## Revalidation checklist

- [ ] Verify official URLs and schemas after major platform releases.
- [ ] Confirm model access and supported capabilities for the exact account/runtime.
- [ ] Test native agent frontmatter and hook payloads in a disposable repository.
- [ ] Review permission rules and cross-provider data transfer behavior.
- [ ] Update compatibility records with exact versions, date, commands, and observed results.
