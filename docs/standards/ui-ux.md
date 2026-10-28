# UI/UX Design Standards

**Status:** Active guidance. Revalidate by 2027-01-28.  
**Research protocol:** Follow [research/PROTOCOL.md](../../research/PROTOCOL.md). All sources below were accessed 2026-10-28. Product-specific usability outcomes are **UNVERIFIED** until tested.

## Principles
- Start from user goals, context, constraints, and evidence—not trends or personal taste.
- Separate observed findings, stakeholder statements, hypotheses, and design decisions. Never invent participants or metrics.
- Design the full journey: entry, success, loading, empty, error, permission denied, offline, cancellation, and recovery states where applicable.
- Prefer predictable controls, clear status, familiar language, error prevention, reversible actions, and user control.
- Make accessibility a design requirement. Aim for WCAG 2.2 AA for applicable web experiences; this target is not a conformance claim without a full audit.
- Use responsive, content-first layouts, reusable semantic components, purposeful motion, and reduced-motion support.
- Minimize data collection, explain permissions at point of need, and reject deceptive consent/dark patterns.

## Process
1. **Brief:** record goal, audience, contexts/devices, constraints, decision owner, success signals, non-goals, and approvals.
2. **Research:** review direct evidence, platform conventions, accessibility guidance, and comparable products. Log URL, publisher, source/access dates, tier, applicability, and confidence.
3. **Synthesize:** map tasks, journey, information architecture, risks, and assumptions; label hypotheses needing research.
4. **Explore:** create flows and low-fidelity wireframes before visual polish; include alternate and failure paths.
5. **Specify:** define components, tokens, responsive behavior, interaction states, keyboard/focus behavior, motion, and content.
6. **Evaluate:** conduct risk-appropriate heuristic, accessibility, and usability checks. Record method, context/sample limits, issues, and evidence. Prototype inspection is not user testing.
7. **Handoff:** mark only reviewed frames ready; use [handoff spec](../../templates/handoff-spec.md), assets, tokens, decisions, and open questions.
8. **Independent review:** QA/Reviewer checks task coverage, accessibility, edge cases, implementation clarity, and evidence quality.

## Quality checklist
- [ ] Goals and acceptance criteria trace to the brief; evidence and assumptions are distinguishable.
- [ ] Success, loading, empty, error, offline, permission, and recovery states are covered where relevant.
- [ ] Layout works at agreed viewports, text zoom, and reflow conditions.
- [ ] Keyboard navigation, focus visibility, semantic order, labels, target size, contrast, and screen-reader names are considered.
- [ ] Color is not the only signal; reduced motion and text resizing are considered.
- [ ] Components/tokens have stable names; variants and behavior are documented.
- [ ] Test method/results, severity, known issues, owner, and approval status are recorded.
- [ ] Handoff includes source links, dimensions, assets, font/licence notes, responsive rules, and unresolved decisions.

## Common pitfalls
Happy-path-only flows; stakeholder preference presented as user evidence; color-only cues; tiny targets; invisible focus; hover-only interactions; one-off components; screenshots without state/behavior specs; treating automated scans as proof of WCAG conformance; claiming user testing that did not occur.

## Research sources (accessed 2026-10-28)
- W3C, [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — Tier 1 normative standard for web content.
- W3C WAI, [WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/) — Tier 1 explanatory guidance on versions and conformance.
- Figma, [Guide to Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode) — Tier 1 vendor guidance for inspecting designs, annotations, and assets; access varies by plan/seat.
- W3C, [Internationalization quick tips](https://www.w3.org/International/quicktips/index) — Tier 1 guidance for language, text, direction, and localized formats.

**UNVERIFIED:** No product-specific user study, usability metric, WCAG audit, or Figma entitlement was verified. Recheck vendor features and applicable law before relying on them.
