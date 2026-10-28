# Deep research report pipeline

**Use for:** decisions or reports that need traceable, current, cross-checked evidence.

## Ordered roles and handoffs

1. **Orchestrator** — [agents/orchestrator/role.md](../agents/orchestrator/role.md): decision question, audience, deadline, constraints and risk.
2. **Planner** — [agents/planner/role.md](../agents/planner/role.md): research questions, scope, inclusion/exclusion criteria, freshness thresholds and output outline.
3. **Deep Researcher** — [agents/deep-researcher/role.md](../agents/deep-researcher/role.md): follow [research protocol](../research/PROTOCOL.md) and [source registry](../research/sources.md); capture source URL/title/publisher/date/access date, relevant version, claim supported and limitations.
4. **Domain specialist** — select the relevant existing contract (for example [Android Developer](../agents/android-developer/role.md), [Web Developer](../agents/web-developer/role.md), or [Software Developer](../agents/software-developer/role.md)): challenge applicability and technical interpretation.
5. **QA/Reviewer** — [agents/qa-reviewer/role.md](../agents/qa-reviewer/role.md): trace material conclusions to evidence, inspect conflicts, freshness, counterevidence, uncertainty and scope.
6. **Deep Researcher** — resolve findings where evidence permits; revise conclusions or explicitly retain unresolved disagreement.
7. **Orchestrator** — deliver executive summary, method, evidence, comparison, confidence/limitations, sources and decision implications.

## Quality gates

- Prefer primary/official sources, then maintained code/releases, then credible public community evidence according to [research protocol](../research/PROTOCOL.md).
- Distinguish observed facts, inference, and recommendation; preserve dates/version context and contradictory evidence.
- Never imply training knowledge has been disabled. Search coverage is bounded; record query/source gaps and avoid false comprehensiveness.
- Consequential recommendations with insufficient evidence are escalated, not dressed up as certainty.

## Parallelizable work

Independent research questions may be assigned concurrently after shared inclusion criteria are set. Have one owner consolidate duplicates/conflicts and a separate reviewer verify claims; do not split the same source log among concurrent writers without merge ownership.
