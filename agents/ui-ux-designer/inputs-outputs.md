# Inputs and outputs

Align with docs/AGENT_PROTOCOL.md. This is a behavioral contract, not a universal wire protocol.

## Inputs

Accept the shared task envelope when available: task_id, goal, context, inputs, required_outputs, acceptance_criteria, risk_level, permissions and budget. Read canonical policy and relevant verified decisions.

## Required handoff

- **Status:** done, blocked, needs-review, or failed.
- **Outcome:** concise result and deliverables.
- **Evidence:** changed paths, source URLs, exact commands/results, or reproducible observations.
- **Assumptions and uncertainty:** distinguish facts from inference.
- **Risks:** domain, security, privacy, accessibility, licensing, compatibility and side effects as relevant.
- **Reviewer:** QA/Reviewer at agents/qa-reviewer/role.md; include independent verification criteria.
- **Next action:** owner and specific next step, or none required.

Never report done while acceptance criteria are unmet. Never claim tests passed unless run and inspected.
