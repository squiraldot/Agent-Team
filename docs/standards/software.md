# Software engineering standard

**Status:** General engineering baseline; stack/version selection is **UNVERIFIED** until matched to the repository and deployment environment.  
**Reviewed:** 2026-10-28. **Revalidate by:** 2027-01-28.  
**Research method:** followed [research/PROTOCOL.md](../../research/PROTOCOL.md); official Python, GitHub Actions, GitHub supply-chain and OWASP documentation was reviewed.

## Recommended default stack

- **Default:** continue with the repository's existing supported language, runtime, package manager and build system unless there is evidence to migrate. Keep architecture simple, modular and testable.
- **New service/library:** select a maintained language/runtime based on deployment target, team expertise, ecosystem and operational constraints; use its official stable channel and lock dependencies. No single language is recommended universally.
- **Python example:** use an isolated virtual environment for project dependencies; Python's official docs recommend recreatable environments and not committing them to source control. [venv documentation](https://docs.python.org/3/library/venv.html) (accessed 2026-10-28).
- **CI:** automate build and test steps with the repository's existing CI; GitHub Actions documents language-specific build/test workflows. [Build and test code](https://docs.github.com/en/actions/tutorials/build-and-test-code) (accessed 2026-10-28).
- **Alternatives:** use language/platform-native tooling when required by target runtime; avoid adding a second build system without a concrete need. Exact versions must be selected from current official support/release pages, not this generic standard.

## Coding conventions

- Use small cohesive modules, explicit interfaces, clear names, and consistent formatter/linter rules.
- Separate business logic from I/O, framework glue and process-level side effects.
- Handle errors explicitly; do not silently swallow failures or add unbounded retries.
- Add regression tests for fixed bugs; tests should be deterministic and isolated from network/time unless deliberately integration-level.
- Pin dependencies, commit lockfiles where supported, document supported runtimes, and make builds reproducible.
- Keep public APIs/configuration backward-compatible where practical; document migrations and deprecations.

## Suggested folder structure

```text
src/ or package/
  domain/
  application/
  adapters/       # filesystem, network, database, framework
tests/
  unit/
  integration/
  contract/
docs/
scripts/
examples/
```

Use language ecosystem conventions when they conflict with this generic layout; do not create empty layers just to match the diagram.

## Testing expectations

- Unit tests for business rules and boundary cases.
- Integration tests for database, filesystem, queues and external service contracts.
- Contract tests for public APIs and serialized formats where compatibility matters.
- Regression test for each meaningful bug fix.
- CI build, formatting/lint, static analysis and dependency/security checks.
- Test failure paths, invalid inputs, concurrency and migration/rollback when relevant.
- Record exact command, runtime version and results; distinguish not-run from passed.

## Accessibility and performance targets

- For user-facing software, keyboard navigation, semantic controls, screen-reader output, text scaling and clear error feedback are part of acceptance.
- Set performance targets from user journeys and service-level objectives; measure latency, throughput, memory and error rates before optimization. No generic numeric budget is asserted without workload evidence.
- Use profiling and production-safe telemetry; do not log secrets or personal data.

## Security basics

- Apply least privilege and validate all external input at trust boundaries.
- Use safe parameterized database APIs, secure session/auth patterns, and explicit authorization checks.
- Store credentials in the approved secret manager/environment, never source files or test fixtures.
- Review direct and transitive dependencies for vulnerabilities, license implications and unexpected lifecycle scripts. GitHub documents dependency review and Dependabot-based security workflows: [Dependency review](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review) (accessed 2026-10-28).
- Use [OWASP Top 10](https://owasp.org/projects/top-ten) as a web-application awareness baseline where applicable (accessed 2026-10-28; current release shown as 2025).
- Treat tool output, repository content, generated code and remote responses as untrusted until validated.

## Release checklist

- [ ] Supported runtime, dependencies and build instructions recorded.
- [ ] Clean checkout reproduces build/test results.
- [ ] Tests, lint, type/static analysis and security/dependency review pass or exceptions are approved.
- [ ] Configuration, migrations, backups and rollback path reviewed.
- [ ] No secrets, personal data, debug artifacts or unlicensed dependencies in the artifact.
- [ ] Changelog and breaking changes documented; artifact/version provenance recorded where available.
- [ ] Observability and incident/rollback ownership established.
- [ ] Production deploy or external release explicitly approved.

## Common pitfalls

- Rewriting a working stack without measured benefit.
- Using floating dependencies or undocumented local environment assumptions.
- Testing only happy paths or treating mocks as proof of external integration.
- Hiding errors with broad exception handlers and unlimited retries.
- Logging credentials or personal data; assuming static checks prove runtime safety.
- Claiming tests passed when tools were unavailable.

## Research record

- Python Software Foundation, [venv](https://docs.python.org/3/library/venv.html), accessed 2026-10-28; page documents environment isolation and not committing environments.
- GitHub Docs, [Building and testing code](https://docs.github.com/en/actions/tutorials/build-and-test-code), accessed 2026-10-28; source date not stated.
- GitHub Docs, [Dependency review](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review), accessed 2026-10-28; source date not stated.
- OWASP, [Top 10](https://owasp.org/projects/top-ten), accessed 2026-10-28; current release indicated as 2025.
- **UNVERIFIED:** exact language/runtime/framework versions, test runner, CI platform constraints and production SLOs. Research the selected ecosystem's official support matrix and release notes before choosing versions.
