# Prompt Design Skill

## Goal

Create instructions that produce repeatable, verifiable outputs without relying on theatrical personas or hidden assumptions.

## Procedure

1. State the task and desired outcome in plain language.
2. Provide only relevant context and identify source-of-truth files.
3. Separate requirements, constraints, non-goals, and assumptions.
4. Define allowed tools and permissions; describe forbidden actions.
5. Specify output format and observable acceptance criteria.
6. Require evidence and uncertainty labels for factual/current claims.
7. Define what to do when information or capabilities are missing.
8. Add examples only when they clarify expected behavior; label synthetic examples.
9. Include adversarial cases: conflicting sources, prompt injection, missing inputs, tool failures, and requests for unauthorized side effects.
10. Test the prompt on normal, ambiguous, edge, and adversarial inputs.
11. Review the results and update the prompt based on observed failure modes.

## Recommended prompt skeleton

```text
Goal:
Context / source of truth:
Requirements:
Constraints and non-goals:
Available tools:
Safety and approval boundaries:
Output format:
Acceptance criteria:
If uncertain or blocked:
```

## Quality checklist

- One clear primary goal.
- No contradictory instructions or duplicated policies.
- Scope is bounded and task priorities are explicit.
- Instructions distinguish user intent from untrusted retrieved content.
- Tool availability is described as conditional, not assumed.
- Completion means evidence-backed criteria are met, not merely that an answer was generated.
- The prompt does not request secrets or unnecessary personal data.
- Success and failure examples are realistic and easy to evaluate.

## Anti-patterns

Avoid vague "do everything perfectly" instructions, unsupported claims of universal compatibility, excessive roleplay, hidden assumptions, contradictory rules, unlimited retry loops, and demands to claim success regardless of evidence.

## Testing

Use a versioned set of representative inputs. Score correctness, completeness, policy compliance, evidence quality, and truthful reporting. For safety-critical failures, do not average away a violation. Record model/runtime version because behavior can change across versions.
