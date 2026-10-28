#!/usr/bin/env bash
set -euo pipefail
# Claude Code supplies hook input as JSON on stdin. This hook intentionally logs no command
# text (which might contain secrets) and does not pretend to be a complete security sandbox.
payload="$(cat)"
tool_name="$(printf '%s' "$payload" | jq -r '.tool_name // empty' 2>/dev/null || true)"
if [[ "$tool_name" == "Bash" ]]; then
  command_text="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"
  # Block a small set of obviously destructive patterns as a last-resort guardrail.
  # This is not a substitute for reviewing commands or configuring Claude permissions.
  if printf '%s' "$command_text" | grep -Eiq '(^|[;&|[:space:]])(rm[[:space:]]+-rf[[:space:]]+/($|[[:space:]])|mkfs([.[:space:]]|$)|shutdown([[:space:]]|$)|reboot([[:space:]]|$))'; then
    printf '%s\n' 'Blocked by Agent-Team safety hook: destructive system command pattern.' >&2
    exit 2
  fi
fi
exit 0
