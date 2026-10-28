#!/usr/bin/env python3
"""Generate thin runtime adapters linked to the canonical AGENTS.md policy.

Uses only the Python standard library and is compatible with Android Termux.
Codex reads AGENTS.md directly, so no second Codex policy file is generated.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Relative links are deliberate: each adapter must point to the one shared policy.
ADAPTERS = {
    "CLAUDE.md": (
        "# Claude Code adapter\n\n"
        "Read [AGENTS.md](AGENTS.md) as the single source of truth for shared policy.\n"
        "This file is a thin native entry point; do not copy shared rules here.\n\n"
        "Use Claude Code-specific features only when supported by the installed version:\n"
        "- Agent definitions: `.claude/agents/` (canonical role contracts remain in `agents/`)\n"
        "- Skills: `.claude/skills/`\n"
        "- Hooks and settings: `.claude/hooks/` and `.claude/settings.json`\n\n"
        "If a native feature conflicts with AGENTS.md, follow AGENTS.md and report the incompatibility.\n"
    ),
    ".claude/CLAUDE.md": (
        "# Claude Code project adapter\n\n"
        "Read [the shared policy](../AGENTS.md) before acting. Keep shared behavior in AGENTS.md; "
        "this file only points to the canonical policy and Claude-specific entry points.\n"
        "Use `../agents/` for portable role contracts and `../docs/WORKFLOW.md` for stage contracts.\n"
        "Do not assume tools, hooks, subagents, or permissions are available unless the active runtime confirms them.\n"
    ),
    "GEMINI.md": (
        "# Gemini CLI adapter\n\n"
        "Read [AGENTS.md](AGENTS.md) for the canonical provider-neutral policy. This file is only a Gemini CLI "
        "entry point; do not duplicate shared rules.\n"
        "Use current Gemini CLI documentation for native context, settings, skills, hooks, extensions, and agent features. "
        "Report unavailable capabilities rather than simulating them.\n"
    ),
    ".github/copilot-instructions.md": (
        "# GitHub Copilot adapter\n\n"
        "Follow the canonical [AGENTS.md](../AGENTS.md); do not copy its shared policy into this file.\n"
        "Use native Copilot agent profiles and skills only on supported clients and versions. Repository instructions, "
        "custom-agent behavior, tools, and approvals can differ across GitHub.com, CLI, and IDE surfaces.\n"
    ),
    ".cursor/rules/agent-team.mdc": (
        "---\n"
        "description: Entry point to canonical Agent-Team policy in AGENTS.md\n"
        "alwaysApply: true\n"
        "---\n"
        "Read and follow the repository-root AGENTS.md as the single source of truth. This rule is only a pointer; "
        "do not duplicate shared policy here. Use current Cursor documentation for rules, skills, subagents, hooks, "
        "tools, and approval behavior. Never claim unsupported capabilities or unrun checks.\n"
    ),
}



# Git blob IDs pin canonical bootstrap template bytes. Updating a template requires
# intentionally updating its expected blob ID in the same reviewed change.
BOOTSTRAP_TEMPLATE_BLOBS = {
    "templates/host-bootstrap/AGENTS.md.md": "dacd17e269334ce0fe86ae890b46f9bb728a3a40",
    "templates/host-bootstrap/CLAUDE.md.md": "ff3745fa2d20ec1db96e013e45c9ec3c39e63cdc",
    "templates/host-bootstrap/GEMINI.md.md": "bfd0fe6732c49e304703fcbab4f4763c144d91fb",
    "templates/host-bootstrap/claude-project.md": "b45698876ce3356e16acedf47ff536983747dc90",
    "templates/host-bootstrap/copilot.md": "697f8677f7736c74d1e2c003f46ddf8f6038404b",
    "templates/host-bootstrap/cursor.mdc.md": "324036eeaffa9211aafa3f87af5323e14028e793",
    "templates/host-bootstrap/claude-skill.md": "08fba44edc4865c59e0e34b3c20b368eb5253aab",
    "templates/host-bootstrap/codex-skill.md": "08fba44edc4865c59e0e34b3c20b368eb5253aab",
    "templates/host-bootstrap/local-state/README.md": "04350814e1afaf276325fa9d92aedf59c20e446c",
}


def bootstrap_template_errors(root: Path = ROOT) -> list[str]:
    """Detect missing, unexpected, or byte-drifted host bootstrap templates."""
    directory = root / "templates" / "host-bootstrap"
    errors: list[str] = []
    if not directory.is_dir():
        return ["missing: templates/host-bootstrap/"]
    expected_paths = set(BOOTSTRAP_TEMPLATE_BLOBS)
    actual_paths = {
        path.relative_to(root).as_posix()
        for path in directory.rglob("*")
        if path.is_file()
    }
    for relative in sorted(expected_paths - actual_paths):
        errors.append(f"missing bootstrap template: {relative}")
    for relative in sorted(actual_paths - expected_paths):
        errors.append(f"unexpected bootstrap template: {relative}")
    for relative in sorted(expected_paths & actual_paths):
        data = (root / relative).read_bytes()
        git_blob = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        if git_blob != BOOTSTRAP_TEMPLATE_BLOBS[relative]:
            errors.append(f"bootstrap template drift: {relative}")
    return errors


def render_adapters(root: Path = ROOT) -> dict[str, str]:
    """Render every generated adapter with a digest of the current canonical policy."""
    source = root / "AGENTS.md"
    if not source.is_file():
        raise FileNotFoundError(f"Canonical policy not found: {source}")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    header = (
        "<!-- Generated by scripts/sync_platforms.py; do not edit by hand. -->\n"
        f"<!-- AGENTS-SHA256: {digest} -->\n\n"
    )
    rendered: dict[str, str] = {}
    for relative, body in ADAPTERS.items():
        # Cursor requires YAML frontmatter at the beginning of a rule file.
        if relative.endswith(".mdc") and body.startswith("---\n"):
            _, frontmatter, remainder = body.split("---\n", 2)
            rendered[relative] = "---\n" + frontmatter + "---\n" + header + remainder
        else:
            rendered[relative] = header + body
    return rendered


def sync(root: Path = ROOT, check: bool = False) -> list[str]:
    """Write generated adapters or return drift/missing-file diagnostics in check mode."""
    errors: list[str] = []
    if check:
        template_root = root if (root / "templates" / "host-bootstrap").is_dir() else ROOT
        errors.extend(bootstrap_template_errors(template_root))
    for relative, expected in render_adapters(root).items():
        path = root / relative
        actual = path.read_text(encoding="utf-8") if path.is_file() else None
        if actual == expected:
            continue
        if check:
            state = "missing" if actual is None else "drift"
            errors.append(f"{state}: {relative}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(expected.encode("utf-8"))
            print(f"updated: {relative}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated adapters are missing or stale")
    args = parser.parse_args(argv)
    try:
        errors = sync(root=ROOT, check=args.check)
    except (OSError, UnicodeError) as exc:
        print(f"sync_platforms: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("Platform adapter drift detected:")
        for error in errors:
            print(f"  - {error}")
        print("Run: python scripts/sync_platforms.py")
        return 1
    print("Platform adapters are synchronized with AGENTS.md." if args.check else "Platform adapters updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
