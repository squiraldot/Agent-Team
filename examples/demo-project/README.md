# SproutLog landing-page demo

A small, dependency-free static landing page used as the Phase 13 proof of work for Agent-Team. SproutLog is a fictional gardening-journal product; the feature copy below is demo content, not market evidence.

## Open the demo

Open [index.html](index.html) directly in a modern browser. It uses local HTML/CSS only; no package install, build step, external font, image, analytics, API, or network request is needed.

## Pipeline and artifacts

1. **Research** — [evidence-log.md](evidence-log.md) records sources actually opened on 2026-10-28, claim-level support, cross-checks, confidence, and gaps.
2. **Plan** — [plan.md](plan.md) defines scope, sequence, acceptance checks, and risk.
3. **Design brief** — [design-brief.md](design-brief.md) defines audience, content hierarchy, tone, visual system, accessibility, and responsive behavior.
4. **Build** — [index.html](index.html) is the runnable landing page.
5. **Review** — [reviewer-report.md](reviewer-report.md) records source-level findings and checks that could not be executed.
6. **Handoff** — [handoff.md](handoff.md) records how to run it, deliverables, status, and limitations.

Supporting records: [decision records](decisions.md) and [run log](run-log.json).

## Verification status

The page source is inspectable and has no external runtime dependencies. The repository-level validator and unit tests are the authoritative automated checks. Browser rendering, keyboard/screen-reader checks, and automated accessibility audits are **UNVERIFIED** unless explicitly reported as run in the final upgrade report. This demo is evidence of a documented end-to-end workflow, not proof that Agent-Team launches independent agents or orchestrates these stages automatically.
