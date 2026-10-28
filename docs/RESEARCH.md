# Research Notes and Sources

Research snapshot: 2026-10-28. Re-check official documentation before upgrades; interfaces and model availability change.

1. Anthropic, “Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents” (2026-06-18): https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more — rationale for separating instructions, skills, subagents, and hooks.
2. Anthropic, “How to configure hooks”: https://claude.com/resources/articles/how-to-configure-hooks — project/user/local settings and matcher concepts.
3. Claude Platform Docs, Claude Opus 5.5: https://platform.claude.com/docs/en/models/opus-5-5/overview — model ID and provider-specific availability as researched.
4. Anthropic, “Introducing Claude Opus 5.5” (2026-09-22): https://www.anthropic.com/claude-opus-5-5 — official launch information.
5. Claude Code subagents: https://code.claude.com/docs/en/sub-agents — canonical subagent file/frontmatter reference.
6. Claude Code hooks: https://code.claude.com/docs/en/hooks — event names, payloads, matchers, exit behavior.
7. Claude Code settings: https://code.claude.com/docs/en/settings — settings and permissions.
8. Claude Code skills: https://code.claude.com/docs/en/skills — skill loading and structure.

## Findings and caveats
The reference diagram's planning/research/build/review/routing split is a workflow pattern, not a guarantee of autonomous agents. Model access depends on CLI version, account, and provider. Hooks are deterministic automation only when their event/schema is configured correctly; test locally.

## Revalidation checklist
Verify official URLs and schemas, confirm model ID access, test frontmatter and hook payloads in the installed CLI, review permission rules in a disposable repository, and update this file with date and observed changes.
