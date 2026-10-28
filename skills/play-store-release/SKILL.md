---
name: play-store-release
description: Prepare an Android app release for Google Play with policy, signing, testing, privacy, and staged-rollout checks.
version: 1.0.0
owner: Agent-Team maintainers
status: active
---

# Play Store Release

## Trigger conditions
Trigger when preparing an Android app bundle, internal/closed/open/production track release, or store listing update.

## Steps
1. Confirm application ID, versionCode/versionName, target SDK, build variant, signing ownership, and release channel.
2. Review current official Play Console policies and Android release requirements; log access date and applicable links.
3. Build a reproducible release AAB; keep keystores and credentials outside Git and CI logs.
4. Run unit, instrumentation, device/API-level, accessibility, crash, and upgrade-path tests appropriate to the app.
5. Audit permissions, Data safety answers, privacy policy, SDK/data collection, content rating, target audience, ads, and declarations.
6. Validate listing assets, localized text, screenshots, support contact, and store metadata.
7. Upload to an appropriate test track, inspect pre-launch reports, then stage rollout with monitoring and rollback criteria.

## Checklist
- [ ] Exact package/version and signing checked
- [ ] Current official policy reviewed
- [ ] AAB and upgrade path tested
- [ ] Permissions/data collection match disclosures
- [ ] Listing and declarations reviewed
- [ ] Test-track report reviewed
- [ ] Rollout and rollback thresholds defined

## Failure modes
Policy interpretation uncertain: do not guess; consult current official guidance. Signing key unavailable: stop and preserve ownership. Crashes, privacy mismatch, or blocking policy issue: do not promote to production.

## Related canonical guidance
- Shared policy: [AGENTS.md](../../AGENTS.md)
- Research standards: [docs/RESEARCH.md](../../docs/RESEARCH.md)
- Extending this framework: [docs/EXTENDING.md](../../docs/EXTENDING.md)
