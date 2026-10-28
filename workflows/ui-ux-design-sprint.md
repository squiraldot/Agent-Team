# UI/UX design sprint pipeline

**Use for:** discovery, user flows, interaction design, wireframes, prototypes and usability improvements.

**Standards:** [UI/UX](../docs/standards/ui-ux.md), [graphic branding](../docs/standards/graphic-branding.md) when visual identity is in scope, and [deliverable formats](../docs/DELIVERABLE_FORMATS.md). Use [handoff template](../templates/handoff-spec.md).

## Ordered roles and handoffs

1. **Orchestrator** — [agents/orchestrator/role.md](../agents/orchestrator/role.md): product goal, audience, constraints, decision-maker and sprint timebox.
2. **Planner** — [agents/planner/role.md](../agents/planner/role.md): sprint questions, scope, hypotheses, acceptance signals and research plan.
3. **Deep Researcher + UI/UX Designer** — [Deep Researcher](../agents/deep-researcher/role.md) and [UI/UX Designer](../agents/ui-ux-designer/role.md): user evidence, platform conventions, accessibility and competitive references; distinguish observations from assumptions.
4. **UI/UX Designer** — [role contract](../agents/ui-ux-designer/role.md): information architecture, flows, wireframes, visual hierarchy, responsive/error/empty states and prototype notes.
5. **Graphic Designer & Branding** — [role contract](../agents/graphic-designer-branding/role.md), when visual identity/assets are in scope: tokens, typography, color and asset direction.
6. **QA/Reviewer** — [role contract](../agents/qa-reviewer/role.md): independently critique task completion, accessibility, consistency, edge cases and usability risks.
7. **UI/UX Designer** — incorporate findings and prepare handoff spec, components/states, interaction behavior and unresolved questions.
8. **Orchestrator** — deliver design artifacts, rationale, assumptions, review findings and validation plan.

## Quality gates

- Every primary flow has success, loading, empty, error and recovery states where applicable.
- Accessibility and responsive behavior are specified, not left as visual guesswork.
- Research findings, assumptions and design decisions are clearly separated.
- Usability testing is reported only if conducted; prototype inspection is not user testing.
- Handoff names actual files, source links, tokens, asset/licence status, open issues and approval state.

## Parallelizable work

Research and initial screen inventory may proceed concurrently after scope stabilizes. Designer and reviewer may work in parallel on separate artifacts after a checkpoint; reviewer must not silently rewrite the design.
