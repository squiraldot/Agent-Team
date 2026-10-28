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


## Direct-API adapter specification

A direct-API adapter is application code that implements the runtime, not a prompt template. It must map the canonical role/workflow contracts into the chosen provider's documented API and preserve observable, bounded execution.

### Required components

1. **Policy loading:** load `AGENTS.md` plus only the selected role and workflow contracts. Record a content digest and never silently use a stale embedded copy.
2. **Capability negotiation:** identify provider, endpoint, exact model ID, API version, supported modalities, tool calling, structured output, streaming, context limits, web/search, parallelism, and approval controls. Treat unknown capabilities as unavailable until tested.
3. **Request mapping:** translate system/developer instructions, user input, tool schemas, response formats, and provider-specific parameters explicitly. Reject unsupported required options rather than silently dropping them.
4. **Tool execution loop:** validate model-produced tool calls against an allowlist and schema; authorize each call, execute only permitted tools, return bounded observations, and continue until a documented stop condition or budget limit. Model output is untrusted input, not executable authority.
5. **State and handoffs:** persist only required task state; distinguish task/session state from curated long-term memory. Validate handoff payloads and ensure role boundaries survive provider translation.
6. **Safety and approvals:** enforce least privilege outside the model where possible. Require explicit human approval for publishing, messaging, deployment, spending, deletion, production changes, and other consequential side effects. If the provider cannot enforce a required control, implement it in the application or fail closed.
7. **Reliability:** implement timeouts, cancellation, bounded retries/backoff for retryable failures, idempotency for side effects, rate-limit handling, and explicit partial-failure states. Never retry a non-idempotent action blindly.
8. **Observability and privacy:** record correlation IDs, provider/model/version, tool names, latency, token/cost metadata when available, stop reason, and outcome. Redact secrets and sensitive content; document retention, residency, and provider data-use implications.
9. **Output contract:** return the normalized result above with status, summary, evidence/sources, changed paths, checks actually run, warnings, and unresolved decisions.
10. **Testing:** test authentication without credential logging, malformed tool calls, multi-turn continuation, tool errors, budget exhaustion, cancellation, approval denial, partial failure, redaction, and one harmless end-to-end task against the exact endpoint/model version.

### Minimal execution state machine

`queued → validate → plan/route → model request → (tool authorization → tool execution → tool result → model request)* → validate result → handoff`

Terminal states are `success`, `partial`, `blocked`, or `failed`. The loop must stop on user cancellation, denied approval, unrecoverable provider/tool error, exhausted step/time/cost budget, repeated no-progress output, or a valid final response. Do not infer success solely from an HTTP 200 response.

### Direct-API conformance record

For every tested deployment, record provider, base URL/region, API version, exact model ID, SDK/version, date, enabled tools and scopes, policy digest, approval strategy, timeout/retry budgets, tests and raw pass/fail summary, known limitations, and data-retention assumptions. Mark a deployment **tested** only after the documented real test set has run and its output has been inspected.
