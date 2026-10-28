#!/usr/bin/env python3
"""End-to-end test using a real local Git submodule in a disposable host repository."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBMODULE_PATH = ".agent-team"


def run(command: list[str], cwd: Path | None = None) -> str:
    print("+ " + " ".join(command), flush=True)
    result = subprocess.run(command, cwd=cwd, text=True, encoding="utf-8", capture_output=True, check=False)
    if result.stdout:
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n", flush=True)
    if result.stderr:
        print(result.stderr, file=sys.stderr, end="" if result.stderr.endswith("\n") else "\n", flush=True)
    print(f"exit: {result.returncode}", flush=True)
    if result.returncode:
        raise RuntimeError("Command failed: " + " ".join(command))
    return result.stdout


def main() -> int:
    if not shutil.which("git") or not shutil.which("python3"):
        print("E2E ERROR: git and python3 are required.", file=sys.stderr)
        return 2
    try:
        run(["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"])
        with tempfile.TemporaryDirectory(prefix="agent-team-submodule-e2e-") as temporary:
            host = Path(temporary) / "host"
            host.mkdir()
            run(["git", "init", "-q"], cwd=host)
            run(["git", "config", "user.name", "Agent-Team E2E"], cwd=host)
            run(["git", "config", "user.email", "agent-team-e2e@example.invalid"], cwd=host)
            (host / "README.md").write_text("# Disposable host project\n", encoding="utf-8")
            run(["git", "add", "README.md"], cwd=host)
            run(["git", "commit", "-m", "test: seed disposable host"], cwd=host)
            run(["git", "-c", "protocol.file.allow=always", "submodule", "add", "--quiet", str(ROOT), SUBMODULE_PATH], cwd=host)
            installer = host / SUBMODULE_PATH / "scripts" / "install_into_project.py"
            run(["python3", str(installer), "--target", str(host)], cwd=host)
            run(["python3", str(installer), "--target", str(host), "--check"], cwd=host)
            run(["python3", str(installer), "--target", str(host), "--uninstall"], cwd=host)
            targets = ["AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursor/rules/agent-team.mdc",
                       ".github/copilot-instructions.md", ".claude/CLAUDE.md",
                       ".claude/skills/agent-team/SKILL.md", ".agents/skills/agent-team/SKILL.md"]
            leftovers = []
            for relative in targets:
                path = host / relative
                if path.is_file():
                    content = path.read_text(encoding="utf-8")
                    if "<!-- agent-team:begin -->" in content or "<!-- agent-team:end -->" in content:
                        leftovers.append(relative)
            if leftovers:
                raise RuntimeError("Managed blocks remain after uninstall: " + ", ".join(leftovers))
            for relative in (".agents", ".claude", ".cursor"):
                if (host / relative).exists():
                    raise RuntimeError(f"Uninstall left installer-only directory behind: {relative}")
            if not (host / ".agent-team-local").is_dir():
                raise RuntimeError("Uninstall unexpectedly removed host-local state.")
            run(["git", "status", "--short"], cwd=host)
            print("E2E PASS: local submodule add, install, --check, and uninstall completed.")
            return 0
    except (OSError, RuntimeError) as exc:
        print(f"E2E FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
