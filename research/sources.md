# Source Registry
Registry links are leads, not evidence of access. Open and inspect the source.

## Tiers
1. **Official/primary:** official docs, APIs, specifications, standards, changelogs, policies, release notes, advisories and first-party code. Best for requirements; may lag or be version/region-specific.
2. **Maintainers/issues:** official GitHub/GitLab issues, discussions, PRs, release notes, trackers and maintainer responses. Record status/version/reproducibility; an issue is not a guarantee.
3. **Public communities:** Stack Overflow, Reddit, Hacker News, Dev.to, permitted public forums/Discord, Product Hunt, Behance, Dribbble. Anecdotes and votes do not establish prevalence or correctness.
4. **Blogs/videos:** tutorials, newsletters, podcasts and commentary. Leads only until corroborated; check author, date, sponsorship, primary citations and version.

## Domain lists
### Web
Tier 1: MDN https://developer.mozilla.org/en-US/docs/ ; WHATWG https://html.spec.whatwg.org/ ; W3C https://www.w3.org/TR/ ; web.dev https://web.dev/ ; Google Search Central https://developers.google.com/search/docs ; React https://react.dev/ ; Node https://nodejs.org/docs/ ; TypeScript https://www.typescriptlang.org/docs/.
Tier 2: official framework repos/issues/RFCs/release notes. Tier 3: Stack Overflow, Reddit, Hacker News, Dev.to. Tier 4: tutorials and benchmarks; reproduce performance claims.
### Android
Tier 1: Android Developers https://developer.android.com/ ; AOSP https://source.android.com/ ; Kotlin https://kotlinlang.org/docs/home.html ; Compose https://developer.android.com/compose ; Google Play policy https://support.google.com/googleplay/android-developer/topic/9877466 ; Flutter https://docs.flutter.dev/ ; React Native https://reactnative.dev/docs/getting-started ; Kotlin Multiplatform https://kotlinlang.org/docs/multiplatform.html.
Tier 2: AndroidX/framework repos, issues, release notes, policy announcements. Tier 3: Stack Overflow, Reddit Android/dev communities, public forums. Tier 4: device tutorials/benchmarks; distinguish anecdotes from guarantees.
### Design
Tier 1: W3C/WAI https://www.w3.org/WAI/standards-guidelines/ ; WCAG 2.2 https://www.w3.org/TR/WCAG22/ ; Apple HIG https://developer.apple.com/design/human-interface-guidelines/ ; Material https://m3.material.io/ ; official design systems and type licenses.
Tier 2: design-system issues/accessibility reports/changelogs. Tier 3: Behance https://www.behance.net/ ; Dribbble https://dribbble.com/ ; public UX forums/Reddit. Portfolios are not usability research. Tier 4: design trend commentary; distinguish taste from measured usability.
### Content
Tier 1: platform policies, creator/editorial docs, language authorities, copyright/licensing and primary statements; YouTube API policies https://developers.google.com/youtube/terms/developer-policies.
Tier 2: support forums, policy changelogs, publisher corrections. Tier 3: public creator communities, Reddit, Hacker News, Dev.to. Tier 4: creator blogs/videos/marketing reports; check methodology and incentives.
### AI tools
Tier 1: official APIs, model/system cards, releases, pricing/limits, security/privacy and terms: OpenAI https://developers.openai.com/api/docs/ ; Anthropic https://docs.anthropic.com/ ; Google AI https://ai.google.dev/.
Tier 2: provider repos/issues/changelogs/incidents/status. Tier 3: Hacker News, Reddit, Stack Overflow, Dev.to, permitted public forums/Discord, Product Hunt. Tier 4: roundups/affiliate blogs/demos; verify capability, privacy and pricing directly.

## Staleness thresholds
| Domain | Re-check after | Immediate trigger |
|---|---:|---|
| Web APIs/frameworks/packages/browser | 90 days | release, deprecation, security advisory |
| SEO/search guidance | 90 days | policy/algorithm announcement or current ranking claim |
| Android SDK/Play policy/permissions | 60 days | deadline, target API requirement, security bulletin |
| Design/accessibility/type licenses | 180 days | standard/license revision or critical defect |
| Content policies/copyright/monetization | 30 days | policy or jurisdiction change |
| AI models/APIs/pricing/limits | 30 days | release, terms/pricing change, incident |
| Community pain points | 30 days | major release, incident or launch |
| Stable/historical facts | 365 days | credible contradiction |
Thresholds trigger review, not automatic falsity. High-impact claims require primary-source revalidation regardless of threshold. If unavailable, mark **STALE / UNVERIFIED**. Respect ToS, robots.txt, rate limits, copyright, privacy and access controls; never scrape private/paywalled/login-gated/restricted content or collect community-member personal data. Registry references checked 2026-10-28; see docs/RESEARCH.md.
