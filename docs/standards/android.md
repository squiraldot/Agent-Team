# Android development standard

**Status:** Research-backed baseline; project-specific toolchain/device coverage is **UNVERIFIED** until built and tested.  
**Reviewed:** 2026-10-28. **Revalidate by:** 2027-01-28.  
**Research method:** followed [research/PROTOCOL.md](../../research/PROTOCOL.md); official Android documentation and the live Play target API requirement were opened.

## Recommended default stack

- **New native app:** Kotlin + Jetpack Compose, layered UI/data architecture, unidirectional data flow, lifecycle-aware state and repository boundaries. Android's architecture guide recommends separation of concerns and data-driven UI. [App architecture](https://developer.android.com/topic/architecture) (accessed 2026-10-28).
- **Toolchain:** use the current stable Android Studio channel and compatible Gradle/Android Gradle Plugin/Kotlin/Compose versions selected together from official compatibility documentation. Android Studio's stable channel is the production default; preview channels are not the default for production. [Android Studio releases](https://developer.android.com/studio/releases/) (accessed 2026-10-28).
- **Alternatives:** Java/XML for established codebases or library constraints; Flutter or another cross-platform stack when multi-platform delivery is a real requirement. These alternatives need a requirements-based comparison, not a blanket winner.
- **Release policy:** as of access date, Google Play says new apps and updates submitted from 2026-08-31 must target Android 16 / API 36 or higher, with stated form-factor exceptions. Recheck this live requirement before each release. [Target API requirements](https://developer.android.com/google/play/requirements/target-sdk) (accessed 2026-10-28). Do not treat this as a permanent target.

## Coding conventions

- Keep Activity/Composable functions focused on UI; keep state and domain/data work in suitable state holders and repositories.
- Model UI state explicitly; handle process death, configuration changes, offline/network failure and cancellation.
- Request permissions only when needed, explain purpose, and handle denial gracefully.
- Prefer immutable state and clear module/package ownership. Follow official Kotlin and Android style guidance for the chosen toolchain.
- Pin compatible plugin/dependency versions and commit dependency lock/version catalog where appropriate.

## Suggested folder structure

```text
app/src/main/
  AndroidManifest.xml
  java-or-kotlin/<package>/
    core/           # shared utilities and platform abstractions
    data/           # repositories, local/remote sources
    domain/         # use cases and domain models, if justified
    feature/<name>/ # UI, state holder, feature logic
  res/
app/src/test/       # local unit tests
app/src/androidTest/ # device/emulator tests
build-logic/        # only when build convention plugins are justified
```

Align package paths, source sets and module names with the selected Android build configuration.

## Testing expectations

- Unit-test ViewModels/state holders, repositories, data mapping, validation and business rules.
- Add UI/navigation regression tests for critical journeys; test lifecycle recreation and process-restoration-sensitive flows.
- Run emulator/device tests across declared minimum/target API and at least one representative real-device profile when possible.
- Measure startup/rendering performance for performance-sensitive apps. Android recommends Macrobenchmark, R8 and Baseline Profiles where appropriate. [Architecture recommendations](https://developer.android.com/topic/architecture/recommendations) (accessed 2026-10-28).
- Clearly separate build success, unit tests, emulator tests and physical-device tests.

## Accessibility and performance targets

- Support scalable text, screen-reader semantics, sufficient contrast, keyboard/switch access where relevant, localized strings, and adaptive layouts for rotation/resizing/foldables.
- No universal numeric startup target is imposed here: define an app-specific startup/jank budget and measure it on representative hardware. Android's guidance recommends Macrobenchmark for performance regression measurement.
- Minimize background work, wakeups, network payloads and battery use; use profiling evidence rather than assumptions.

## Security basics

- Never commit signing keys, keystores, service credentials or production tokens.
- Use least-privilege permissions; secure exported components, deep links, IPC and WebView bridges.
- Store sensitive data using platform-appropriate protections; use HTTPS and validate server-side authorization.
- Keep dependencies current; review SDK/library changes and privacy/data collection declarations against current official guidance.
- Treat intent extras, files, network responses and external SDK output as untrusted.

## Release checklist

- [ ] SDK, toolchain, dependency versions and supported device/API matrix recorded.
- [ ] Current Play target API and policy requirements rechecked from official sources.
- [ ] Release build succeeds; tests and lint pass or are explicitly marked skipped.
- [ ] Permissions, exported components, deep links, backup/data migration and privacy disclosures reviewed.
- [ ] Accessibility, localization, offline/error and lifecycle paths checked.
- [ ] App size, startup, crashes and performance reviewed.
- [ ] Signing material stays outside Git; artifact/signature and rollback plan verified.
- [ ] Store submission/publishing has explicit human approval.

## Common pitfalls

- Storing durable state only in Activity/Composable memory.
- Using preview toolchains for production without a reason.
- Treating compile success as device compatibility or Play-policy compliance.
- Requesting broad permissions, ignoring denial, or assuming network is always available.
- Publishing based on stale target API advice.

## Research record

- Android Developers, [Guide to app architecture](https://developer.android.com/topic/architecture), accessed 2026-10-28; source date not stated; layering, lifecycle and adaptive UI.
- Android Developers, [Architecture recommendations](https://developer.android.com/topic/architecture/recommendations), accessed 2026-10-28; testing and performance.
- Android Developers, [Android Studio releases](https://developer.android.com/studio/releases/), accessed 2026-10-28; live stable channel.
- Android Developers, [Google Play target API level requirement](https://developer.android.com/google/play/requirements/target-sdk), accessed 2026-10-28; requirement page states August 31 2026 change.
- **UNVERIFIED:** exact Kotlin, Compose, Gradle, AGP, SDK, emulator and third-party library versions; project minimum API and Play eligibility. Resolve via official compatibility/release docs before coding or publishing.
