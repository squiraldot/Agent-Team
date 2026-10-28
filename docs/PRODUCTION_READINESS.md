# Production Readiness Standard

This repository is a portable agent-team specification and runtime configuration starter. It is not, by itself, a hosted multi-agent service, security sandbox, universal model gateway, or proof that a workflow is production-safe.

## Readiness levels

| Level | Meaning | Evidence required |
|---|---|---|
| L0 — Documented | Roles and procedures are described | Reviewed docs and examples |
| L1 — Structurally validated | Expected files/configuration exist and parse | CI preflight passes |
| L2 — Runtime validated | A named harness can load the configuration | Recorded smoke-test transcript |
| L3 — Workflow evaluated | Critical workflows pass repeatable task tests | Evaluation results and regression set |
| L4 — Operationally ready | Monitoring, access controls, recovery, ownership and release process exist | Operational sign-off for a defined deployment |

Never label the whole project "production-ready" merely because documentation or static checks pass. Report the achieved level and the exact tested environment.

## Release gates

A release candidate should pass all applicable gates:

1. **Requirements:** scope, user intent, constraints, acceptance criteria, and out-of-scope items are explicit.
2. **Research:** time-sensitive claims use current primary sources; every material factual claim is attributable; conflicts and unknowns are visible.
3. **Implementation:** changes are minimal, traceable, and include tests for behavior changes.
4. **Review:** a reviewer independent of the implementation checks correctness, security, privacy, regressions, and requirements coverage.
5. **Validation:** run relevant tests, linters, formatters, config parsing, and integration smoke tests. Report skipped checks honestly.
6. **Safety:** secrets are not exposed; risky tools are least-privilege; irreversible or external side effects require explicit authorization.
7. **Delivery:** summarize changed files, decisions, test commands/results, known limitations, and follow-up work.

## Reliability controls

- Bound retries, tool calls, time, output size, recursion, and delegation depth.
- Retry only transient failures; use backoff and jitter in executable adapters.
- Do not retry non-idempotent actions automatically unless an idempotency strategy exists.
- Preserve task state in explicit artifacts rather than relying only on conversation history.
- Make workflows resumable where possible; define what happens after partial failure.
- Use structured task handoffs with inputs, outputs, assumptions, and completion criteria.
- Treat agent output as a proposal until checked against evidence or tests.
- Fail closed for missing authorization, unknown tools, invalid configuration, and policy violations.
- Fail visibly for unavailable provider capabilities; do not silently pretend a feature ran.

## Human approval boundaries

Require explicit human approval before:
- publishing, emailing, messaging, or posting externally;
- deploying, promoting, or changing production infrastructure;
- purchases, paid API usage above a configured budget, or financial transactions;
- deleting data, destructive migrations, or irreversible changes;
- changing access controls, secrets, identity, or security policy;
- uploading private source, logs, customer data, or prompts to another provider.

Approval must identify the action, target, scope, and relevant data transfer. A generic earlier approval is not blanket authorization for a different action.

## Operational metrics

For a real deployed adapter, record at least:
- task success rate against a versioned evaluation set;
- policy/approval violations and blocked actions;
- tool success/failure and retry counts;
- end-to-end latency and per-step latency;
- token or provider usage and estimated cost;
- fallback frequency and provider/model selected;
- human override/rework rate;
- incident count and severity.

Do not log secrets, full sensitive prompts, or customer content by default. Prefer redacted metadata and configurable retention.

## Release checklist

- [ ] Change is scoped and reviewed.
- [ ] Static validation and automated tests pass.
- [ ] Native runtime smoke test is recorded for each claimed integration.
- [ ] Evaluation suite passes or exceptions are documented.
- [ ] Security and privacy review completed for tool/data changes.
- [ ] Changelog and compatibility record updated.
- [ ] Rollback/recovery procedure exists for deployed components.
- [ ] Release notes distinguish verified behavior from planned capability.
