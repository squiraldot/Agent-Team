# Generic Runtime Adapter Guide

Use this guide for runtimes without a repository-specific adapter, including Windsurf, Aider, Cline, and future tools. Their exact instruction discovery and feature support must be verified against their current official documentation before configuration.

## Canonical policy

1. Keep repository-root `AGENTS.md` as the only shared policy source.
2. If the runtime natively reads `AGENTS.md`, point to it directly; do not create a duplicate policy file.
3. Otherwise, create the smallest supported native entry point that explicitly instructs the runtime to read/import `AGENTS.md`. If it cannot read repository files, inject the canonical file's contents through the runtime's documented mechanism at startup.
4. Keep native syntax, permissions, and feature mapping in the adapter only. Shared behavioral rules stay in `AGENTS.md`; reusable role contracts and workflows stay in `agents/`, `skills/`, `playbooks/`, and `workflows/`.
5. Never assume relative links are automatically loaded. Verify that the runtime actually reads the referenced policy, or configure explicit loading.

## Capability mapping

Document the exact runtime/client/version and map each required capability separately: instruction loading, role/subagent execution, skills, hooks, web/search, file access, shell access, structured output, approval controls, cancellation, and parallel execution. Mark unsupported capabilities explicitly. A prompt that mentions a capability does not implement it.

## Minimal adapter checklist

- Link to the canonical policy and specify precedence when native defaults conflict.
- Preserve the host's own config format; do not paste foreign frontmatter or hook schemas.
- Avoid duplicating canonical rules. If the host requires an embedded prompt, generate it from `AGENTS.md` and record the source digest.
- Enforce least privilege, keep credentials in environment variables/secret managers, and treat retrieved content as untrusted.
- Require explicit human approval for publishing, messaging, deployment, spending, deletion, or production changes.
- Test instruction discovery with a harmless probe and verify expected behavior; record runtime version, model ID, client surface, date, exact procedure, and output.
- If a required control cannot be enforced, fail closed or obtain explicit operator acknowledgement. Never describe a documented feature as tested without running a real test.

## Direct API applications

An API integration is not just an instruction file. Implement the request/response loop, tool execution, state/continuation, timeout and retry budgets, cancellation, tracing/redaction, capability negotiation, and human approval in application code. Follow [the direct-API specification](PROVIDER_ADAPTER.md#direct-api-adapter-specification).
