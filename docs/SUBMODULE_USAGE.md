# Using Agent-Team as a Git Submodule

This guide covers the pinned-framework model, installation lifecycle, host state, platform entry points, CI, safe updates, troubleshooting, and verification boundaries. The submodule is a read-only source of framework policy and assets; the host repository remains the project being changed.

## Model and boundaries

- **Host root:** the user's repository and project-specific instructions.
- **Framework root:** the pinned Agent-Team submodule, default .agent-team/.
- **Host-local state:** .agent-team-local/ in the host repository.

Never write host-specific memory, evidence, run logs, decisions, generated artifacts, or credentials inside the submodule. Keep the submodule pinned to a reviewed commit. The installer uses only Python's standard library and does not create symlinks.

## Prerequisites and first install

Requirements: Git, Python 3.10+, and an existing host directory. Install the submodule from the host root:

\`\`\`bash
git submodule add https://github.com/squiraldot/Agent-Team.git .agent-team
python3 .agent-team/scripts/install_into_project.py --target .
python3 .agent-team/scripts/install_into_project.py --target . --check
\`\`\`

The repository URL is the public upstream URL; use your approved fork URL if appropriate. The host commit records the selected submodule commit. Commit the installer-generated host instruction changes and the .gitmodules/gitlink changes in the host repository after reviewing the diff.

If the framework policy is missing, initialize submodules with \`git submodule update --init --recursive\`. The installer intentionally exits with code 2 and prints this recovery command rather than silently installing a broken bootstrap.

## Installer reference

\`\`\`text
python3 .agent-team/scripts/install_into_project.py [options]

--target PATH             host project root (default: current directory)
--submodule-path PATH     submodule path relative to host root (default: .agent-team)
--platforms all|LIST      all or comma-separated platform names
--dry-run                 print planned changes without writing
--check                   exit 1 when managed bootstrap files drift
--uninstall               remove only Agent-Team managed blocks
\`\`\`

Supported platform selectors are codex, claude, gemini, cursor, and copilot. AGENTS.md is always generated as the provider-neutral entry point; the selector chooses additional platform-specific files/stubs. --dry-run, --check, and --uninstall are mutually exclusive. Exit code 0 means the requested operation completed, 1 means --check found drift, and 2 means usage/environment/marker/path failure.

### Managed-block safety

The only region updated in an existing host file is the block between:

\`\`\`html
<!-- agent-team:begin -->
... managed Agent-Team instructions ...
<!-- agent-team:end -->
\`\`\`

If no markers exist, the installer appends a managed block without replacing existing text. If a marker is missing, duplicated, or reversed, the installer stops before applying any planned changes. Run --check after manual edits. Uninstall removes managed blocks only; it intentionally leaves .agent-team-local/, the submodule, and all unrelated host text untouched.

Do not use the installer to rewrite the submodule's own generated adapters. scripts/sync_platforms.py manages framework-owned adapter files; install_into_project.py manages host-owned bootstrap blocks.

## Host-local state

The installer scaffolds .agent-team-local/ with:

- memory/: curated non-secret host-specific lessons and decisions.
- evidence/: research notes, source URLs, access dates, and uncertainty.
- runs/: sanitized run logs without raw prompts, credentials, or unnecessary personal data.
- decisions/: concise decisions and approval records.

The scaffold is additive. Existing files and directories are not overwritten. Apply the host project's access controls and retention policy. The installer does not generate runtime records automatically; tools or people must write records deliberately.

## First prompt

Use a prompt such as:

> Read .agent-team/AGENTS.md first. Resolve all Agent-Team framework paths relative to .agent-team/. My project's own instructions win for project-specific architecture, conventions, and dependencies. Agent-Team governs workflow, research protocol, safety boundaries, and independent review gates. Keep the submodule read-only; host-specific memory, evidence, run logs, and decisions belong only in .agent-team-local/.

## Clone, initialize, pin, and update

Clone with recursive submodules:

\`\`\`bash
git clone --recurse-submodules <host-repository-url>
\`\`\`

For an existing checkout:

\`\`\`bash
git submodule update --init --recursive
\`\`\`

A detached HEAD inside the submodule is normal: the host repository pins a commit, not a moving branch. To update deliberately to a published release tag (example only; use a tag only if it actually exists):

\`\`\`bash
git -C .agent-team fetch --tags
git -C .agent-team checkout v1.0.0
git add .agent-team
git commit -m "chore: update Agent-Team submodule"
\`\`\`

To pin a reviewed exact commit, checkout its SHA instead of a tag. Then commit the updated gitlink in the host repository. Teammates and CI reproduce the pin with \`git submodule update --init --recursive\`. Review release notes, migrations, and changes to role contracts before updating.

## CI setup

The host CI checkout step must initialize submodules recursively. For GitHub Actions:

\`\`\`yaml
- uses: actions/checkout@v4
  with:
    submodules: recursive
\`\`\`

Then run the installer check from the host root. Framework maintainers should run the framework validator, sync check, unit tests, and the local-submodule end-to-end script in the Agent-Team repository itself. These are separate checks for separate roots.

## Platform entry points and evidence

All statuses below are **expected, untested** for actual AI-client behavior in this implementation environment. The repository code is not evidence that an AI client loaded or obeyed a bootstrap file.

| Platform | Files installed | Evidence status |
|---|---|---|
| OpenAI Codex | AGENTS.md; .agents/skills/agent-team/SKILL.md | expected, untested |
| Claude Code | CLAUDE.md; .claude/CLAUDE.md; .claude/skills/agent-team/SKILL.md | expected, untested |
| Gemini CLI | GEMINI.md | expected, untested |
| Cursor | .cursor/rules/agent-team.mdc | expected, untested |
| GitHub Copilot | .github/copilot-instructions.md | expected, untested |

The Cursor and skills formats still need manual checks in each installed client/version. Instructions and skill stubs are pointers, not an execution sandbox or proof that independent subagents are launched.

## Termux

Install Git and Python 3 using the Termux package manager, then run the same commands with \`python3\`. The installer has no pip dependencies, does not rely on symlinks, and normalizes framework paths to forward slashes. Ensure the selected submodule path exists and that the host directory is writable. Review changes with \`git status --short\` and \`git diff --\` before committing.

## Troubleshooting

### Submodule folder is empty
Run \`git submodule update --init --recursive\`; check .gitmodules and network access. The installer requires <submodule-path>/AGENTS.md.

### Detached HEAD
Expected for a pinned submodule. Do not commit framework edits inside it for ordinary host work. Choose a release tag or commit intentionally and commit the changed gitlink in the host.

### AI tool does not pick up the rules
Confirm the tool recognizes the installed instruction path, the correct host root is open, and the managed block points to the correct submodule path. Reload/reopen only as documented by that product. Ask the tool to state which policy file it read, then compare the result with a harmless task. Do not label a platform tested until you observe the exact client/version.

### Managed-block conflict
Back up the file. Make sure there is exactly one begin marker and one end marker in the correct order. The installer refuses malformed or duplicate markers and should make no changes. Resolve the conflict manually, then run --check.

### Custom submodule path
Pass the same value to every installer invocation, for example \`--submodule-path vendor/agent-team\`. The path must be relative and cannot contain .. components or traverse symlinks.

### Uninstalling
Run \`python3 .agent-team/scripts/install_into_project.py --target . --uninstall\`. This only removes managed bootstrap blocks. It deliberately does not delete local state or remove the Git submodule. Remove those separately only after reviewing and backing up the host data.

## Verification boundary

Static tests can prove installer behavior against temporary fixtures; they cannot prove native AI-tool discovery or adherence. Record client, version, operating system, model/provider, permission mode, observed files loaded, test prompt, outcome, and limitations before changing any platform row to tested.
