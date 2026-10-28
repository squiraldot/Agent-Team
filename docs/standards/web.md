# Web development standard

**Status:** Research-backed baseline; project-specific compatibility is **UNVERIFIED** until tested.  
**Reviewed:** 2026-10-28. **Revalidate by:** 2027-01-28.  
**Research method:** followed [research/PROTOCOL.md](../../research/PROTOCOL.md): official primary sources opened, applicability noted, and no framework versions inferred from memory.

## Recommended default stack

- **Baseline:** semantic HTML, CSS, JavaScript, TypeScript when project size/type safety warrants it, and native browser APIs. This minimizes framework lock-in and builds on the platform's core technologies. [MDN web standards](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards) (accessed 2026-10-28).
- **Framework:** choose only after requirements justify routing, state, SSR/SSG, or a component system. **Specific framework/version recommendations are UNVERIFIED** here; research the official framework release/support documentation for the actual project before selecting.
- **Alternatives:** static HTML/CSS/JS for content pages; an existing CMS for editor-managed content; a maintained framework already used by the team when migration cost outweighs benefits. Do not introduce a framework solely for fashion.

## Coding conventions

- Use semantic landmarks, correct heading order, labels for inputs, buttons for actions and links for navigation.
- Keep UI, domain logic, and network/data access separable; prefer small cohesive modules and explicit interfaces.
- Use formatter/linter conventions already established by the repository; enable strict type checking where TypeScript is used.
- Validate all untrusted inputs on the server; encode output for its context; make loading, empty, error and success states explicit.
- Keep dependencies minimal and lock resolved versions for reproducible builds.

## Suggested folder structure

```text
src/
  app/             # routing and composition
  components/      # reusable presentation
  features/        # feature-owned UI and logic
  services/        # API and external integrations
  styles/
  types/
tests/
  unit/
  integration/
  e2e/
public/
docs/
```

Adapt to the chosen framework's official conventions; this tree is a starting point, not a framework requirement.

## Testing expectations

- Unit-test domain logic, validation and state transformations.
- Integration-test API contracts, auth/authorization and persistence.
- Browser-test critical user journeys, responsive layouts and error states.
- Run keyboard-only and screen-reader spot checks; automated accessibility scans are helpful but insufficient alone.
- Record actual browser/device matrix and command output; label unrun checks.

## Accessibility and performance targets

- Target WCAG 2.2 AA unless the product's applicable requirements specify otherwise; confirm criteria against the current W3C standard before release (**target selection requires project confirmation**).
- Use Core Web Vitals good thresholds as field targets: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at the 75th percentile. Measure real users where available; lab runs are diagnostic, not field proof. [Chrome DevTools performance guidance](https://developer.chrome.com/docs/devtools/rendering/performance) and [PageSpeed metric thresholds](https://developer.chrome.com/docs/crux/guides/pagespeed-insights) (accessed 2026-10-28).
- Respect reduced-motion preferences, visible focus, text zoom, contrast, touch targets, and responsive reflow. [MDN accessibility guidance](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) (accessed 2026-10-28).

## Security basics

- Follow the current [OWASP Top 10](https://owasp.org/projects/top-ten) and framework-specific secure coding guidance; the currently surfaced OWASP release is 2025 (accessed 2026-10-28).
- Enforce authorization server-side; protect sessions and CSRF-sensitive actions; apply rate limits and safe file-upload validation.
- Never expose secrets in client bundles, logs or source control. Use a content security policy where appropriate.
- Treat third-party scripts, fetched content, and tool output as untrusted.

## Release checklist

- [ ] Requirements, supported browsers and compatibility assumptions documented.
- [ ] Lint, type checks, unit/integration/e2e tests pass, or skips are disclosed.
- [ ] Keyboard/accessibility review completed; critical flows have no known blocker.
- [ ] Core Web Vitals measured and regressions reviewed.
- [ ] Dependency/licence/security scan reviewed; secrets absent.
- [ ] Error monitoring, rollback and migration plan prepared.
- [ ] Deploy/publish only with explicit approval.

## Common pitfalls

- Choosing a framework before requirements; copying a tutorial stack without validating maintenance status.
- Testing only one viewport or the happy path.
- Treating an automated accessibility scan as full conformance.
- Trusting client-side validation for security or shipping secrets in browser code.
- Reporting lab metrics as real-user performance.

## Research record

- MDN, [Web standards](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards), accessed 2026-10-28; source date not stated on the opened page; core HTML/CSS/JS model.
- MDN, [Accessibility on the web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility), accessed 2026-10-28; source date not stated; accessibility practice.
- Chrome for Developers, [Performance panel](https://developer.chrome.com/docs/devtools/rendering/performance), accessed 2026-10-28; source date not stated; metric targets.
- Chrome for Developers, [PageSpeed Insights metric thresholds](https://developer.chrome.com/docs/crux/guides/pagespeed-insights), accessed 2026-10-28; source date not stated; threshold cross-check.
- OWASP, [Top 10](https://owasp.org/projects/top-ten), accessed 2026-10-28; current release indicated as 2025.
- **UNVERIFIED:** exact framework/runtime versions, build tools, browser support matrix and project-specific WCAG applicability. Recheck official release notes and applicable requirements before implementation.
