#!/usr/bin/env bash
set -euo pipefail

# Claude Code supplies hook input as JSON on stdin. Never log the command payload:
# it may contain credentials, private paths, or user data. This is a narrow guardrail,
# not a general-purpose security sandbox.
if ! command -v jq >/dev/null 2>&1; then
  printf '%s\n' 'Agent-Team safety hook blocked Bash: jq is required to inspect tool input.' >&2
  exit 2
fi

payload="$(cat)"
if ! printf '%s' "$payload" | jq -e 'type == "object"' >/dev/null 2>&1; then
  printf '%s\n' 'Agent-Team safety hook blocked Bash: hook input was not valid JSON object.' >&2
  exit 2
fi

tool_name="$(printf '%s' "$payload" | jq -r '.tool_name // empty')"
if [[ "$tool_name" == "Bash" ]]; then
  command_text="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty')"

  # Block a narrow set of obviously destructive host/system commands.
  # Runtime permissions, human review, and OS isolation remain the primary controls.
  if printf '%s' "$command_text" | grep -Eiq '(^|[;&|[:space:]])(rm[[:space:]]+-rf[[:space:]]+/($|[[:space:]])|mkfs([.[:space:]]|$)|wipefs([[:space:]]|$)|shutdown([[:space:]]|$)|reboot([[:space:]]|$)|find[[:space:]]+/[^;|&]*[[:space:]]-delete([[:space:]]|$)|dd[[:space:]][^;|&]*[[:space:]]of=/dev/)'; then
    printf '%s\n' 'Blocked by Agent-Team safety hook: destructive system command pattern.' >&2
    exit 2
  fi
fi

exit 0
