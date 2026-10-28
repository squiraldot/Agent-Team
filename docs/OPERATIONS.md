# Operations Guide

## Prerequisites
Git, Bash, Claude Code installed/authenticated, and `jq` for the example command hook.

## First-time setup
1. Clone the repository.
2. Review `.claude/CLAUDE.md`, `.claude/settings.json`, and every hook script.
3. Confirm the selected model is available; change the model setting if needed.
4. Install `jq` if using the sample pre-tool hook.
5. Run `bash run.sh`.
6. Open Claude Code in this repository and confirm it recognizes project instructions and agents.
7. Test with a harmless task before important work.

## Suggested workflow
Planner creates a plan for multi-step tasks; researcher verifies current claims; builder creates the deliverable; reviewer challenges it independently; router chooses revise/clarify/stop; owner inspects changes and runs project tests.

## Troubleshooting
- Agent missing: check Markdown path/frontmatter and reload the CLI if required by your version.
- Hook fails: run `bash -n` on scripts, verify `jq`, and inspect current Claude Code hook schema/logs.
- Wrong model: check CLI/account availability and edit settings.
- Unexpected block: inspect hook and permissions; do not blindly disable safeguards.
- No tests run: `run.sh` checks structure/syntax only; add project-specific tests.

## Maintenance
Review official docs after major releases. Revalidate model IDs, hook payloads, and permissions before broadening access.
