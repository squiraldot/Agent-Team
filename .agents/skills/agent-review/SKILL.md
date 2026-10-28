---
name: agent-review
description: Independently review a proposed change for correctness, security, privacy, regression risk, tests, and acceptance criteria.
---

# Agent Review

1. Read the root `AGENTS.md`, the task acceptance criteria, and the complete diff.
2. Review changed code and configuration directly; do not rely on the implementation agent's summary.
3. Prioritize correctness, data loss, security boundaries, secret exposure, injection risks, permission changes, external side effects, compatibility, and missing tests.
4. For each finding, state severity, location, evidence, impact, and a concrete fix.
5. Separate blocking findings from optional improvements.
6. If no findings are found, describe review scope and checks not performed. Do not claim a full audit without one.
7. Never claim a test passed unless you executed it and inspected its output.
