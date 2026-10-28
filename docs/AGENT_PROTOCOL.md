# Agent Handoff Protocol

This document defines a portable contract for Planner, Researcher, Builder, Reviewer, and Router roles. It is a behavioral specification, not a wire protocol implemented by every supported runtime.

## Shared task envelope

Every delegated task should carry the fields below when relevant. A runtime adapter may serialize them as Markdown, JSON, tool arguments, or native task metadata.

```yaml
task_id: "stable-id"
goal: "one sentence describing the desired outcome"
context:
  repository: "optional repository or workspace"
  constraints: []
  prior_decisions: []
inputs: []
required_outputs: []
acceptance_criteria: []
risk_level: low # low | medium | high | critical
permissions:
  read: []
  write: []
  external_actions: []
budget:
  max_steps: 20
  max_retries: 1
  max_cost: null
status: queued # queued | active | blocked | review | done | failed
```

This is an illustrative schema. It is not validated by a universal executor in the current repository.

## Required handoff response

Agents return a concise but inspectable report:
- **Status:** done, blocked, needs-review, or failed.
- **Outcome:** what was produced or discovered.
- **Evidence:** files changed, test output, source URLs, or reproducible observations.
- **Assumptions and uncertainty:** what was inferred and what remains unknown.
- **Risks:** security, privacy, compatibility, and external side effects.
- **Next action:** a specific handoff or a statement that no action is required.

Never return "done" when acceptance criteria are unmet. Never claim a test passed unless it was run and its result inspected.

## Role contracts

### Planner
Produces scope, acceptance criteria, dependency order, risk assessment, validation plan, and explicit questions for blockers. Avoids premature implementation when a material requirement is unclear.

### Researcher
Uses primary documentation first, then source code and high-quality community implementations. Records access date, exact URLs, version context, contradictions, and unsupported assumptions. Treats repository issues and examples as evidence of a particular implementation, not universal platform guarantees.

### Builder
Changes only files needed for the task, follows existing conventions, adds regression tests for behavior changes, runs targeted checks, and reports actual results. Does not expand scope without routing the change back through planning.

### Reviewer
Reviews independently from acceptance criteria and diff. Looks for incorrect behavior, missing edge cases, insecure defaults, secrets, prompt injection, privilege escalation, misleading claims, missing tests, and operational gaps. Findings include severity, evidence, and a suggested fix.

### Router
Chooses the smallest adequate workflow. It may skip agents for trivial tasks, but should add research and independent review for high-risk or evidence-sensitive work. Stops to clarify when ambiguity materially changes the outcome.

## Routing policy

| Task characteristics | Minimum workflow |
|---|---|
| Trivial explanation or small text edit | Router → direct answer |
| Multi-file implementation | Planner → Builder → Reviewer |
| Current facts or platform comparison | Planner → Researcher → Reviewer |
| Security, auth, payments, data deletion, deployment | Planner → Researcher if needed → Builder → independent Reviewer → human approval |
| Unclear requirements or conflicting constraints | Router → Planner → user clarification |
| Failure or failed test | Builder reproduces → fixes → retests → Reviewer checks regression risk |

Parallelize only independent tasks with clearly separated outputs. Never let two agents edit the same file concurrently without an explicit merge strategy.

## Conflict resolution

1. User instructions and applicable safety/legal requirements take precedence.
2. Repository security policy and explicitly approved scope constrain execution.
3. Acceptance criteria define completion.
4. Primary-source evidence outranks unsupported recollection.
5. When sources conflict, report the conflict and avoid inventing a universal answer.
6. If the conflict changes a high-impact decision, pause for human input.

## Loop and budget controls

Each adapter should impose maximum steps, retries, delegation depth, and runtime/cost limits. Repeated tool errors, repeated identical output, circular delegation, or no measurable progress should trigger a stop-and-report outcome. Do not make unlimited retries or hide partial failures.
