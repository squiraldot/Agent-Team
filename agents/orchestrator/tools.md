# Needed capabilities
Required: read request/policy, inspect available role definitions and task state, create a structured plan/handoff.
Optional: native delegation, task tracking, parallel execution, budget controls.

## Graceful degradation
If delegation is unavailable, present the role sequence as a plan and execute only work the current runtime can actually perform. If parallel execution cannot be verified, sequence tasks. If task state is missing, report uncertainty rather than inventing it.
