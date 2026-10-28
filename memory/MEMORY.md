# Agent-Team — Durable Project Memory

> Curated, non-sensitive decisions and lessons only. This file is a navigation aid, not a transcript, issue tracker, secret store, or substitute for canonical documentation.

## Allowed content and format
- Store stable architecture decisions, project-wide conventions, verified compatibility facts, durable lessons, and links to their source documents.
- Use concise bullets with **Decision/Lesson**, **Reason/evidence**, **Date or revision**, and **Canonical reference** where useful.
- Mark uncertainty explicitly; distinguish planned, configured, tested, and production-approved states.
- Keep detailed implementation instructions in their canonical docs and link to them rather than copying them here.

## Prohibited content
- Never store passwords, API keys, tokens, private keys, signing credentials, recovery codes, customer/user personal data, private conversations, raw sensitive traces, or confidential third-party content.
- Do not store speculative claims as facts, transient task state, duplicate documentation, or unredacted incident details.

## Pruning and maintenance
- Review when decisions change, at release milestones, and during maintenance.
- Remove superseded, duplicated, stale, or no-longer-actionable entries; preserve only a short rationale and link to the current decision where history matters.
- Revalidate time-sensitive compatibility claims before retaining them; include exact version/date/evidence or label unverified.
- If a secret or sensitive detail appears, remove it from current content, rotate/revoke exposed credentials, and assess Git history and artifacts. A file edit alone does not erase history.

## Durable project facts
- Shared policy: [AGENTS.md](../AGENTS.md).
- Role contracts: [agents/README.md](../agents/README.md).
- Research method and evidence: [docs/RESEARCH.md](../docs/RESEARCH.md).
- Quality and regression process: [docs/EVALUATION.md](../docs/EVALUATION.md) and [docs/QUALITY_GATES.md](../docs/QUALITY_GATES.md).
- Security model: [docs/SECURITY.md](../docs/SECURITY.md).
- The repository provides portable instructions, runtime examples, workflow docs, and static validation; documentation alone does not create a universal executor or sandbox.
