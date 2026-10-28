# Product Discovery and Delivery Playbook

## Goal

Turn a feature idea into a scoped, testable user outcome with explicit acceptance criteria and controlled risk.

## Inputs

User/persona, problem, current workaround, desired outcome, constraints, platform, existing architecture, timeline/budget if relevant, data sensitivity, and decision owner.

## Workflow

1. **Discover:** identify user, problem, frequency, current workaround, and why it matters.
2. **Define outcome:** describe what success changes for the user; avoid starting from a list of UI components.
3. **Specify:** functional requirements, non-functional requirements, out-of-scope items, assumptions, and acceptance criteria.
4. **Map journeys:** happy path, empty/loading/error states, cancellation, recovery, accessibility, offline/slow network, and edge cases.
5. **Assess risk:** data collected, permissions, authentication, payments, retention/deletion, third-party services, abuse, and operational cost.
6. **Research:** verify platform/API capabilities and licensing in official docs; inspect existing code before choosing a new dependency.
7. **Plan:** slice work into independently testable increments; identify dependencies and rollback strategy.
8. **Build:** implement the smallest end-to-end slice that proves value; do not add speculative architecture.
9. **Test:** unit, integration, and critical user-flow checks as appropriate; include regression tests for fixed bugs.
10. **Review:** independent review of requirements, correctness, security, privacy, accessibility, performance, and maintainability.
11. **Release:** owner approves the change; provide release notes, known limitations, monitoring, and rollback instructions.

## Acceptance-criteria template

```text
Given [starting state]
When [user action or event]
Then [observable result]
And [important safety/error behavior]
```

Criteria must be observable. "Works well" and "secure" are not sufficient without concrete checks.

## Quality gates

- Every requirement maps to a criterion or is explicitly deferred.
- Error and empty states are designed, not left implicit.
- Sensitive data is minimized and has a documented purpose and lifecycle.
- Permissions are least-privilege and requested when needed.
- External side effects have idempotency/retry handling where appropriate.
- Tests and known limitations are reported honestly.
- No production rollout or data migration occurs without explicit approval.

## Failure handling

If scope grows, return to planning. If a dependency is unavailable, document the constraint and alternatives. If tests cannot run, state why and avoid presenting the feature as fully verified. For destructive migrations, require backup, recovery plan, and owner approval.

## Deliverables

Problem statement, requirements, acceptance criteria, implementation plan, risk notes, changed artifacts, test evidence, release/rollback notes, and unresolved questions.
