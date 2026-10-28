#!/usr/bin/env python3
"""Install Agent-Team host bootstrap blocks without replacing user-owned content."""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "<!-- agent-team:begin -->"
END = "<!-- agent-team:end -->"
LOCAL_DIRS = ("memory", "evidence", "runs", "decisions")
PLATFORM_FILES = {
    "codex": ("AGENTS.md", ".agents/skills/agent-team/SKILL.md"),
    "claude": ("CLAUDE.md", ".claude/CLAUDE.md", ".claude/skills/agent-team/SKILL.md"),
    "gemini": ("GEMINI.md",),
    "cursor": (".cursor/rules/agent-team.mdc",),
    "copilot": (".github/copilot-instructions.md",),
}
ALL_PLATFORMS = tuple(PLATFORM_FILES)
CORE_FILE = "AGENTS.md"
FRONTMATTER = {
    ".cursor/rules/agent-team.mdc": "---\ndescription: Entry point to canonical Agent-Team policy in the pinned submodule\nalwaysApply: true\n---\n",
    ".claude/skills/agent-team/SKILL.md": "---\nname: agent-team\ndescription: Entry point to the pinned Agent-Team workflow and review gates.\n---\n",
    ".agents/skills/agent-team/SKILL.md": "---\nname: agent-team\ndescription: Entry point to the pinned Agent-Team workflow and review gates.\n---\n",
}


def has_frontmatter(content: str) -> bool:
    return content.startswith("---\n") and "\n---\n" in content[4:]


class InstallError(Exception):
    """Expected, user-actionable installation error."""


def safe_relative_path(value: str, label: str) -> str:
    normalized = value.replace("\\", "/")
    path = Path(normalized)
    if not normalized or path.is_absolute() or any(part in ("", ".", "..") for part in normalized.split("/")):
        raise InstallError(f"{label} must be a safe relative path without '..': {value!r}")
    if re.match(r"^[A-Za-z]:", normalized):
        raise InstallError(f"{label} must be relative: {value!r}")
    return normalized.rstrip("/")


def parse_platforms(value: str) -> tuple[str, ...]:
    if value.strip().lower() == "all":
        return ALL_PLATFORMS
    chosen = tuple(dict.fromkeys(part.strip().lower() for part in value.split(",") if part.strip()))
    unknown = sorted(set(chosen) - set(ALL_PLATFORMS))
    if not chosen or unknown:
        raise InstallError("Invalid --platforms. Choose all or a comma list from: " + ", ".join(ALL_PLATFORMS))
    return chosen


def render_template(path: Path, submodule_path: str) -> str:
    try:
        template = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise InstallError(f"Cannot read bootstrap template {path}: {exc}") from exc
    return template.replace("{{SUBMODULE_PATH}}", submodule_path).replace("{{LOCAL_STATE}}", ".agent-team-local")


def managed_block(text: str) -> tuple[str, int]:
    starts = text.count(BEGIN)
    ends = text.count(END)
    if starts != ends or starts > 1:
        raise InstallError("Malformed or duplicated Agent-Team managed markers; expected exactly zero or one matching begin/end pair.")
    if starts == 0:
        return text, 0
    start = text.find(BEGIN)
    end = text.find(END)
    if end < start:
        raise InstallError("Malformed Agent-Team managed markers: end marker appears before begin marker.")
    return text[:start].rstrip(), 1


def merge_content(
    existing: str | None,
    block: str,
    uninstall: bool = False,
    generated_frontmatter: str | None = None,
) -> str | None:
    if existing is None:
        return None if uninstall else block.rstrip()
    starts, ends = existing.count(BEGIN), existing.count(END)
    if starts != ends or starts > 1:
        raise InstallError("Malformed or duplicated Agent-Team managed markers; no files were changed.")
    if starts == 1:
        start = existing.find(BEGIN)
        end = existing.find(END)
        if end < start:
            raise InstallError("Malformed Agent-Team managed markers: end marker appears before begin marker; no files were changed.")
        end += len(END)
        replacement = "" if uninstall else block.rstrip()
        result = existing[:start] + replacement + existing[end:]
        if not result.strip():
            return None
        # A platform file created by this installer consists only of its known
        # front matter plus the managed block. Remove that file on uninstall,
        # but preserve any user-authored text outside the block.
        if uninstall and generated_frontmatter and result.strip() == generated_frontmatter.strip():
            return None
        return result
    if uninstall:
        if generated_frontmatter and existing.strip() == generated_frontmatter.strip():
            return None
        return existing
    separator = "" if not existing or existing.endswith("\n") else "\n"
    return existing + separator + block.rstrip()


def check_no_symlink_path(root: Path, relative: str) -> Path:
    current = root
    parts = relative.split("/")
    for index, part in enumerate(parts):
        current = current / part
        if current.is_symlink():
            raise InstallError(f"Symlinks are not supported for host integration paths: {current}")
        if index < len(parts) - 1 and current.exists() and not current.is_dir():
            raise InstallError(f"Expected a directory in host integration path: {current}")
    return current


def state_scaffold(target: Path, dry_run: bool) -> list[str]:
    actions = []
    base = target / ".agent-team-local"
    if base.is_symlink():
        raise InstallError(f"Host-local state path must not be a symlink: {base}")
    if base.exists() and not base.is_dir():
        raise InstallError(f"Host-local state path must be a directory: {base}")
    readme = base / "README.md"
    if readme.is_symlink():
        raise InstallError(f"Host-local state README must not be a symlink: {readme}")
    if not readme.exists():
        content = render_template(ROOT / "templates/host-bootstrap/local-state/README.md", ".agent-team")
        actions.append(f"create .agent-team-local/README.md")
        if not dry_run:
            base.mkdir(parents=True, exist_ok=True)
            readme.write_text(content, encoding="utf-8")
    elif not readme.is_file():
        raise InstallError(f"Expected a regular file: {readme}")
    for name in LOCAL_DIRS:
        folder = base / name
        if folder.is_symlink():
            raise InstallError(f"Host-local state directory must not be a symlink: {folder}")
        if not folder.exists():
            actions.append(f"create .agent-team-local/{name}/")
            if not dry_run:
                folder.mkdir(parents=True, exist_ok=True)
                (folder / "README.md").write_text(
                    f"# {name.title()}\n\nHost-local Agent-Team {name} data. Keep secrets and unnecessary personal data out.\n",
                    encoding="utf-8",
                )
        elif not folder.is_dir():
            raise InstallError(f"Expected a directory: {folder}")
    return actions


def selected_files(platforms: tuple[str, ...]) -> list[str]:
    # AGENTS.md is the provider-neutral entry point and is always installed.
    result = [CORE_FILE]
    for platform in platforms:
        for path in PLATFORM_FILES[platform]:
            if path not in result:
                result.append(path)
    return result


def build_block(relative: str, submodule_path: str) -> str:
    template_files = {
        "AGENTS.md": "AGENTS.md.md",
        "CLAUDE.md": "CLAUDE.md.md",
        "GEMINI.md": "GEMINI.md.md",
        ".claude/CLAUDE.md": "claude-project.md",
        ".claude/skills/agent-team/SKILL.md": "claude-skill.md",
        ".agents/skills/agent-team/SKILL.md": "codex-skill.md",
        ".github/copilot-instructions.md": "copilot.md",
        ".cursor/rules/agent-team.mdc": "cursor.mdc.md",
    }
    template_name = template_files.get(relative)
    if template_name is None:
        raise InstallError(f"No bootstrap template is registered for {relative}")
    return render_template(ROOT / "templates" / "host-bootstrap" / template_name, submodule_path).rstrip()


def plan_changes(target: Path, submodule_path: str, platforms: tuple[str, ...], uninstall: bool) -> tuple[list[tuple[Path, str | None]], list[str]]:
    framework = check_no_symlink_path(target, submodule_path)
    if not uninstall and not (framework / "AGENTS.md").is_file():
        raise InstallError(
            f"Agent-Team policy not found at {framework / 'AGENTS.md'}. "
            "Initialize the submodule first: git submodule update --init --recursive"
        )
    if uninstall and not framework.exists():
        # Uninstall should still be possible after the submodule was removed.
        pass
    changes: list[tuple[Path, str | None]] = []
    messages: list[str] = []
    for relative in selected_files(platforms):
        path = check_no_symlink_path(target, relative)
        existing = None
        if path.exists():
            if not path.is_file():
                raise InstallError(f"Expected a regular file, not a directory: {path}")
            existing = path.read_text(encoding="utf-8")
            if not existing.strip():
                existing = None
        block = build_block(relative, submodule_path)
        if relative in FRONTMATTER:
            if existing is None:
                block = FRONTMATTER[relative] + "\n" + block
            elif not has_frontmatter(existing):
                raise InstallError(
                    f"{relative} must start with valid YAML front matter before Agent-Team can manage its instruction block; "
                    "back up the file and add the platform's required front matter first."
                )
        result = merge_content(existing, block, uninstall=uninstall, generated_frontmatter=FRONTMATTER.get(relative))
        if result != existing:
            changes.append((path, result))
            action = "remove managed block from" if uninstall else ("create" if existing is None else "update managed block in")
            messages.append(f"{action} {path.relative_to(target).as_posix()}")
    return changes, messages


def apply_changes(changes: list[tuple[Path, str | None]], dry_run: bool, target: Path) -> None:
    if dry_run:
        return
    for path, content in changes:
        if content is None:
            if path.exists():
                path.unlink()
            # Remove only now-empty parent directories, stopping at the host
            # root. rmdir fails safely as soon as user content remains.
            parent = path.parent
            while parent != target:
                try:
                    parent.rmdir()
                except OSError:
                    break
                parent = parent.parent
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(path.name + ".agent-team-tmp")
        if temporary.exists() or temporary.is_symlink():
            raise InstallError(f"Refusing to overwrite temporary path: {temporary}")
        temporary.write_text(content, encoding="utf-8", newline="\n")
        os.replace(temporary, path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".", help="host project root (default: current directory)")
    parser.add_argument("--submodule-path", default=".agent-team", help="submodule path relative to host root")
    parser.add_argument("--platforms", default="all", help="all or comma list: " + ", ".join(ALL_PLATFORMS))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="show planned changes without writing")
    mode.add_argument("--check", action="store_true", help="fail with exit 1 if bootstrap files drift")
    mode.add_argument("--uninstall", action="store_true", help="remove only Agent-Team managed blocks")
    args = parser.parse_args(argv)
    try:
        target_input = Path(args.target).expanduser()
        if target_input.is_symlink():
            raise InstallError(f"Target root must not be a symlink: {target_input}")
        target = target_input.resolve(strict=True)
        if not target.is_dir():
            raise InstallError(f"Target is not a directory: {target}")
        submodule_path = safe_relative_path(args.submodule_path, "--submodule-path")
        platforms = parse_platforms(args.platforms)
        changes, messages = plan_changes(target, submodule_path, platforms, args.uninstall)
        state_actions = []
        if not args.uninstall and not args.check:
            state_actions = state_scaffold(target, True)
        if args.check:
            if changes:
                print("Agent-Team host bootstrap drift detected:")
                for message in messages:
                    print(f"  - {message}")
                return 1
            print("Agent-Team host bootstrap is synchronized.")
            return 0
        messages.extend(state_actions)
        if args.dry_run:
            print("Dry run; no files written.")
        for message in messages:
            print(("would " if args.dry_run else "") + message)
        apply_changes(changes, args.dry_run, target)
        if not args.uninstall and not args.dry_run:
            state_scaffold(target, False)
        print("Agent-Team uninstall complete." if args.uninstall else ("Dry run complete." if args.dry_run else "Agent-Team host bootstrap installed."))
        return 0
    except (InstallError, OSError, UnicodeError) as exc:
        print(f"install_into_project: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
