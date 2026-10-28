---
name: api-design
description: Design consistent, secure, evolvable APIs with documented contracts and testable error behavior.
version: 1.0.0
owner: Agent-Team maintainers
status: active
---

# Api Design

## Trigger conditions
Trigger when creating or revising HTTP, RPC, webhook, or public/internal service interfaces.

## Steps
1. Identify consumers, use cases, trust boundary, latency/volume needs, and compatibility constraints.
2. Define resources/actions, naming, HTTP semantics, schemas, validation, and content types.
3. Specify authentication, object-level authorization, rate limits, CORS where applicable, and sensitive-data handling.
4. Standardize success/error envelopes, status codes, pagination, filtering, idempotency, and retries.
5. Define versioning/deprecation, timeouts, quotas, observability, and webhook signature/replay handling.
6. Write examples and contract tests, including malformed input and authorization failures.
7. Review the contract with consumers before implementation.

## Checklist
- [ ] Consumer and trust boundary documented
- [ ] Request/response schemas and errors defined
- [ ] Authz, validation, limits, and idempotency considered
- [ ] Pagination and versioning rules explicit
- [ ] Contract tests cover negative paths
- [ ] Sensitive fields and logs minimized

## Failure modes
Ambiguous ownership or semantics: resolve before coding. Breaking change without migration plan: block release. Unbounded queries, retries, or payloads: add limits before production.

## Related canonical guidance
- Shared policy: [AGENTS.md](../../AGENTS.md)
- Research standards: [docs/RESEARCH.md](../../docs/RESEARCH.md)
- Extending this framework: [docs/EXTENDING.md](../../docs/EXTENDING.md)
