# Platform Capability Matrix

This matrix separates documented native features from Agent-Team runtime verification. **Status describes the evidence level for the integration guidance in this repository:** `documented` means current official docs were checked; `tested` requires an actual runtime test of the exact combination; `unverified` means documentation or runtime behavior remains insufficiently checked. No combination below has been runtime-tested as part of this upgrade. The labels describe documentation evidence only; they do not assert that this repository's adapters execute in those runtimes.

| Platform/runtime | Instructions file | Native subagents | Skills | Hooks | Web access | Approval model | Status |
|---|---|---|---|---|---|---|---|
| OpenAI Codex | `AGENTS.md` (native; canonical policy) | Documented in applicable current Codex surfaces; exact availability is client/version dependent | `.agents/skills/` (documented) | Codex hooks documented; separate from Claude hook schema | Tool/client/configuration dependent; do not assume enabled | Codex permission mode, sandbox, and configured approvals; human policy still applies | documented |
| Anthropic Claude Code | `CLAUDE.md` → `AGENTS.md` | `.claude/agents/`; native support documented | `.claude/skills/` | `.claude/settings.json`, `.claude/hooks/`; native lifecycle hooks documented | Depends on installed tools, permissions, and configuration | Native permission/approval settings; review exact configuration and retain explicit approval for consequential actions | documented |
| Google Gemini CLI | `GEMINI.md` → `AGENTS.md` | Native subagents documented; status and configuration may vary by version | Agent Skills/extensions documented | Native hooks/settings documented | Web search/fetch tools depend on installed version and configuration | Tool trust, approval settings, and sandbox configuration; inspect actual mode before writes | documented |
| GitHub Copilot | `.github/copilot-instructions.md` → `AGENTS.md` | Custom agent profiles documented; invocation and properties vary across GitHub.com, CLI, and IDEs | Documented on supported surfaces; exact location/features vary | Copilot hooks documented for supported surfaces; not universal across all clients | Depends on product surface, available tools, and permissions | Surface-specific permission prompts and assisted-permissions settings; external side effects require explicit approval | documented |
| Cursor | `.cursor/rules/agent-team.mdc` → `AGENTS.md` | Native subagents documented; nesting and tool access are constrained by mode/configuration | `.agents/skills/` and Cursor skills documented | Native hooks documented; configuration and event names are Cursor-specific | Depends on built-in browser/MCP tools, account, and configuration | Runtime permissions plus hook policy; inspect current mode and require approval for consequential side effects | documented |
| Other IDE/CLI runtimes (e.g. Windsurf, Aider, Cline) | Native entry point to be verified; otherwise import `AGENTS.md` using documented mechanism | Runtime-specific; do not assume | Runtime-specific | Runtime-specific | Runtime-specific | Runtime-specific; configure explicit approval gates | unverified |
| Direct provider API application | Application-owned loader for `AGENTS.md` | Application/framework must implement delegation unless API provides it | Application/framework-owned | Application/framework-owned | API/tool dependent | Must be enforced in application code or fail closed | unverified |

## Interpretation and verification

- `documented` is not a claim that this repository's generated adapter was exercised in the named runtime. It means the native feature mapping above is grounded in official docs reviewed on 2026-10-28; links and notes are recorded in [RESEARCH.md](RESEARCH.md).
- No row is marked `tested`: no exact runtime/model/client combination was run during this phase. Static checks and adapter digest checks cannot prove a runtime reads, follows, or enforces an instruction.
- Web access means a usable search/fetch/browser capability, not simply network access. It can depend on the client, account, model, tool permissions, and organization policy.
- Approval model describes potential native controls, not a guarantee that prompts enforce policy. Hooks and instructions are not a security sandbox.
- The Phase 13 consistency pass checked that no runtime combination is labeled tested and that the evidence-level wording is explicit; it did not re-open every platform-specific source listed below. Existing documented labels rely on the dated research notes and listed official sources. Re-fetch relevant docs and test the exact client/version before upgrading a status. Use the checklist in [COMPATIBILITY.md](COMPATIBILITY.md).

## Official documentation checked

Access date: **2026-10-28**. See [RESEARCH.md](RESEARCH.md) for the claim-level summary and source list.
- Codex: https://learn.chatgpt.com/docs/customization/overview ; https://learn.chatgpt.com/docs/agent-configuration/agents-md ; https://learn.chatgpt.com/docs/hooks
- Claude Code: https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more
- Gemini CLI: https://geminicli.com/docs/ ; https://geminicli.com/docs/reference/configuration/ ; https://geminicli.com/docs/extensions/
- GitHub Copilot: https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions ; https://docs.github.com/en/copilot/concepts/customizations/custom-agents ; https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations
- Cursor: https://cursor.com/docs/rules ; https://cursor.com/help/customization/skills ; https://cursor.com/docs/subagents ; https://cursor.com/docs/hooks


## Submodule bootstrap status

These are expected bootstrap entry points, not confirmed runtime observations. As of 2026-10-28, all entries below are **expected, untested** for actual instruction discovery and compliance; no AI client was launched for this submodule implementation.

| Platform | Bootstrap files | Status |
|---|---|---|
| OpenAI Codex | AGENTS.md; .agents/skills/agent-team/SKILL.md | expected, untested |
| Anthropic Claude Code | CLAUDE.md; .claude/CLAUDE.md; .claude/skills/agent-team/SKILL.md | expected, untested |
| Google Gemini CLI | GEMINI.md | expected, untested |
| Cursor | .cursor/rules/agent-team.mdc | expected, untested |
| GitHub Copilot | .github/copilot-instructions.md | expected, untested |

Installer and static test results do not upgrade these labels. Test the exact client/version and confirm which files are loaded before using the tested label.
