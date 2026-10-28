# Design and Content Deliverable Formats

These are interoperability expectations, not a guarantee that every runtime or tool can create every artifact. Report unsupported capabilities and only list files that exist and were inspected.

## Design

### SVG assets
- Prefer SVG for vector-suitable logos/icons and PNG/WebP/JPEG for raster imagery.
- Use `viewBox`, appropriate dimensions, and meaningful `title`/`desc` for informative standalone assets; embedded UI must provide accessible names appropriately.
- Keep SVG self-contained where practical. Avoid scripts, event handlers, unnecessary filters, external resources, and oversized metadata. Sanitize untrusted SVG before web embedding.
- Include preview, intended background, minimum size, variants, and editable-source status. Validate XML and render in target consumers.
- Naming: `{brand}-{asset}-{variant}-{theme}.{ext}`; examples `brand-logo-primary-color.svg`, `brand-icon-app-dark.png`. Use lowercase kebab-case and avoid ambiguous names like `final-final2`.

### Design tokens — JSON Schema example
This illustrative JSON Schema (Draft 2020-12) validates shape, not contrast or design suitability.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Design Tokens",
  "type": "object",
  "required": ["$schemaVersion", "color", "spacing", "typography"],
  "properties": {
    "$schemaVersion": { "type": "string", "const": "1.0.0" },
    "color": { "type": "object", "additionalProperties": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" } },
    "spacing": { "type": "object", "additionalProperties": { "type": "number", "minimum": 0 } },
    "typography": {
      "type": "object",
      "additionalProperties": {
        "type": "object", "required": ["fontFamily", "fontSize", "lineHeight"],
        "properties": {
          "fontFamily": { "type": "string", "minLength": 1 },
          "fontSize": { "type": "string", "minLength": 1 },
          "lineHeight": { "type": "number", "exclusiveMinimum": 0 }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

Example values:
```json
{
  "$schemaVersion": "1.0.0",
  "color": { "text-primary": "#171717", "surface-canvas": "#FFFFFF", "action-primary": "#65A30D" },
  "spacing": { "space-1": 4, "space-2": 8, "space-3": 12, "space-4": 16 },
  "typography": { "body-md": { "fontFamily": "Inter, sans-serif", "fontSize": "1rem", "lineHeight": 1.5 } }
}
```
Use semantic names in components; extend the schema for aliases, themes, and token groups only with documented rules. These values are examples, not approved brand tokens.

### Naming conventions
- Paths and exported filenames: lowercase kebab-case, ASCII where practical; avoid spaces and ambiguous versions.
- Tokens: semantic roles such as `text-primary`, `surface-canvas`, `action-primary`, not raw color names in consuming UI.
- Components: stable role-based names; represent size/state/theme/platform as explicit variants.
- Include purpose and variant in asset names; version in a manifest unless multiple versions must coexist.
- Use consistent locale tags (for example `en`, `en-IN`, `hi`, `hi-Latn`) and confirm region/script needs.

### Figma-ready handoff
Use [handoff-spec.md](../templates/handoff-spec.md); the spec remains useful if Figma is unavailable. Include:
- File/page/frame URLs or equivalent source location, owner, updated date, revision, and status.
- Frames/components marked ready only after review; platform, viewport, responsive behavior, and relevant states.
- Token source/version, type styles, grid/spacing, breakpoints, component variants, interactions, accessibility expectations, and content assumptions.
- Asset manifest with filename, format, dimensions, background, provenance/licence, and editability.
- Acceptance criteria, known deviations, open questions, reviewers, and change log.
- Dev Mode can aid inspection, but generated CSS/code is not a substitute for implementation judgment and responsive/accessibility QA.

### Brand-kit folder layout
Use [templates/brand-kit/README.md](../templates/brand-kit/README.md) as canonical starter:
```text
brand-kit/
├── README.md
├── brief/ (brand-brief.md, research-log.md)
├── strategy/ (positioning.md, voice-and-messaging.md)
├── identity/
│   ├── logo/{source/, exports/}
│   ├── color/design-tokens.json
│   ├── typography/font-licences.md
│   └── imagery/
├── guidelines/brand-guidelines.md
├── previews/
└── handoff/handoff-spec.md
```
Only include existing files; explicitly mark missing source artwork, rights, or approvals.

### Image-generation brief
Use [templates/image-brief.md](../templates/image-brief.md). Specify goal, audience, placement, subject, composition, ratio/dimensions, palette, style constraints, negative constraints, references/rights, tool/model when known, post-processing, acceptance criteria, and delivery inventory. A brief is not proof that generation occurred.

## Content
1. **Brief:** objective, audience, channel, locale, tone, key message, CTA, constraints, source needs, word/time budget, owner, approver, success criteria.
2. **Outline:** headline/deck, section order and purpose, key points, evidence required, examples, CTA, approximate word/time budget.
3. **Draft:** complete copy/script with headings, source markers, caveats, relevant alt text/caption/transcript needs, and visible placeholders for missing inputs.
4. **Edit pass:** revision summary plus structure, fact-check, voice, clarity, grammar, accessibility, rights, localization, and platform-limit checks; unresolved issues remain explicit.
5. **SEO metadata:** slug, unique title, meta description, H1, canonical URL only if known, social fields, and structured-data suggestions only when justified. Search engines can rewrite titles/snippets; never guarantee rankings or exact display.
6. **Multilingual versions:** source locale, target BCP 47 locale, adaptation approach, glossary, protected terms, preserved variables/links, regional units/dates, reviewer, QA notes, and unresolved ambiguity. Link each version to the approved source.

## Completion manifest
Include artifact path, format, dimensions/word count where relevant, version, status (draft/reviewed/approved), provenance, rights status, checks performed, limitations, and approvals needed. Never claim approved or verified without evidence.
