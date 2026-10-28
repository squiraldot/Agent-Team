# Plugins and modules standard

**Status:** Cross-platform guidance; host-specific requirements are **UNVERIFIED** until the target host and distribution channel are selected.  
**Reviewed:** 2026-10-28. **Revalidate by:** 2027-01-28.  
**Research method:** followed [research/PROTOCOL.md](../../research/PROTOCOL.md), prioritizing official host handbooks and distribution guidance.

## Recommended default stack

- **General module/library:** use the host's supported language, manifest/metadata format, build/package system and public extension API. Avoid private APIs and modifying host core.
- **WordPress plugin:** PHP with WordPress public hooks/APIs and WordPress coding standards; use the official Plugin Handbook for security, privacy and lifecycle practices. [Plugin Handbook](https://developer.wordpress.org/plugins/) and [Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/) (accessed 2026-10-28).
- **Browser extension:** use the target browser's current supported extension manifest/API model. Chrome's migration guidance documents Manifest V3; verify current support and API-specific minimum browser versions before committing to it. [Chrome manifest migration](https://developer.chrome.com/docs/extensions/develop/migrate/manifest) (accessed 2026-10-28).
- **Alternatives:** a standalone service/API, host-native plugin system, or library package may be safer than an extension if the integration surface is unstable. Exact language/runtime/package-manager versions are **UNVERIFIED** until researched for the chosen host.

## Coding conventions

- Define the supported host/runtime range and public API contract before implementation.
- Keep host adapters thin; isolate business logic from host lifecycle callbacks.
- Use namespaced symbols, explicit error handling, stable configuration schemas and backwards-compatible migrations.
- Declare every permission/capability with a user-facing reason; do not request broad access by default.
- Document dependencies, licenses, data flows, uninstall behavior, upgrade behavior and compatibility breaks.
- Follow the host's official style and API conventions rather than imposing one global language standard.

## Suggested folder structure

```text
plugin-or-module/
  manifest-or-plugin-entry
  src/
    host-adapter/
    core/
    services/
  assets/
  tests/
    unit/
    integration/
    host-smoke/
  docs/
  examples/
  package-metadata-and-lockfile
```

Use host-required names/locations where applicable; the sketch is conceptual.

## Testing expectations

- Unit-test pure business logic and schema/input validation.
- Integration-test public host APIs, permissions, event hooks, migration and failure behavior.
- Test install, update, disable, uninstall and rollback on each claimed host/runtime version.
- Validate package contents from a clean install; ensure development files and secrets are not shipped.
- For browser extensions, test permission prompts, content/background boundaries and supported browser versions.
- For WordPress, use a disposable test site and verify capabilities, nonces, escaping, sanitization and upgrade paths.

## Accessibility and performance targets

- UI surfaces should follow the host platform's accessibility conventions, keyboard behavior, semantics and focus order.
- Keep background work, polling, event listeners, injected scripts and network requests minimal.
- Establish host-specific latency/resource budgets when relevant; no universal plugin performance threshold is asserted here (**UNVERIFIED** until host and usage are known).

## Security basics

- Treat every request, stored option, imported file, message, event payload and remote response as untrusted.
- Enforce authorization on every privileged action; validate inputs and contextually escape output.
- Keep secrets out of packages; use least-privilege permissions and secure transport.
- Avoid remote code execution, hidden behavior, obfuscation and undocumented collection. Review dependency licenses and vulnerabilities.
- For WordPress.org distribution, verify the current [Detailed Plugin Guidelines](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/) and applicable license compatibility before submission (accessed 2026-10-28).
- For browser extensions, recheck current browser store policies and permission rules; this document does not assert store eligibility.

## Release checklist

- [ ] Target host, minimum versions and distribution channel explicitly documented.
- [ ] Official API/manifest and store rules checked at release time.
- [ ] Package manifest and artifact contents validated.
- [ ] Unit, integration and host-version smoke tests recorded.
- [ ] Permission rationale, data collection, privacy and license review completed.
- [ ] Upgrade, rollback, disable and uninstall behavior tested.
- [ ] Changelog, compatibility matrix and support instructions updated.
- [ ] Marketplace upload/release approved by a human.

## Common pitfalls

- Editing host core or relying on private/undocumented APIs.
- Requesting broad permissions before proving they are needed.
- Testing only fresh install, not update/uninstall.
- Shipping dev dependencies, secrets, debug endpoints or source maps unintentionally.
- Assuming one store's policy or manifest rules apply to another.

## Research record

- WordPress.org, [Plugin Handbook](https://developer.wordpress.org/plugins/), accessed 2026-10-28; source date not stated; host API/security overview.
- WordPress.org, [Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/), accessed 2026-10-28; source date not stated; coding and accessibility guidance.
- WordPress.org, [Detailed Plugin Guidelines](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/), accessed 2026-10-28; page states last updated 2024-03-15.
- Chrome for Developers, [Update the manifest](https://developer.chrome.com/docs/extensions/develop/migrate/manifest), accessed 2026-10-28; source date not stated; Manifest V3 migration and compatibility note.
- **UNVERIFIED:** host-specific toolchain versions, browser/store policy eligibility, package signing and exact release workflow. Research current official docs for the selected target before implementation/release.
