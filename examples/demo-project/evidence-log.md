# Evidence log — SproutLog demo

**Question:** Which lightweight web-design choices are supported by accessible standards and technical guidance for a small static landing page?  
**Research access date:** 2026-10-28  
**Scope:** HTML/CSS landing page; no framework/runtime compatibility or user-outcome claim.

## Claim-level evidence

### E1 — Responsive layout should accommodate varied viewport sizes

- **Source:** “Responsive web design,” MDN Web Docs.
- **URL:** https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
- **Tier:** 1 (technical documentation; secondary explanation of web platform behavior).
- **Access date:** 2026-10-28; publication/update date: not recorded from the opened page.
- **Observed support:** MDN describes responsive web design as making pages render well across screen sizes/resolutions and calls out fluid layout, media queries, responsive typography, and the viewport meta tag.
- **Use in demo:** Include the viewport meta tag, flexible layout, and a narrow-screen CSS breakpoint.
- **Confidence:** Medium — source opened and directly supports the implementation direction; no device rendering was executed.

### E2 — Reflow and keyboard operability are relevant accessibility checks

- **Source:** W3C Web Accessibility Initiative, “How to Meet WCAG (Quickref Reference).”
- **URL:** https://www.w3.org/WAI/WCAG22/quickref/
- **Tier:** 1 (standards organization / WCAG criteria reference).
- **Access date:** 2026-10-28; page date: not stated in the opened view.
- **Observed support:** The quick reference lists WCAG criteria including Reflow (1.4.10), Keyboard (2.1.1), Focus Visible (2.4.7), and Link Purpose (2.4.4).
- **Use in demo:** Provide responsive reflow, ordinary anchors, descriptive link text, and visible keyboard focus as implementation intentions.
- **Confidence:** Medium — primary criteria were opened; this is not a completed conformance audit.

### E3 — Link text should communicate destination and anchors support keyboard activation

- **Source:** “<a> HTML anchor element,” MDN Web Docs.
- **URL:** https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a
- **Tier:** 1 (technical documentation; secondary explanation of HTML semantics).
- **Access date:** 2026-10-28; publication/update date: not recorded from the opened page.
- **Observed support:** MDN states that link content should indicate its destination and that an anchor with href activates with Enter when focused.
- **Use in demo:** Use a normal in-page anchor with meaningful text instead of a fake button or click-only element.
- **Confidence:** Medium — source opened; keyboard behavior and assistive-technology output were not manually tested.

## Cross-check and conflicts

- **Responsive reflow:** MDN's responsive-design guide (E1) explains varied screen sizes and responsive layout; W3C's WCAG quick reference (E2) separately lists the Reflow criterion. These sources support the design direction from different roles: practical implementation guidance and normative accessibility criteria. They do not prove this page passes either source's recommendations.
- **Link behavior:** MDN's anchor reference (E3) explains destination-indicating link content and keyboard activation; W3C's Link Purpose and Keyboard criteria (E2) provide an independent standards cross-check. The page uses semantic anchors, but no manual keyboard audit was run.
- **No material contradiction found** within the narrow claims checked. This is not an exhaustive literature review.

## Unverified items and evidence limits

- **UNVERIFIED:** actual browser rendering, keyboard sequence, screen-reader announcements, contrast ratios, browser/device matrix, automated accessibility score, load/performance metrics, and WCAG conformance.
- No users were interviewed and no conversion or product-market claim was researched.
- Sources were opened in this session; only claims summarized above are attributed to them. URLs in the broader repository source registry are not treated as accessed evidence for this demo.
- Confidence is Medium for design rationale and Unverified for actual conformance/runtime behavior.
