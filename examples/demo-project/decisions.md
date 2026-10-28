# Decision records — SproutLog demo

## ADR-DEMO-001: Use a single self-contained static document

- **Status:** Accepted
- **Date:** 2026-10-28
- **Question:** What is the smallest implementation that demonstrates a reviewable landing-page pipeline without creating avoidable setup risk?
- **Options considered:** framework app with dependencies; split HTML/CSS/JS; one HTML file with embedded CSS.
- **Decision:** One HTML document with embedded CSS and no JavaScript.
- **Evidence:** [Plan](plan.md) requires a locally runnable, small demo. [E1](evidence-log.md#e1--responsive-layout-should-accommodate-varied-viewport-sizes) and [E2](evidence-log.md#e2--reflow-and-keyboard-operability-are-relevant-accessibility-checks) support responsive layout and accessibility-oriented implementation choices, but do not require a framework.
- **Rationale:** A browser can open the page directly; no package manager, build step, external font, image, analytics, or network dependency is needed.
- **Consequences:** The demo is intentionally small and does not prove complex application architecture, cross-browser support, or production readiness.
- **Rollback:** Split files or introduce a framework only if future requirements justify the extra tooling and testing.

## ADR-DEMO-002: Do not imply an actual signup or product exists

- **Status:** Accepted
- **Date:** 2026-10-28
- **Decision:** Use fictional product copy and an in-page anchor CTA; collect no user data and make no outcome claims.
- **Rationale:** The scope is a workflow demonstration, not a deployed commercial product. No backend, contact channel, testimonials, user counts, or conversion evidence exists.
- **Risk avoided:** Misleading visitors or inventing a product promise.
