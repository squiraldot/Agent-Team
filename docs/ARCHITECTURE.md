# Architecture

## Overview
Agent-Team is a repository-level operating system for Claude Code: five focused subagents, playbooks, reusable skills, curated project memory, and lifecycle hooks.

```text
User request -> Router/Planner -> Researcher (when evidence is needed)
                           -> Builder -> Reviewer -> Router decision
                                      -> Human approval for external/irreversible actions
```

## Components
- `.claude/CLAUDE.md`: project instructions and completion criteria.
- `.claude/settings.json`: model preference, permission denies, hooks.
- `.claude/hooks/`: small shell lifecycle checks.
- `agents/`: specialist prompts.
- `playbooks/`: repeatable end-to-end workflows.
- `skills/`: reusable procedures.
- `memory/MEMORY.md`: durable project decisions.
- `run.sh`: local structural and syntax preflight.

## Design choices
Narrow roles reduce ambiguity; independent review challenges confirmation bias; human approval limits external impact. Skip unnecessary agents for simple tasks. Hooks are guardrails, not a sandbox.

## Execution model
Claude Code interprets the configuration according to the installed version. This repository does not implement a separate multi-agent runtime. `run.sh` validates files and shell syntax; it does not launch Claude or prove model behavior.

## Change process
Update relevant files, run `bash run.sh`, inspect diffs, validate JSON, test representative normal/ambiguous/unsafe tasks, and update this document when architecture changes.
