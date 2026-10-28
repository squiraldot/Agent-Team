# Design brief — SproutLog

## Product and audience

SproutLog is a fictional personal gardening journal for beginners who want to remember watering, track plant growth, and build a simple routine. Primary audience: people tending a few indoor or balcony plants and using a phone as their main device.

## User need and primary action

**Need:** “Help me keep plant-care notes without making gardening feel complicated.”  
**Primary action:** explore the simple three-step workflow through an in-page link. No signup or data collection is implemented.

## Message hierarchy

1. **Headline:** Make room for greener days.
2. **Supporting message:** A calm place to keep plant notes, care reminders, and small wins together.
3. **Benefits:** keep plant notes together, remember simple care tasks, notice growth over time.
4. **How it works:** add a plant, note a care task, look back at progress.
5. **CTA:** “See how it works” — navigates to an on-page section and does not imply an external action.

All features are fictional demo copy, not factual claims about an existing product.

## Visual direction

- Calm botanical palette: deep forest, leaf green, warm cream, muted sage.
- Editorial headline with system fonts; no externally hosted font.
- Generous whitespace, rounded cards, clear contrast, restrained decoration.
- Use CSS-drawn plant-like geometry instead of stock imagery or unlicensed assets.
- Mobile-first layout; card columns collapse naturally on narrow screens.

## Accessibility and interaction

- Use semantic header, nav, main, section, and footer landmarks with one primary heading.
- Keep links descriptive and keyboard-operable; show a visible focus outline with :focus-visible.
- Avoid conveying meaning through color alone; maintain readable text and adequate contrast as a design intention, not a measured conformance claim.
- Set document language and viewport; use responsive layout and allow text to reflow.
- Respect prefers-reduced-motion; no essential content depends on animation.
- Do not use fake controls, inaccessible click handlers, or a form that collects data.

## Content constraints

- No fabricated testimonials, user counts, guarantees, pricing, medical/safety claims, or market statistics.
- No external assets, tracking, APIs, or third-party dependencies.
- Browser compatibility, contrast ratios, and WCAG conformance remain unverified until tested.
