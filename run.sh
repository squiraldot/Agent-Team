#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"
printf '%s\n' 'Agent-Team repository preflight'
required=('README.md' '.claude/CLAUDE.md' '.claude/settings.json' 'agents/planner.md' 'agents/researcher.md' 'agents/builder.md' 'agents/reviewer.md' 'agents/router.md' 'memory/MEMORY.md')
missing=0
for path in "${required[@]}"; do
  if [[ -f "$path" ]]; then printf '  OK   %s\n' "$path"; else printf '  MISS %s\n' "$path"; missing=1; fi
done
if command -v jq >/dev/null 2>&1; then jq empty .claude/settings.json && echo '  OK   settings JSON parses'; else echo '  SKIP jq not installed'; fi
for path in .claude/hooks/*.sh; do bash -n "$path"; done
bash -n run.sh
echo '  OK   shell syntax'
if [[ "$missing" -ne 0 ]]; then echo 'Preflight failed: required files missing.' >&2; exit 1; fi
echo 'Preflight complete. Structural/syntax checks only; agent behavior and security are not proven.'
