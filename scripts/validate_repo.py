#!/usr/bin/env python3
"""Validate Agent-Team's repository structure and low-risk configuration invariants.

This is a static preflight. It does not execute agents, validate remote APIs, or prove security.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".claude/settings.json",
    ".claude/agents/planner.md",
    ".claude/agents/researcher.md",
    ".claude/agents/builder.md",
    ".claude/agents/reviewer.md",
    ".claude/agents/router.md",
    "agents/planner.md",
    "agents/researcher.md",
    "agents/builder.md",
    "agents/reviewer.md",
    "agents/router.md",
    "config/agent-team.example.yaml",
    "docs/SECURITY.md",
    "docs/COMPATIBILITY.md",
    "docs/EVALUATION.md",
    "docs/RESEARCH.md",
    "docs/AGENT_PROTOCOL.md",
    "docs/PRODUCTION_READINESS.md",
    "docs/PLATFORM_MATRIX.md",
    "docs/INCIDENT_RESPONSE.md",
    "docs/RELEASE_CHECKLIST.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/workflows/validate.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/agents/planner.agent.md",
    ".agents/skills/agent-review/SKILL.md",
    "memory/MEMORY.md",
    "run.sh",
)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?<![A-Za-z0-9_])sk-[A-Za-z0-9]{20,}(?![A-Za-z0-9_])"),
    re.compile(r"(?<![A-Za-z0-9_])gh[pousr]_[A-Za-z0-9]{20,}(?![A-Za-z0-9_])"),
)


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    settings = ROOT / ".claude/settings.json"
    if settings.is_file():
        try:
            parsed = json.loads(settings.read_text(encoding="utf-8"))
            if not isinstance(parsed, dict):
                errors.append(".claude/settings.json must contain a JSON object")
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f".claude/settings.json is invalid JSON: {exc}")

    config = ROOT / "config/agent-team.example.yaml"
    if config.is_file():
        content = config.read_text(encoding="utf-8")
        if "fallback_enabled: false" not in content:
            errors.append("Example config must keep cross-provider fallback disabled by default")
        if re.search(r"(?im)^\s*(?:api_key|token|secret)\s*:\s*['\"]?[^#\s]", content):
            errors.append("Example config appears to contain a literal credential")

    for relative in ("AGENTS.md", "README.md", "docs/SECURITY.md"):
        path = ROOT / relative
        if path.is_file():
            content = path.read_text(encoding="utf-8")
            for pattern in SECRET_PATTERNS:
                if pattern.search(content):
                    errors.append(f"Potential secret-like value detected in {relative}")

    if errors:
        print("Agent-Team validation FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Agent-Team validation passed: {len(REQUIRED)} required files checked.")
    print("Static checks only; runtime behavior and security are not proven.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
