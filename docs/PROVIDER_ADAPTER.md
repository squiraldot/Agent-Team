# Provider Adapter Contract

This document specifies how a future CLI/API adapter should consume the provider-neutral Agent-Team configuration. It is a contract, not a claim that a universal adapter implementation is already included.

## Inputs
- Shared rules: `AGENTS.md`
- Role definitions: `agents/*.md`
- Workflow procedures: `playbooks/` and `skills/`
- Optional preferences: `config/agent-team.example.yaml`, copied to a local config and edited by the operator
- Runtime credentials supplied through environment variables or a secret manager

## Required adapter behavior
1. Parse and validate configuration; reject unknown required fields.
2. Discover runtime/provider capabilities at startup when possible.
3. Resolve provider and model from explicit user config, then runtime defaults. Never silently assume a particular vendor/model.
4. Map role prompts to the runtime's native subagent/agent API when available; otherwise run roles sequentially as ordinary prompts.
5. Map tool permissions and approval requirements to native controls. If a runtime cannot enforce a required control, fail closed or require explicit operator acknowledgement.
6. Enforce timeouts, bounded retries, and cancellation.
7. Keep cross-provider fallback disabled unless explicitly enabled.
8. Redact secrets and minimize transmitted context.
9. Return structured results with status, provider/model identifiers actually used, sources, changed paths, tests run, warnings, and unresolved items.
10. Never claim a tool, model, or test was used if it was not.

## Suggested normalized result
```json
{
  "status": "success | partial | blocked | failed",
  "role": "planner | researcher | builder | reviewer | router",
  "provider": "actual provider name",
  "model": "actual model ID or null",
  "summary": "short outcome",
  "sources": [],
  "changed_paths": [],
  "checks": [],
  "warnings": [],
  "unresolved": []
}
```

## Capability negotiation
Represent capabilities explicitly, for example: text, vision, audio, web_search, file_read, file_write, shell, structured_output, tool_calling, parallel_agents, and human_approval. A role may run only when its required capabilities are available or an approved fallback exists.

## Failure policy
- Invalid configuration: stop with actionable validation errors.
- Unknown model: ask the runtime/provider or stop; do not guess.
- Missing capability: report unsupported capability and offer a safe alternative.
- Rate limit/transient error: bounded retry with backoff.
- Authentication failure: stop; never print credentials.
- Cross-provider fallback: require explicit opt-in and privacy review.
- Partial execution: report completed work and remaining steps; do not imply atomic success.

## Security
The adapter must not treat model output as trusted code. Commands require policy checks and runtime permissions. Destructive or external actions require explicit approval. Provider logs and retention policies differ; document the exact provider's data handling before sending sensitive repositories.
