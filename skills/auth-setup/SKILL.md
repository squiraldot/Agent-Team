---
name: auth-setup
description: Plan and implement secure authentication flows with explicit provider, session, recovery, and authorization boundaries.
version: 1.0.0
owner: Agent-Team maintainers
status: active
---

# Auth Setup

## Trigger conditions
Trigger when adding login/signup, sessions, OAuth, password reset, account deletion, or access control.

## Steps
1. Identify platform, trust boundaries, data sensitivity, user roles, and required providers.
2. Prefer maintained platform-native auth; verify current official docs and SDK versions.
3. Define signup/sign-in, session lifetime/rotation, logout, recovery, email/phone verification, MFA needs, and account deletion.
4. Enforce authorization server-side for every protected resource; deny by default.
5. Protect secrets, cookies/tokens, redirect URIs, rate limits, CSRF/XSS surfaces, and account enumeration.
6. Add tests for unauthenticated, unauthorized, expired, revoked, and cross-user access.
7. Document migrations, recovery, monitoring, and rollback.

## Checklist
- [ ] Threat boundaries and roles documented
- [ ] Secrets remain outside source control
- [ ] Server-side authorization verified
- [ ] Session expiry/revocation tested
- [ ] Recovery and abuse protections tested
- [ ] Privacy/data retention reviewed
- [ ] Failure and rollback paths documented

## Failure modes
No backend enforcement: do not claim protected data is secure. Provider behavior/version unclear: pause implementation and verify docs. OAuth redirect or token handling unsafe: block release until corrected.

## Related canonical guidance
- Shared policy: [AGENTS.md](../../AGENTS.md)
- Research standards: [docs/RESEARCH.md](../../docs/RESEARCH.md)
- Extending this framework: [docs/EXTENDING.md](../../docs/EXTENDING.md)
