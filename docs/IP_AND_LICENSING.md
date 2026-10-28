# Intellectual Property and Licensing Checks

**This is not legal advice.** Law, licences, contracts, and platform policies vary by jurisdiction, asset, use, and time. Escalate material uncertainty to qualified counsel or the rights holder.

## Dependencies and code
- Inventory direct/transitive dependencies, versions, source, licence identifiers/files, notices, and attribution obligations using lockfiles, package metadata, and SBOM tools where available.
- Read actual licence text and notices, not only registry badges or summaries. Record source URL, version, access date, and exceptions.
- Review intended distribution/modification, notice preservation, source-disclosure, patent, network/service, and attribution conditions as applicable. Compatibility is context-specific; do not claim it without a documented basis.
- Track security advisories and get approval for new licence obligations. Missing/unclear licence information is **UNVERIFIED** and blocks release until resolved.
- Preserve required copyright notices, licence text, and NOTICE files in distributed artifacts.

## Assets and copied material
- For images, fonts, icons, video, datasets, snippets and other assets record creator/rights holder, source URL/ID, access date, licence/terms, permitted uses, modification rules, required attribution, and permission evidence.
- Verify the licence covers the actual use: commercial/noncommercial, modification, redistribution, embedding, print/app/web, and transfer/sublicensing where relevant.
- Public availability, search indexing, payment, attribution, or AI generation does not by itself establish permission.
- Use original work, verified appropriately licensed material, or documented permission. If rights are unclear, replace the item or pause release.
- Do not copy substantial copyrighted text, source code, artwork, or distinctive assets without permission or a documented legal basis. Prefer original implementation and paraphrase; keep justified quotations short, exact, attributed, and compliant with applicable terms.

## AI-assisted/generated content
- Review output for protected expression similarity, trademarks, likenesses, confidential input leakage, and provider terms. Record tool/model/provenance where available. Human review does not guarantee clearance.
- Do not claim prompts or outputs are automatically copyrightable, public domain, exclusive, or infringement-free; rules differ by jurisdiction.
- Disclose AI generation/manipulation when required by applicable law, contract, commissioning terms, platform policy, or context. Check current policy for exact platform/content type; use machine-readable marks or visible labels when required. Do not assume every AI output always requires the same disclosure.
- EU AI Act Article 50 establishes transparency obligations for certain interactions and generated/manipulated content with scope, exceptions and actor-specific duties. Check official text/guidance for the specific context, not a blanket rule for every asset.
- Do not submit third-party confidential material to a provider unless authorized.

## Attribution record
For each third-party item record title, creator, source, licence/version, access date, required attribution, modifications, intended use, reviewer, and evidence path. Attribution does not replace permission when permission is required. Keep a credits/NOTICE file when needed.

## Release gate
- [ ] Direct/transitive dependencies and licences reviewed.
- [ ] Notices, attribution, and applicable source-disclosure duties satisfied.
- [ ] Asset permissions cover intended use and distribution.
- [ ] AI/provider terms and disclosure obligations checked for jurisdiction/platform/content type.
- [ ] Similarity, trademark, likeness, privacy, and confidential-input risks reviewed.
- [ ] Unknown rights marked **UNVERIFIED**; pause or replace assets until resolved.
- [ ] Legal review/approval recorded where warranted.

## Research sources (accessed 2026-10-28)
1. GitHub Docs, [Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) — official platform guidance; notes it is not legal advice and does not replace reading the full licence.
2. U.S. Copyright Office, [Copyright and Artificial Intelligence, Part 2: Copyrightability](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) — official U.S. report on human authorship/copyrightability of AI outputs; jurisdiction-specific.
3. European Commission, [AI Act Article 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50) and [FAQ on transparency obligations](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) — official legal text and implementation guidance. The FAQ states Article 50 applies from 2 August 2026 and explains particular duties/exceptions; confirm applicability to the facts and current guidance.

**Evidence limits:** These sources do not decide licence compatibility, infringement, fair use/fair dealing, ownership, or disclosure duties for a specific project. Re-check official terms and applicable law at release.
