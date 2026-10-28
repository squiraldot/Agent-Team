# Agent Handoff Protocol

This document defines portable behavioral contracts for Orchestrator (legacy name: Router), Planner, Deep Researcher (legacy name: Researcher), Builder, QA/Reviewer (legacy name: Reviewer), and Security & Privacy Reviewer. It is not a wire protocol implemented by every supported runtime.

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

## Canonical role contracts

Portable role directories under `agents/` are canonical; native runtime files should be thin wrappers referencing these files. Role files define responsibilities, not proof that a runtime executes a subagent.

- **Orchestrator (legacy Router):** decompose work, select the smallest adequate role set, sequence dependencies, parallelize only independent tasks when runtime support is verified, track handoffs, escalate ambiguity/approval/capability gaps, and stop on acceptance, blockers, exhausted budgets, repeated failures, or no progress. Skip delegation for simple, low-risk tasks.
- **Planner:** define goal and non-goals, scope, explicit requirements versus assumptions, dependencies, risks, observable acceptance criteria, validation steps, and approval/rollback gates. Does not implement unless explicitly assigned both planning and execution.
- **Deep Researcher (legacy Researcher):** define evidence requirements, source quality, version/date context, contradiction handling, and uncertainty. Prefer official docs/specifications, then maintained source code/releases, then public community reports. The research engine is deferred to Phase 4; never imply browser/search execution without an available tool and observed result.
- **Builder:** implement only accepted scope, follow conventions, add regression tests for behavior changes, run available checks, inspect the final diff, and report exact commands/results and limitations. Does not silently expand scope.
- **QA/Reviewer (legacy Reviewer):** independently check acceptance criteria, artifact/diff, evidence, correctness, edge cases, tests, documentation, and regression risk. The producer must not review its own output and call it independent. Findings include severity, location/scenario, evidence, impact, and recommended fix.
- **Security & Privacy Reviewer:** independently assess trust boundaries, sensitive data flows, permissions, secrets, injection, logging/retention, unsafe operations, and consequential side effects. This is not a substitute for a penetration test or compliance audit unless that scope is explicitly and actually performed.

## Routing policy

| Task characteristics | Minimum workflow |
|---|---|
| Trivial explanation or small text edit | Orchestrator → direct answer |
| Multi-file implementation | Orchestrator → Planner → Builder → independent QA/Reviewer |
| Current facts or platform comparison | Orchestrator → Planner → Deep Researcher → QA/Reviewer |
| Security, auth, payments, data deletion, deployment | Planner → Deep Researcher if needed → Builder → independent QA/Reviewer + Security & Privacy Reviewer → human approval |
| Unclear requirements or conflicting constraints | Orchestrator → Planner → user clarification |
| Failure or failed test | Builder reproduces → fixes → retests → independent QA/Reviewer checks regression risk |

Parallelize only independent tasks with clearly separated outputs and verified runtime support. Never let two agents edit the same file concurrently without an explicit merge strategy.

## Conflict resolution

1. User instructions and applicable safety/legal requirements take precedence.
2. Repository security policy and explicitly approved scope constrain execution.
3. Acceptance criteria define completion.
4. Primary-source evidence outranks unsupported recollection.
5. When sources conflict, report the conflict and avoid inventing a universal answer.
6. If the conflict changes a high-impact decision, pause for human input.

## Loop and budget controls

Each adapter should impose maximum steps, retries, delegation depth, and runtime/cost limits. Repeated tool errors, repeated identical output, circular delegation, or no measurable progress should trigger a stop-and-report outcome. Do not make unlimited retries or hide partial failures.
