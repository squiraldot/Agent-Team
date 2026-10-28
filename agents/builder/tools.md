# Needed capabilities

## Required
- Read canonical policy, task envelope, relevant artifacts, and acceptance criteria.
- Produce the structured handoff defined in `inputs-outputs.md`.

## Optional
- Use only tools actually exposed by the active runtime and required for the assigned task. Record the tool/source/command actually used.

## Graceful degradation
- If a needed capability is unavailable, stop the affected subtask, explain the limitation, and return a useful partial result or next step.
- Do not claim that a search, test, code execution, or external action occurred unless it actually did.
