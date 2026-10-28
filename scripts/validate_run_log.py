#!/usr/bin/env python3
"""Validate sanitized Agent-Team run-log JSON using only the Python standard library."""
from __future__ import annotations
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

OUTCOMES = {"success", "partial", "blocked", "failed"}
APPROVAL_STATUSES = {"requested", "approved", "denied", "not_requested"}
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"(?<![A-Za-z0-9_])sk-[A-Za-z0-9]{20,}(?![A-Za-z0-9_])"),
    re.compile(r"(?<![A-Za-z0-9_])gh[pousr]_[A-Za-z0-9]{20,}(?![A-Za-z0-9_])"),
    re.compile(r"(?i)\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"""(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['"][A-Za-z0-9_./+=-]{12,}['"]"""),
)
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE = re.compile(r"(?<!\w)(?:\+?\d[ .()-]?){9,15}(?!\w)")

def _timestamp(value: Any, field: str, errors: list[str]) -> datetime | None:
    if not isinstance(value, str):
        errors.append(f"{field} must be an ISO-8601 string with timezone")
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{field} must be a valid ISO-8601 timestamp")
        return None
    if parsed.tzinfo is None:
        errors.append(f"{field} must include a timezone")
        return None
    return parsed

def validate_log(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["run log must be a JSON object"]
    required = ("task_id", "started_at", "finished_at", "roles_used", "sources_consulted", "decisions", "tools_called", "approvals_requested", "outcome")
    for field in required:
        if field not in data:
            errors.append(f"missing required field: {field}")
    if errors:
        return errors
    if not isinstance(data["task_id"], str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{2,127}", data["task_id"]):
        errors.append("task_id must be an opaque 3-128 character identifier")
    start = _timestamp(data["started_at"], "started_at", errors)
    finish = _timestamp(data["finished_at"], "finished_at", errors)
    if start and finish and finish < start:
        errors.append("finished_at must not precede started_at")
    for field in ("roles_used", "sources_consulted", "decisions", "tools_called", "approvals_requested"):
        if not isinstance(data[field], list):
            errors.append(f"{field} must be a list")
    if isinstance(data["roles_used"], list) and any(not isinstance(v, str) or not v for v in data["roles_used"]):
        errors.append("roles_used entries must be non-empty strings")
    if isinstance(data["sources_consulted"], list):
        for i, item in enumerate(data["sources_consulted"]):
            if not isinstance(item, dict) or not isinstance(item.get("source"), str) or not isinstance(item.get("title"), str):
                errors.append(f"sources_consulted[{i}] requires source and title strings")
    if isinstance(data["decisions"], list) and any(not isinstance(v, str) or not v.strip() for v in data["decisions"]):
        errors.append("decisions entries must be non-empty strings")
    if isinstance(data["tools_called"], list):
        for i, item in enumerate(data["tools_called"]):
            if not isinstance(item, dict) or not all(isinstance(item.get(k), str) and item[k] for k in ("name", "capability", "status")):
                errors.append(f"tools_called[{i}] requires name, capability, and status strings")
            elif not isinstance(item.get("duration_ms"), int) or item["duration_ms"] < 0:
                errors.append(f"tools_called[{i}].duration_ms must be a non-negative integer")
    if isinstance(data["approvals_requested"], list):
        for i, item in enumerate(data["approvals_requested"]):
            if not isinstance(item, dict) or not isinstance(item.get("action"), str) or item.get("status") not in APPROVAL_STATUSES:
                errors.append(f"approvals_requested[{i}] requires action and a valid status")
    outcome = data["outcome"]
    if not isinstance(outcome, dict) or outcome.get("status") not in OUTCOMES or not isinstance(outcome.get("summary"), str) or not outcome.get("summary", "").strip():
        errors.append("outcome requires status (success/partial/blocked/failed) and a summary")
    serialized = json.dumps(data, ensure_ascii=False)
    if any(pattern.search(serialized) for pattern in SECRET_PATTERNS):
        errors.append("run log contains a value matching a known secret pattern")
    if EMAIL.search(serialized):
        errors.append("run log appears to contain an email address; remove personal data")
    if PHONE.search(serialized):
        errors.append("run log appears to contain a phone-number-like value; remove personal data")
    return errors

def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("Usage: python scripts/validate_run_log.py RUN_LOG.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(f"Invalid run log: {exc}", file=sys.stderr)
        return 1
    errors = validate_log(data)
    if errors:
        print("Run-log validation FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Run-log validation passed (structural checks only; privacy review is still required).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
