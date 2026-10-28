# UI/UX design sprint pipeline

**Use for:** discovery, user flows, interaction design, wireframes, prototypes and usability improvements.

## Ordered roles and handoffs

1. **Orchestrator** — [agents/orchestrator/role.md](../agents/orchestrator/role.md): product goal, audience, constraints, decision-maker and sprint timebox.
2. **Planner** — [agents/planner/role.md](../agents/planner/role.md): sprint questions, scope, hypotheses, acceptance signals and research plan.
3. **Deep Researcher** — [agents/deep-researcher/role.md](../agents/deep-researcher/role.md) + [UI/UX Designer](../agents/ui-ux-designer/role.md): user evidence, platform conventions, accessibility standards and competitive references; distinguish observations from assumptions.
4. **UI/UX Designer** — [agents/ui-ux-designer/role.md](../agents/ui-ux-designer/role.md): information architecture, flows, wireframes, visual hierarchy, responsive/error/empty states and prototype notes.
5. **Graphic Designer & Branding** — [agents/graphic-designer-branding/role.md](../agents/graphic-designer-branding/role.md), when visual identity or asset system is in scope: tokens, typography, color and asset direction.
6. **QA/Reviewer** — [agents/qa-reviewer/role.md](../agents/qa-reviewer/role.md): independently critique task completion, accessibility, consistency, edge cases and usability risks.
7. **UI/UX Designer** — incorporate findings and prepare handoff spec, components/states, interaction behavior and unresolved questions.
8. **Orchestrator** — deliver design artifacts, rationale, assumptions, review findings and validation plan.

## Quality gates

- Every primary flow has success, loading, empty, error and recovery states where applicable.
- Accessibility and responsive behavior are specified, not left as visual guesswork.
- Research findings, assumptions and design decisions are clearly separated.
- Usability testing is reported only if actually conducted; prototype inspection is not user testing.

## Parallelizable work

Research and an initial inventory of current screens may proceed concurrently after scope is stable. Designer and reviewer can work in parallel on separate artifacts after a checkpoint; do not let reviewer silently rewrite the design.
