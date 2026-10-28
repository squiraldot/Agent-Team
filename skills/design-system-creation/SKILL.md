---
name: design-system-creation
description: Create a coherent, accessible, maintainable design system from product needs and existing UI evidence.
version: 1.0.0
owner: Agent-Team maintainers
status: active
---

# Design System Creation

## Trigger conditions
Trigger when multiple screens/products need consistent tokens, components, interaction patterns, or documentation.

## Steps
1. Gather product goals, users, platforms, brand constraints, existing UI, and accessibility targets.
2. Inventory recurring patterns and identify inconsistencies before inventing new components.
3. Define semantic design tokens for color, type, spacing, sizing, elevation, borders, motion, and breakpoints.
4. Specify component anatomy, variants, states, behavior, responsive rules, and content guidance.
5. Define accessible focus, keyboard, contrast, reduced-motion, and assistive-technology behavior.
6. Build representative examples and validate tokens/components in real screens.
7. Publish contribution, naming, versioning, deprecation, and change-review rules.

## Checklist
- [ ] User/platform constraints captured
- [ ] Tokens are semantic and named consistently
- [ ] Components include states and responsive behavior
- [ ] Accessibility requirements documented
- [ ] Examples validated in real contexts
- [ ] Governance and change policy included

## Failure modes
Premature component proliferation: return to evidence and shared patterns. Token mismatch across platforms: document mappings. Inaccessible defaults: block adoption until corrected.

## Related canonical guidance
- Shared policy: [AGENTS.md](../../AGENTS.md)
- Research standards: [docs/RESEARCH.md](../../docs/RESEARCH.md)
- Extending this framework: [docs/EXTENDING.md](../../docs/EXTENDING.md)
