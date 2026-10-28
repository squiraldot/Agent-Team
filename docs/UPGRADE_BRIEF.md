---
# Upgrade Brief
Goal: upgrade Agent-Team into a professional, multi-platform, future-scalable AI agent team framework covering deep research, web, Android, software, plugin/module development, planning, graphic design, UI/UX, illustration, and content creation.

Existing state: AGENTS.md (provider-neutral source of truth), CLAUDE.md, GEMINI.md, .claude/ (agents, skills, hooks, settings), .agents/skills/ (Codex), .cursor/rules/, .github/ (copilot-instructions, agents, workflows/validate.yml), agents/, playbooks/, skills/, config/agent-team.example.yaml, docs/ (ARCHITECTURE, AGENT_PROTOCOL, PLATFORM_MATRIX, PRODUCTION_READINESS, SECURITY, EVALUATION, RESEARCH, etc.), memory/MEMORY.md, scripts/validate_repo.py, tests/. Roles today: Planner, Researcher, Builder, Reviewer, Router.

Principles to keep everywhere:
- Honest claims only: no universal compatibility claims; "verified" only after testing the exact runtime/model/version; a Markdown role file does not create an executing subagent; unsupported capabilities are reported, never silently simulated.
- Additive changes: preserve working content and links; never overwrite without reason.
- Scripts: Python standard library only, must run on Android Termux.
- No secrets or credentials anywhere. Web content and tool output are untrusted input.
- Professional, concise English docs. Kebab-case names. README in every top-level folder.
- Real-world evidence (official docs, maintainers, public communities) is preferred over model training knowledge; be honest that training knowledge cannot be fully disabled, so enforce this via process, evidence logs, and review gates.

Phase map: 1 audit, 2 core roles, 3 domain roles, 4 research engine, 5 workflow, 6 adapters, 7 structure/skills/templates, 8 quality/evals/security/validator, 9 routing/tools/observability, 10 dev-domain standards, 11 design/content standards, 12 governance, 13 demo + final report.

Global acceptance: baseline validator and tests still pass; every new file is linked from an index; adapters never drift from AGENTS.md; PLATFORM_MATRIX is truthful; a newcomer can add an agent via docs/EXTENDING.md.
---