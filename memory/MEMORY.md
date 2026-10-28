# Project Memory

Store durable project decisions only. Never store passwords, API keys, private user data, or raw sensitive conversations.

## Current project
- Repository: https://github.com/squiraldot/Agent-Team
- Purpose: Claude Code team for planning, research, building/drafting, reviewing, and routing.
- Specialists: planner, researcher, builder, reviewer, router.
- Human approval is required for irreversible or externally visible actions.

## Decisions
- Agent prompts live in `agents/`.
- Repeatable workflows live in `playbooks/`.
- Reusable procedures live in `skills/`.
- Hooks are small, auditable guardrails—not a security boundary.
- Model identifiers and vendor behavior are versioned assumptions.

## Update policy
Add dated entries only for durable decisions. Include rationale and affected paths. Periodically remove stale assumptions. Never store secrets.
