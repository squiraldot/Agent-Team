# Conflict Resolution and Decision Escalation

## Required sequence
1. Each disagreeing agent states its position, assumptions, recommendation, evidence (opened URLs/paths, source/access dates, versions, test output), confidence, and risks. Separate facts, inference, preference, and unknowns; unsupported claims are **UNVERIFIED**.
2. Compare evidence and applicability; list shared facts, disputed claims, risks, reversibility, and what evidence could change either position. Do not use majority vote, fluency, seniority, or confidence as a substitute for evidence.
3. Escalate both positions to the **Orchestrator**. It checks source quality, context, dependencies, user constraints, and whether the disagreement is actually caused by different assumptions.
4. The Orchestrator may resolve a low-risk, reversible issue only when evidence and delegated authority clearly support it. Record rationale and outcome in [DECISIONS.md](DECISIONS.md).
5. Escalate to a **human decision owner** if material disagreement remains, risk is high/irreversible, scope/architecture/public claims/licensing change, approval is required, or the agents lack authority. Pause dependent work until decided or explicitly deferred.
6. Record status, date, both evidence-backed positions, decision owner, rationale, consequences, follow-ups, and links in [DECISIONS.md](DECISIONS.md). Pending means unresolved, not consensus. Revisit only when material evidence or assumptions change, preserving history.
7. Follow [research/PROTOCOL.md](../research/PROTOCOL.md) for source tiers, access dates, cross-checks, conflicts, and confidence.

## Human decision memo template
- **Decision ID / date / status:** ADR-NNN / YYYY-MM-DD / Pending | Accepted | Rejected | Superseded
- **Decision owner / approval needed:**
- **Question and deadline:** one sentence and why now
- **Context and hard constraints:** scope, user requirements, safety/legal constraints
- **Position A:** agent, recommendation, evidence URLs/paths + dates, confidence, risks
- **Position B:** agent, recommendation, evidence URLs/paths + dates, confidence, risks
- **Shared facts / unresolved disputes:** label unknowns **UNVERIFIED**
- **Options:** A / B / hybrid / defer; impact, cost, reversibility, compatibility
- **Orchestrator assessment:** evidence quality, conflicts, safer experiment, recommendation
- **Human decision and rationale:** choice, approver, timestamp; or deferment and owner
- **Follow-ups:** action, owner, due date, tests, migration/rollback
- **Record links:** PR/issue, artifacts, tests, related ADRs

## Safety
Escalate unresolved legal, licensing, privacy, security, irreversible-action, and material scope questions. Keep secrets and personal data out of records; link restricted evidence instead of copying it. If evidence is inaccessible and no safe authorized decision is possible, pause.
