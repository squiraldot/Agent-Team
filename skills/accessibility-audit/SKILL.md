---
name: accessibility-audit
description: Evaluate digital experiences against a stated accessibility target using reproducible manual and automated checks.
version: 1.0.0
owner: Agent-Team maintainers
status: active
---

# Accessibility Audit

## Trigger conditions
Trigger when auditing a website/app, before a release, after major UI changes, or when accessibility defects are reported.

## Steps
1. Define product surfaces, representative journeys, platforms, assistive technologies, and target standard/version.
2. Review current normative guidance and record scope; do not equate an automated score with conformance.
3. Run available automated checks, then manually test keyboard order, focus visibility, semantics, labels, errors, contrast, zoom/reflow, motion, and media alternatives.
4. Test critical journeys with screen readers and real controls where feasible.
5. Record each issue with affected URL/screen, steps, expected/actual result, impact, and suggested fix.
6. Prioritize blockers and barriers; validate fixes and regression-test related components.
7. State sample coverage, untested surfaces, and residual uncertainty.

## Checklist
- [ ] Target standard/version and scope stated
- [ ] Automated and manual checks performed
- [ ] Keyboard and screen-reader paths sampled
- [ ] Contrast, zoom, focus, forms, and media checked
- [ ] Issues are reproducible and prioritized
- [ ] Fixes re-tested; limitations disclosed

## Failure modes
Automated-only audit: report as partial, never compliant. Missing assistive technology/device: disclose coverage gap. Fundamental barriers on critical paths: recommend blocking release until mitigated.

## Related canonical guidance
- Shared policy: [AGENTS.md](../../AGENTS.md)
- Research standards: [docs/RESEARCH.md](../../docs/RESEARCH.md)
- Extending this framework: [docs/EXTENDING.md](../../docs/EXTENDING.md)
