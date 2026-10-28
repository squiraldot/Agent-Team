# Architecture Decision Records

Use this log for consequential architecture, governance, and cross-role decisions. Pending entries are unresolved. For agent conflicts, follow [Conflict Resolution](CONFLICT_RESOLUTION.md); for contracts/adapters use [Versioning](VERSIONING.md) and [Migration](../MIGRATION.md).

## ADR-001: Separate agent roles
**Status:** Accepted. **Decision:** Use planner, researcher, builder, reviewer, router. **Reason:** Responsibilities become easier to delegate and inspect. **Trade-off:** Orchestration overhead; skip agents for simple tasks.

## ADR-002: Human approval for external actions
**Status:** Accepted. Publishing, messaging, deployment, payments, and destructive operations require explicit approval because they may be irreversible.

## ADR-003: Hooks are guardrails, not a sandbox
**Status:** Accepted. Keep hooks small and auditable; pattern matching cannot guarantee safety. Require human review and OS-level controls for higher-risk operations.

## ADR-004: Curated project memory
**Status:** Accepted. Store durable decisions, not raw logs or secrets, to reduce privacy risk and stale context.

## ADR-005: Stage-gated professional workflows
**Status:** Accepted. **Decision:** Define one canonical, provider-neutral workflow with explicit entry/exit criteria, owners, artifacts, failure handling, simplification rules, and human escalation; provide small domain pipelines that reference canonical role contracts. **Reason:** Repeatable handoffs and visible quality gates reduce omissions while keeping responsibilities auditable. **Trade-offs:** Process adds overhead, so trivial low-risk tasks may skip formal stages; documented pipelines are specifications, not executable orchestration, and parallel work is conditional on verified runtime support. **Rollback:** Revert or amend individual pipeline guidance without changing canonical role policy; consequential external actions still require human approval.

## New decision record template
Copy this template for a new consequential decision. For a disagreement, include both agent positions and evidence, then the Orchestrator's assessment and human decision where required.

### ADR-NNN: Short decision title
- **Status:** Proposed / Pending / Accepted / Rejected / Superseded
- **Date / owner / approver:**
- **Question and context:**
- **Constraints and scope:**
- **Position A and evidence:** role, recommendation, source/path + access date, confidence, risks
- **Position B and evidence:** role, recommendation, source/path + access date, confidence, risks
- **Shared facts / unresolved disputes:** mark unknowns **UNVERIFIED**
- **Options considered:** including defer/no-change
- **Decision and rationale:** or explicitly state **Pending** and why
- **Consequences / compatibility / licensing impact:**
- **Actions:** owner, due date, tests, migration/rollback
- **Links:** issue/PR, artifacts, research log, related ADRs
