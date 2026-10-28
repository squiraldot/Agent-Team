#!/usr/bin/env python3
"""Static repository preflight; does not prove runtime behavior or security."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md",
    ".claude/settings.json", ".claude/agents/planner.md",
    ".claude/agents/researcher.md", ".claude/agents/builder.md",
    ".claude/agents/reviewer.md", ".claude/agents/router.md",
    "agents/planner.md", "agents/researcher.md", "agents/builder.md",
    "agents/reviewer.md", "agents/router.md", "config/agent-team.example.yaml",
    "docs/SECURITY.md", "docs/COMPATIBILITY.md", "docs/EVALUATION.md",
    "docs/RESEARCH.md", "docs/AGENT_PROTOCOL.md", "docs/PRODUCTION_READINESS.md",
    "docs/PLATFORM_MATRIX.md", "docs/INCIDENT_RESPONSE.md", "docs/RELEASE_CHECKLIST.md",
    "docs/QUALITY_GATES.md", "docs/TOOLS_AND_MCP.md", "docs/RUN_LOG.md", "scripts/validate_run_log.py", "templates/run-log-template.json", "tests/test_validate_run_log.py", "evals/README.md", "CONTRIBUTING.md", "SECURITY.md",
    ".github/workflows/validate.yml", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml", ".github/agents/planner.agent.md",
    ".agents/skills/agent-review/SKILL.md", "memory/MEMORY.md", "run.sh",
)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"(?<![A-Za-z0-9_])sk-[A-Za-z0-9]{20,}(?![A-Za-z0-9_])"),
    re.compile(r"(?<![A-Za-z0-9_])gh[pousr]_[A-Za-z0-9]{20,}(?![A-Za-z0-9_])"),
    re.compile(r"(?i)\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"][A-Za-z0-9_./+=-]{16,}['\"]"),
)
FRONTMATTER_FIELDS = ("name", "description", "version", "owner", "status")
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
PLACEHOLDER = re.compile(r"\b(?:TODO|FIXME|TBD)\b", re.I)
# Intentional examples/documentation can include TODO vocabulary; only flag unresolved
# task placeholders in deliverable artifacts, not guidance explaining the validator.
PLACEHOLDER_EXEMPT = {"scripts/validate_repo.py", "tests/test_validate_repo.py", "docs/EXTENDING.md"}


def parse_front_matter(content: str) -> tuple[dict[str, str] | None, str | None]:
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing opening YAML front matter"
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, "missing closing YAML front matter"
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([a-z][a-z0-9_-]*):\s*(.*?)\s*$", line)
        if not match:
            return None, f"invalid front-matter line: {line}"
        fields[match.group(1)] = match.group(2).strip().strip("'\"")
    missing = [key for key in FRONTMATTER_FIELDS if not fields.get(key)]
    if missing:
        return fields, "missing fields: " + ", ".join(missing)
    if not SEMVER.fullmatch(fields["version"]):
        return fields, "version must follow semantic versioning (MAJOR.MINOR.PATCH)"
    if fields["status"].lower() not in {"draft", "active", "deprecated", "experimental", "archived"}:
        return fields, "status must be draft, active, deprecated, experimental, or archived"
    return fields, None


def required_role_files(root: Path = ROOT) -> list[str]:
    errors = []
    agents = root / "agents"
    required = ("role.md", "rules.md", "tools.md", "checklist.md", "inputs-outputs.md")
    if not agents.exists():
        return ["Missing agents/ directory"]
    for folder in sorted(p for p in agents.iterdir() if p.is_dir()):
        if folder.name.startswith("_"):
            continue
        for filename in required:
            if not (folder / filename).is_file():
                errors.append(f"{folder.relative_to(root).as_posix()}: missing required role file {filename}")
    return errors


def front_matter_errors(root: Path = ROOT) -> list[str]:
    errors = []
    candidates = []
    for pattern in ("agents/*/role.md", "skills/*/SKILL.md", "skills/automation/README.md",
                    "skills/design/README.md", "skills/prompts/README.md", "skills/research/README.md",
                    "skills/writing/README.md", "skills/community-pulse/README.md", "playbooks/*/README.md"):
        candidates.extend(root.glob(pattern))
    seen = set()
    for path in sorted(candidates):
        if path in seen or not path.is_file():
            continue
        seen.add(path)
        _, error = parse_front_matter(path.read_text(encoding="utf-8"))
        if error:
            errors.append(f"{path.relative_to(root).as_posix()}: {error}")
    return errors


def broken_links(root: Path = ROOT) -> list[str]:
    errors = []
    markdown = list(root.rglob("*.md")) + list(root.rglob("*.mdc"))
    link_pattern = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
    reference_pattern = re.compile(r"^\s*\[[^\]]+\]:\s*<?([^\s>]+)>?", re.M)
    for source in markdown:
        if any(part in {".git", ".venv", "__pycache__"} for part in source.parts):
            continue
        text = source.read_text(encoding="utf-8")
        targets = [m.group(1).strip().split()[0] for m in link_pattern.finditer(text)]
        targets.extend(m.group(1).strip() for m in reference_pattern.finditer(text))
        for raw in targets:
            target = raw.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//") or not parsed.path:
                continue
            decoded = unquote(parsed.path)
            candidate = (source.parent / decoded).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{source.relative_to(root).as_posix()}: link escapes repository: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{source.relative_to(root).as_posix()}: broken relative link: {target}")
    return errors


def secret_errors(root: Path = ROOT) -> list[str]:
    errors = []
    ignored_dirs = {".git", ".venv", "__pycache__", "node_modules"}
    for path in root.rglob("*"):
        if not path.is_file() or any(part in ignored_dirs for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".mdc", ".py", ".sh", ".json", ".yaml", ".yml", ".toml", ".txt", ".env", ".ini", ".cfg"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                errors.append(f"Potential secret-like value detected in {path.relative_to(root).as_posix()}")
                break
    return errors


def placeholder_errors(root: Path = ROOT) -> list[str]:
    errors = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".mdc", ".py", ".sh", ".json", ".yaml", ".yml", ".toml", ".txt"}:
            continue
        rel = path.relative_to(root).as_posix()
        if rel in PLACEHOLDER_EXEMPT or any(p in {".git", ".venv", "__pycache__", "node_modules"} for p in path.parts):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for number, line in enumerate(lines, 1):
            if PLACEHOLDER.search(line) and re.search(r"(?:TODO|FIXME|TBD)\s*(?:[:—-]|$)", line, re.I):
                errors.append(f"{rel}:{number}: unfilled placeholder")
    return errors


def index_errors(root: Path = ROOT) -> list[str]:
    """Require all Phase 8 deliverables to be discoverable from canonical indexes."""
    checks = {
        "README.md": ("evals/README.md", "docs/QUALITY_GATES.md", "docs/TOOLS_AND_MCP.md", "docs/RUN_LOG.md", "scripts/validate_run_log.py", "templates/run-log-template.json"),
        "docs/README.md": ("QUALITY_GATES.md", "EVALUATION.md", "SECURITY.md", "TOOLS_AND_MCP.md", "RUN_LOG.md"),
        "evals/README.md": ("planner.md", "researcher.md", "builder.md", "reviewer.md", "router.md", "security-privacy-reviewer.md", "domain-specialists.md"),
    }
    errors = []
    for index, needles in checks.items():
        path = root / index
        if not path.is_file():
            errors.append(f"Missing index: {index}")
            continue
        content = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in content:
                errors.append(f"{index}: missing index entry for {needle}")
    return errors


def collect_errors(root: Path = ROOT) -> list[str]:
    errors = [f"Missing required file: {p}" for p in REQUIRED if not (root / p).is_file()]
    errors.extend(required_role_files(root))
    errors.extend(front_matter_errors(root))
    errors.extend(broken_links(root))
    errors.extend(secret_errors(root))
    errors.extend(placeholder_errors(root))
    errors.extend(index_errors(root))
    settings = root / ".claude/settings.json"
    if settings.is_file():
        try:
            if not isinstance(json.loads(settings.read_text(encoding="utf-8")), dict):
                errors.append(".claude/settings.json must contain a JSON object")
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f".claude/settings.json is invalid JSON: {exc}")
    config = root / "config/agent-team.example.yaml"
    if config.is_file():
        content = config.read_text(encoding="utf-8")
        if "fallback_enabled: false" not in content:
            errors.append("Example config must keep fallback disabled by default")
        if "cross_provider_fallback_enabled: false" not in content or "allow_cross_provider_fallback: false" not in content:
            errors.append("Example config must keep cross-provider fallback disabled in routing and privacy")
        for tier in ("fast", "balanced", "deep-reasoning"):
            if not re.search(rf"(?m)^  {re.escape(tier)}:\s*$", content):
                errors.append(f"Example config missing model tier: {tier}")
        for role in ("planner", "researcher", "builder", "reviewer", "router"):
            match = re.search(rf"(?ms)^  {role}:\n(.*?)(?=^  [a-z][a-z0-9_-]*:\n|^privacy:|\Z)", content)
            if not match:
                errors.append(f"Example config missing role routing: {role}")
                continue
            block = match.group(1)
            for key in ("tier:", "fallback_order:", "max_input_tokens:", "max_output_tokens:", "max_cost_usd:", "max_iterations:", "timeout_seconds:"):
                if key not in block:
                    errors.append(f"Example config role {role} missing {key}")
        if re.search(r"(?im)^\s*(?:api_key|token|secret)\s*:\s*['\"]?[^#\s]", content):
            errors.append("Example config appears to contain a literal credential")
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        print("Agent-Team validation FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Agent-Team validation passed: {len(REQUIRED)} required files plus role contracts, front matter, links, secrets, placeholders, and indexes checked.")
    print("Static checks only; runtime behavior and security are not proven.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
