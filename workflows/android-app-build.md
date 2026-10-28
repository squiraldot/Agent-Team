# Android app build pipeline

**Use for:** native Android or cross-platform app work where Android is a target.

## Ordered roles and handoffs

1. **Orchestrator** — [agents/orchestrator/role.md](../agents/orchestrator/role.md): brief, target devices/OS, distribution plan, permissions and risk.
2. **Planner** — [agents/planner/role.md](../agents/planner/role.md): feature slices, architecture, data/lifecycle plan, acceptance and device test matrix.
3. **Deep Researcher** — [agents/deep-researcher/role.md](../agents/deep-researcher/role.md) + [Android Developer](../agents/android-developer/role.md): official Android/API, SDK, library, target-SDK and distribution requirements with dates/versions.
4. **UI/UX Designer** — [agents/ui-ux-designer/role.md](../agents/ui-ux-designer/role.md): navigation, screen states, accessibility, adaptive layouts and interaction specs.
5. **Android Developer** — [agents/android-developer/role.md](../agents/android-developer/role.md): implement small increments; pass source diff, build config, data/permission rationale, tests and run steps.
6. **QA/Reviewer** — [agents/qa-reviewer/role.md](../agents/qa-reviewer/role.md): independent functional, lifecycle, regression and acceptance review.
7. **Security & Privacy Reviewer** — [agents/security-privacy-reviewer/role.md](../agents/security-privacy-reviewer/role.md): review auth, permissions, local/cloud data, network, exported components and secrets.
8. **Android Developer / Builder** — fix findings, run unit/instrumented/build checks available, inspect logs and update setup/release notes.
9. **Orchestrator** — handoff build/test evidence, supported OS/device scope, untested paths, signing/distribution caveats and approval requests.

## Quality gates

- SDK/toolchain and library versions are explicit; no compatibility claim without a tested version/device matrix.
- Permission requests are least-privilege and explained; data persistence, offline/error behavior and lifecycle transitions are covered.
- Build and unit tests run when tooling exists; emulator/physical-device tests are identified separately.
- Signing keys, keystores, tokens and user data are never committed. Store/release/signing/publishing require human approval.

## Parallelizable work

Researcher can verify platform requirements while Designer drafts flows; QA can draft test cases while architecture is planned. Do not parallel-edit Gradle/build files or shared navigation/state modules. Only claim device coverage that was actually tested.
