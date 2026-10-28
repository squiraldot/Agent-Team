# Deliverable Formats

## Design
- **SVG:** Use for vector-suitable logos/icons. Include viewBox, aspect ratio, descriptive IDs, accessible title/description where meaningful; avoid scripts/external dependencies. Validate XML and render at target sizes. SVG is not automatically editable everywhere.
- **Design tokens:** Versioned JSON, semantic names, separate raw/semantic colors, document aliases/modes. JSON Schema example (Draft 2020-12):
~~~json
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","required":["$schemaVersion","name","tokens"],"properties":{"$schemaVersion":{"type":"string","pattern":"^1\\.0\\.0$"},"name":{"type":"string"},"tokens":{"type":"object"}},"additionalProperties":false}
~~~
This is an envelope example; add project-specific constraints.
- **Naming:** lowercase kebab-case, e.g. brand-mark-primary.svg, design-tokens.json. Avoid final-final and overwriting masters; keep asset/license manifest.
- **Figma handoff:** written spec, not proof a Figma file exists. Use ../templates/handoff-spec.md; document pages, components, variants, tokens, responsive states, focus, motion, accessibility, assets, acceptance. Dev Mode access varies by plan/seat.
- **Brand kit:** use ../templates/brand-kit/README.md; include brief, strategy, logos/source, logos/exports, typography, color, tokens, imagery, templates, guidelines, licenses, handoff, previews.
- **Image brief:** use ../templates/image-brief.md; specify goal, audience, subject, composition, ratio, outputs, reference rights, constraints, checks, provenance. A brief is not an image.

## Content formats
1. **Brief:** objective, audience, channel, voice, locale, CTA, constraints, success measure, approver.
2. **Outline:** audience questions, headings, evidence, order, CTA, gaps.
3. **Draft:** complete copy and citations for facts; uncertainty explicit.
4. **Edit pass:** structure, fact-check, tone, clarity, accessibility, grammar, rights, localization and open issues.
5. **SEO metadata:** title, description, slug, canonical URL if known, topic/search intent, H1, social metadata, alt text; no ranking guarantees.
6. **Multilingual:** source/target locale, glossary, protected terms, local dates/currency/units, adaptation notes, reviewer, approval, parity checklist.

Research/access dates: W3C WCAG https://www.w3.org/WAI/standards-guidelines/wcag/ ; Figma Dev Mode https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode-in-Figma ; Google SEO Starter Guide https://developers.google.com/search/docs/fundamentals/seo-starter-guide . Accessed 2026-10-28; revalidate 2027-01-28. Tool versions/licensing are UNVERIFIED until checked.