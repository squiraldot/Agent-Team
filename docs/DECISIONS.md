# Architecture Decision Records

## ADR-001: Separate agent roles
**Status:** Accepted. **Decision:** Use planner, researcher, builder, reviewer, router. **Reason:** Responsibilities become easier to delegate and inspect. **Trade-off:** Orchestration overhead; skip agents for simple tasks.

## ADR-002: Human approval for external actions
**Status:** Accepted. Publishing, messaging, deployment, payments, and destructive operations require explicit approval because they may be irreversible.

## ADR-003: Hooks are guardrails, not a sandbox
**Status:** Accepted. Keep hooks small and auditable; pattern matching cannot guarantee safety. Require human review and OS-level controls for higher-risk operations.

## ADR-004: Curated project memory
**Status:** Accepted. Store durable decisions, not raw logs or secrets, to reduce privacy risk and stale context.
