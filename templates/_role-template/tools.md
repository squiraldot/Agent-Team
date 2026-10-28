# Needed capabilities

List only capabilities necessary for this role. Separate required from optional; name expected outputs rather than assuming a specific provider.

## Required

- Read relevant policy, task envelope, and source artifacts.
- Produce a structured handoff matching `inputs-outputs.md`.

## Optional

- Research, shell, repository-write, image, or other tools only when the task requires them and the active runtime exposes them.

## Graceful degradation

- If a required capability is unavailable, stop the affected subtask, state what is unavailable, and provide the safest useful partial result.
- Never claim an operation was performed when only instructions or a proposal were produced.
- If a source cannot be accessed, mark it unavailable and do not fabricate its contents.
