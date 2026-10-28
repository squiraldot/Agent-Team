# Upgrade Progress

## Phase checklist

- [x] Phase 1 — Audit.
- [x] Phase 2 — Core roles and handoff protocol.
- [x] Phase 3 — Domain roles and specialist contracts.
- [x] Phase 4 — Research protocol, sources, logs, and templates.
- [x] Phase 5 — Workflow stages, pipelines, and handoffs.
- [x] Phase 6 — Runtime adapters and drift checks.
- [x] Phase 7 — Skills, templates, extension guide, and indexes.
- [x] Phase 8 — Quality gates, evals, security, validator, and tests.
- [x] Phase 9 — Routing, tools, and observability.
- [x] Phase 10 — Development-domain standards.
- [x] Phase 11 — Design/content standards, deliverable contracts, templates, role/pipeline links, and indexes.
- [ ] Phase 12 — Governance.
- [ ] Phase 13 — Demo and final report.

## Phase 11 changes

- Expanded `docs/standards/ui-ux.md`, `graphic-branding.md`, `illustration.md`, and `content.md` with principles, repeatable process, quality checklist, pitfalls, dated research sources, and explicit **UNVERIFIED** limitations.
- Expanded `docs/DELIVERABLE_FORMATS.md` to specify SVG assets, a JSON Schema design-token example, naming conventions, Figma-ready handoff, brand-kit folder layout, image brief, and content stages: brief, outline, draft, edit pass, SEO metadata, and multilingual versions.
- Updated `templates/handoff-spec.md`, `templates/image-brief.md`, and `templates/brand-kit/README.md`.
- Linked standards from matching canonical roles and the UI/UX design sprint, brand identity, and content campaign pipelines. Updated root/docs/standards indexes.
- Followed `research/PROTOCOL.md`. W3C, Google Search Central, and Figma sources accessed 2026-10-28. The OpenAI image-generation help page was not opened in this research pass and is marked UNVERIFIED. No project-specific usability results, licences, or trademark clearance are claimed.
- **Validation limitation:** this GitHub-file interface has no repository checkout or shell. I could not execute `python scripts/validate_repo.py` or `python -m unittest discover -s tests -v` in this session; these are **not claimed as passed**. The repository's existing index/link checks and Phase 11 unit-test assertions remain the intended gates for local/CI execution.
- Phase 12 was not started.

## Phase 10 changes

- Added `docs/standards/README.md` and the web, Android, plugins/modules, and software engineering standards, including stacks, conventions, structure, testing, security, accessibility/performance where relevant, release checks, pitfalls, source access dates, and unverified items.
- Followed `research/PROTOCOL.md`; official MDN, Chrome for Developers, Android Developers/Google Play, WordPress Developer Resources, Python/GitHub docs, and OWASP sources were consulted. Volatile policy claims are marked for rechecking.
- Linked standards from matching domain roles and relevant build/fix pipelines; updated indexes and repository index tests.
- Verification limitation at that time: validator and full unit tests could not run in the GitHub-file-only session. No local pass was claimed.

## Earlier phases

See the phase-specific repository files and commit history for implementation details. Historical validation notes apply only to their original execution contexts.
