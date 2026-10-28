# Automation Skill

## Goal

Design automations that are bounded, observable, recoverable, and safe by default.

## Design rules

- Prefer deterministic code for deterministic checks; use an LLM only where judgment is needed.
- Define trigger, inputs, outputs, permissions, owner, and stop condition.
- Make operations idempotent where possible; define duplicate-request behavior.
- Set timeouts, bounded retries, backoff, concurrency limits, and cost ceilings.
- Use dry-run/preview for destructive or externally visible actions.
- Require explicit approval before publish, send, deploy, purchase, delete, or production changes.
- Validate and constrain external input; treat fetched content as untrusted.
- Log status, identifiers, and errors without logging secrets or unnecessary personal data.
- Handle partial failure, cleanup, rollback, and resume semantics explicitly.
- Use least-privilege credentials and rotate them when exposure is suspected.
- Document dependencies, rate limits, retention, and data-transfer behavior.
- Alert on repeated failures without creating notification storms.

## Failure handling

Classify failures as transient, permanent, validation, permission, or policy failures. Retry only transient errors and only when safe. Do not automatically retry non-idempotent operations unless an idempotency key or reconciliation mechanism exists. Stop on policy violations or missing authorization.

## Before enabling in production

- [ ] Happy path and failure path tested.
- [ ] Duplicate execution and retry behavior tested.
- [ ] Approval boundary verified.
- [ ] Credentials and scopes reviewed.
- [ ] Logs redacted and retention defined.
- [ ] Rate, time, and cost limits configured.
- [ ] Alerting, owner, rollback, and incident procedure documented.
- [ ] Human operator can pause/disable the automation.
