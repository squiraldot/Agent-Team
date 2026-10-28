# Plugin / module build pipeline

**Use for:** WordPress plugins, editor/browser extensions, libraries, packages, and other installable modules.

## Ordered roles and handoffs

1. **Orchestrator** — [agents/orchestrator/role.md](../agents/orchestrator/role.md): host/runtime, audience, permission boundary, distribution and risk brief.
2. **Planner** — [agents/planner/role.md](../agents/planner/role.md): API contract, compatibility targets, module boundaries, packaging, tests and rollback plan.
3. **Deep Researcher** — [agents/deep-researcher/role.md](../agents/deep-researcher/role.md) + [Plugin/Module Developer](../agents/plugin-module-developer/role.md): official host API, security policy, manifest/schema and supported versions; pass evidence log.
4. **Plugin/Module Developer** — [agents/plugin-module-developer/role.md](../agents/plugin-module-developer/role.md): implement minimal increments with explicit interfaces and least privilege; pass source, manifest, install/update/uninstall notes and tests.
5. **QA/Reviewer** — [agents/qa-reviewer/role.md](../agents/qa-reviewer/role.md): independent API, packaging, compatibility, regression and acceptance review.
6. **Security & Privacy Reviewer** — [agents/security-privacy-reviewer/role.md](../agents/security-privacy-reviewer/role.md): mandatory when permissions, remote code, credentials, user data, admin actions or privileged hooks are involved.
7. **Plugin/Module Developer / Builder** — fix findings, run unit, package, lint and host-specific checks; document tested versions and known limitations.
8. **Orchestrator** — handoff package artifact/source, installation and rollback steps, exact checks, compatibility evidence and release approval status.

## Development standard

Apply [Plugins and modules standard](../docs/standards/plugins-modules.md), selected for the actual host and distribution channel.

## Quality gates

- Manifest and host metadata validate; permissions are minimal and explained.
- Public interfaces, dependency/license obligations, data migration and uninstall behavior are documented.
- Test exact supported host/runtime versions where possible; unsupported versions are clearly labelled unverified.
- Do not publish packages or deploy to a marketplace without explicit human approval.

## Parallelizable work

Research host API constraints independently from test-matrix drafting. Implementation tasks may parallelize only across isolated modules with agreed interfaces and non-overlapping ownership.
