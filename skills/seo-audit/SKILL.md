---
name: seo-audit
description: Audit technical SEO, content relevance, indexing signals, and measurable search health.
version: 1.0.0
owner: Agent-Team maintainers
status: active
---

# Seo Audit

## Trigger conditions
Trigger when launching/redesigning a website, diagnosing organic-search decline, or reviewing SEO before release.

## Steps
1. Confirm site, target audience, geography, goals, and access limits.
2. Crawl or inspect representative URLs; record scope and crawl date.
3. Review robots/indexability, status codes, canonicals, redirects, sitemap, internal links, mobile usability, performance, structured data, metadata, headings, and content intent.
4. Check official search-engine guidance for consequential/current claims; distinguish observed facts from hypotheses.
5. Prioritize findings by impact, confidence, effort, and dependencies; give reproducible evidence and owners.
6. Re-test fixes on affected URLs and report residual risks.

## Checklist
- [ ] Scope and sample size recorded
- [ ] Indexability and canonical signals checked
- [ ] Content intent and internal links reviewed
- [ ] Findings include URL/evidence/severity/fix
- [ ] No ranking guarantees; assumptions labeled
- [ ] Follow-up measurement defined

## Failure modes
No crawler/search-console access: label coverage partial and request exports. Conflicting signals: capture examples and avoid broad conclusions. Recent algorithm/policy claims without official evidence: mark unverified.

## Related canonical guidance
- Shared policy: [AGENTS.md](../../AGENTS.md)
- Research standards: [docs/RESEARCH.md](../../docs/RESEARCH.md)
- Extending this framework: [docs/EXTENDING.md](../../docs/EXTENDING.md)
