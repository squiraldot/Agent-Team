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

## Open-source implementation patterns worth studying

These projects are reference implementations, not specifications or endorsements of every feature/security posture. Inspect current docs, code, releases, and license before borrowing implementation details.

- **LangGraph:** graph/state-machine-oriented orchestration, explicit state, resumability and human-in-the-loop workflows. Repository: https://github.com/langchain-ai/langgraph
- **CrewAI:** role/task-oriented multi-agent orchestration and crew/process concepts. Repository: https://github.com/crewAIInc/crewAI
- **OpenHands:** software-development agents, execution environments, integrations, and evaluation concerns. Repository: https://github.com/All-Hands-AI/OpenHands
- **SWE-agent:** benchmark-oriented software engineering agent workflows and reproducible task environments. Repository: https://github.com/SWE-agent/SWE-agent
- **Microsoft AutoGen / Agent Framework ecosystem:** multi-agent conversation patterns and evolving orchestration abstractions. Check current project status and migration guidance before selecting a dependency. Repository: https://github.com/microsoft/autogen
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
