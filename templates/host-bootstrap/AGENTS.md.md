<!-- agent-team:begin -->
Read {{SUBMODULE_PATH}}/AGENTS.md first before acting. Treat that file as the source of truth for Agent-Team workflow, role contracts, research protocol, and review gates. Resolve every framework path (agents, skills, workflows, research, templates, config, docs, and evals) relative to the {{SUBMODULE_PATH}} directory, never relative to the host root.

Precedence: the host project's own rules win for project-specific architecture, style, dependencies, and conventions. Agent-Team governs the workflow, evidence-first research protocol, independent review gates, safety boundaries, and honest verification reporting. Resolve conflicts using {{SUBMODULE_PATH}}/docs/CONFLICT_RESOLUTION.md.

Keep the submodule pinned and read-only. Write host-specific memory, evidence, run logs, and decisions only under {{LOCAL_STATE}}/ (memory/, evidence/, runs/, decisions/). Never write mutable host state into the submodule. Do not overwrite user files; preserve all content outside this managed block.
<!-- agent-team:end -->
