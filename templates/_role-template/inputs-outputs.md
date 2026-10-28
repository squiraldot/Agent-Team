# Inputs and outputs

Align this handoff with `docs/AGENT_PROTOCOL.md`. Runtime serialization may differ; this is a behavioral contract, not a universal wire protocol.

## Inputs

Accept the shared task envelope when available: `task_id`, `goal`, `context`, `inputs`, `required_outputs`, `acceptance_criteria`, `risk_level`, `permissions`, and `budget`. Also read canonical policy and prior verified decisions relevant to the task.

## Required handoff

- **Status:** done, blocked, needs-review, or failed.
- **Outcome:** concise result or artifact produced.
- **Evidence:** changed paths, source URLs, exact commands/results, or reproducible observations.
- **Assumptions and uncertainty:** distinguish explicit facts from inference.
- **Risks:** security, privacy, compatibility, and external side effects.
- **Next action:** owner and specific next step, or no action required.

Never report done while acceptance criteria are unmet. Never claim tests passed unless run and inspected.
