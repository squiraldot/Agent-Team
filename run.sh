#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"
printf '%s\n' 'Agent-Team repository preflight'

required=(
  'README.md'
  'AGENTS.md'
  'CLAUDE.md'
  'GEMINI.md'
  '.claude/CLAUDE.md'
  '.claude/settings.json'
  'agents/planner.md'
  'agents/researcher.md'
  'agents/builder.md'
  'agents/reviewer.md'
  'agents/router.md'
  'config/agent-team.example.yaml'
  'docs/SECURITY.md'
  'docs/COMPATIBILITY.md'
  'docs/EVALUATION.md'
  'memory/MEMORY.md'
)
missing=0
for path in "${required[@]}"; do
  if [[ -f "$path" ]]; then
    printf '  OK   %s\n' "$path"
  else
    printf '  MISS %s\n' "$path"
    missing=1
  fi
done

if [[ "$missing" -ne 0 ]]; then
  echo 'Preflight failed: required files missing.' >&2
  exit 1
fi

if command -v python3 >/dev/null 2>&1; then
  python3 scripts/validate_repo.py
  python3 -m unittest discover -s tests -v
  python3 -m json.tool .claude/settings.json >/dev/null
  echo '  OK   Python tests and settings JSON'
else
  echo 'WARN python3 not installed; Python validation and unit tests skipped' >&2
fi

if command -v jq >/dev/null 2>&1; then
  jq empty .claude/settings.json
  echo '  OK   jq settings JSON parse'
fi

for path in .claude/hooks/*.sh; do
  bash -n "$path"
done
bash -n run.sh
echo '  OK   shell syntax'
echo 'Preflight complete. Static checks only; runtime behavior and security are not proven.'
