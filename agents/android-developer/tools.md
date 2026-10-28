# Needed capabilities

## Required
- Read AGENTS.md, the task envelope, applicable artifacts, and docs/AGENT_PROTOCOL.md.
- Produce the structured handoff specified in inputs-outputs.md.

## Optional
- Domain editor, repository, test/build, research/browser, design/image, package, or API tools only when the task needs them and the active runtime exposes them.

## Graceful degradation
- If a required capability is unavailable, stop the affected subtask, state the limitation, and provide a safe partial result.
- Never claim an operation was performed when only instructions or a proposal were produced.
- If a source cannot be accessed, mark it unavailable rather than inventing its contents.
