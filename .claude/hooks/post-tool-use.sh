#!/usr/bin/env bash
set -euo pipefail
# Intentionally do not print tool output or file contents: they may contain sensitive data.
# Add project-specific lint/format commands only after verifying they are safe and available.
printf '%s\n' 'Agent-Team: after editing, inspect the diff and run the narrowest relevant check.'
exit 0
