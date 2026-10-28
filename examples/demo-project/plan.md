# Plan — SproutLog landing page

**Task ID:** phase13-sproutlog-demo  
**Status:** Implemented; runtime/browser verification limited  
**Owner:** Builder stage, reviewed separately using the checklist below

## Goal

Produce a small, credible landing page for a fictional gardening journal that demonstrates the documented Agent-Team pipeline from research through handoff.

## Scope

- One responsive static HTML file with embedded CSS.
- Hero, feature summary, three-step workflow, and final in-page CTA.
- Semantic landmarks, descriptive link text, keyboard-visible focus, reduced-motion respect, and a mobile viewport.
- Evidence log, design brief, decision record, sanitized run log, review report, and handoff notes.

## Non-goals

- No signup, backend, email collection, analytics, tracking, remote assets, third-party libraries, deployment, pricing claims, or real product promises.
- No claim of WCAG conformance or measured performance without appropriate testing.

## Implementation sequence

1. Read canonical policy, workflow, research protocol, web standards, and run-log contract.
2. Research only source pages actually opened; map each design-relevant claim to evidence and cross-check with an independent source where practical.
3. Record assumptions and design choices before building.
4. Implement one self-contained HTML document with responsive CSS.
5. Review source for semantics, navigation, responsive layout, reduced motion, external dependencies, unsupported claims, and scope drift.
6. Produce a handoff with exact run instructions and verification status.

## Acceptance checklist

- [x] The six workflow stages are documented in order: research → plan → design brief → build → review → handoff.
- [x] Source evidence records URL, title/publisher, access date, claim supported, confidence, cross-check, and limitations.
- [x] Decisions and run activity are recorded without secrets or personal data.
- [x] Page is dependency-free and can be opened locally.
- [x] HTML includes language, viewport, title, navigation, main content, and section headings.
- [x] Responsive CSS, visible focus, and reduced-motion handling are present in source.
- [ ] Browser/device rendering and manual accessibility checks executed — **UNVERIFIED** in this environment.
- [ ] Performance and WCAG conformance measured — **UNVERIFIED**; no conformance claim is made.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Research is mistaken for a usability test | State that sources inform design choices only; no user research was conducted. |
| Static source is mistaken for runtime proof | Keep browser checks marked UNVERIFIED until executed. |
| Demo copy is mistaken for a real commercial offer | Label product and copy as fictional. |
| External asset/license uncertainty | Use original text and CSS shapes only; no remote or third-party assets. |
| A role document is mistaken for an executing agent | State that one sequential assistant session authored the artifacts; no independent subagents were launched. |
