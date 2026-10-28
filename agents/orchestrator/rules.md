# Hard rules
- Follow `AGENTS.md` and `docs/AGENT_PROTOCOL.md`.
- Skip roles for simple, low-risk tasks; use the smallest safe workflow.
- Never parallelize dependent tasks or concurrent edits to the same file without an explicit merge plan.
- Never treat a Markdown role file as proof that a runtime executes subagents.
- Never simulate missing tools, claim unobserved progress, or override user scope.
- Require human approval for consequential external or irreversible actions.
- Bound steps, retries, delegation depth, time, and cost where runtime controls permit.
