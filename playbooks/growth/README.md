---
name: ethical-growth-experiment
description: Run measurable and ethical distribution or onboarding experiments.
version: 1.0.0
owner: Agent-Team maintainers
status: active
---

# Ethical Growth Experiment Playbook

## Goal

Run measurable distribution or onboarding experiments that deliver real value without misleading users, violating consent, or spamming.

## Inputs

Target audience, value proposition, channel, baseline data, budget, experiment owner, time window, legal/platform constraints, and consent requirements.

## Workflow

1. Define one audience segment and the problem the experiment addresses.
2. Write a falsifiable hypothesis and identify the expected mechanism.
3. Choose one primary metric plus guardrails (complaints, unsubscribes, refunds, bounce, accessibility, support load).
4. Record baseline, sample assumptions, duration, budget, and stop condition before launch.
5. Produce truthful copy/assets; substantiate quantified claims and disclose sponsorship/affiliate relationships.
6. Review privacy, consent, platform rules, accessibility, and brand fit.
7. Get explicit owner approval before ads, messages, public posts, spend, or data collection begins.
8. Run a bounded experiment and monitor the predeclared metrics.
9. Analyze outcomes with caveats; separate correlation from causation and note sample limitations.
10. Decide to stop, iterate, or scale. Record the decision and update the playbook.

## Guardrails

- Do not buy fake engagement, fabricate social proof, or use deceptive scarcity.
- Do not scrape or message people in ways that violate consent, privacy, or platform rules.
- Do not collect sensitive personal data without a justified purpose and approved handling plan.
- Do not optimize a conversion metric while ignoring material harm in guardrail metrics.
- Set spend limits and a kill switch before starting paid experiments.
- Avoid declaring a winner when the sample is too small or the test was not designed to support that conclusion.

## Experiment record

```yaml
experiment_id: "short-name"
hypothesis: "If X, then Y because Z"
audience: "defined segment"
channel: "channel"
primary_metric: "metric and measurement window"
guardrails: ["complaints", "unsubscribe_rate"]
baseline: "known value or unavailable"
budget_limit: 0
start_date: "YYYY-MM-DD"
stop_condition: "predefined threshold or date"
approval_owner: "owner"
result: "pending"
limitations: []
decision: "stop | iterate | scale | inconclusive"
```

## Deliverables

Experiment brief, approved copy/assets, measurement plan, results with caveats, guardrail outcome, and decision log.
