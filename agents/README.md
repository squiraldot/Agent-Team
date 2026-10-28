# Portable agent roles

The role directories are the canonical, runtime-neutral contracts. Each contains `role.md`, `rules.md`, `tools.md`, `checklist.md`, `inputs-outputs.md`, `examples/`, and `evals/`. Native runtime files are thin wrappers that reference these contracts rather than duplicate policy.

## Core roles

| Role | Canonical contract | Use |
|---|---|---|
| Orchestrator | [orchestrator/role.md](orchestrator/role.md) | Decompose tasks, select roles, sequence work, escalate, and stop safely. |
| Planner | [planner/role.md](planner/role.md) | Define scope, assumptions, dependencies, risks, acceptance criteria, and validation. |
| Deep Researcher | [deep-researcher/role.md](deep-researcher/role.md) | Specify evidence-first research outputs; the research engine is deferred to Phase 4. |
| Builder | [builder/role.md](builder/role.md) | Implement scoped work and report actual verification. |
| QA/Reviewer | [qa-reviewer/role.md](qa-reviewer/role.md) | Independently review output against criteria; never review its own work. |
| Security & Privacy Reviewer | [security-privacy-reviewer/role.md](security-privacy-reviewer/role.md) | Assess trust boundaries, permissions, data flows, and consequential side effects. |

## Domain specialist roles — Phase 3

| Role | Canonical contract | Scope |
|---|---|---|
| Web Developer | [web-developer/role.md](web-developer/role.md) | Frontend, backend, full-stack, SEO, performance, accessibility. |
| Android Developer | [android-developer/role.md](android-developer/role.md) | Kotlin/Compose, Java/XML, cross-platform trade-offs, Play compliance. |
| Software Developer | [software-developer/role.md](software-developer/role.md) | CLI tools, APIs, desktop apps, libraries, systems. |
| Plugin/Module Developer | [plugin-module-developer/role.md](plugin-module-developer/role.md) | WordPress, VS Code, browser extensions, npm/PyPI packages, authorized mods. |
| UI/UX Designer | [ui-ux-designer/role.md](ui-ux-designer/role.md) | Research, personas, flows, wireframes, design systems, accessibility, usability. |
| Graphic Designer & Branding | [graphic-designer-branding/role.md](graphic-designer-branding/role.md) | Identity, logos, typography, color systems, brand guidelines. |
| Illustrator & Visual Artist | [illustrator-visual-artist/role.md](illustrator-visual-artist/role.md) | Art direction, image-tool briefs/specs, style guides, asset lists. |
| Content Creator | [content-creator/role.md](content-creator/role.md) | Copy, scripts, social, blogs, documentation, localization including Hinglish when requested. |
| Automation & AI Tools Specialist | [automation-ai-tools-specialist/role.md](automation-ai-tools-specialist/role.md) | Workflows, agents, integrations, digital-tool and trend evaluation. |

Every domain role documents research obligations referencing [docs/RESEARCH.md](../docs/RESEARCH.md) as the Phase 4 protocol, an independent QA/Reviewer handoff, and refusal/escalation boundaries. Research process implementation remains out of scope until Phase 4.

## Add a role

1. Copy [`templates/_role-template/`](../templates/_role-template/) to a kebab-case directory under `agents/`.
2. Complete all contract, example, and evaluation files.
3. Keep scope bounded; state graceful degradation and refusal/escalation rules.
4. Add the role here and create thin wrappers only for runtimes that support them.
5. Check [the handoff protocol](../docs/AGENT_PROTOCOL.md) and [shared policy](../AGENTS.md).

## Legacy paths

Flat files `planner.md`, `builder.md`, `researcher.md`, `reviewer.md`, and `router.md` remain compatibility summaries. Update canonical directories rather than duplicating role policy.
