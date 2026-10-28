"""Tests for host-project submodule installation, preservation, and lifecycle."""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "install_into_project.py"
SPEC = importlib.util.spec_from_file_location("install_into_project", SCRIPT)
assert SPEC and SPEC.loader
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallIntoProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.host = Path(self.temp.name) / "host"
        self.host.mkdir()
        (self.host / ".agent-team").mkdir()
        (self.host / ".agent-team" / "AGENTS.md").write_text("# Canonical Agent-Team policy\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def run_installer(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--target", str(self.host), *args],
            capture_output=True, text=True, encoding="utf-8", check=False,
        )

    def test_install_creates_bootstraps_and_local_scaffold(self):
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn(installer.BEGIN, (self.host / "AGENTS.md").read_text(encoding="utf-8"))
        self.assertIn(".agent-team/AGENTS.md", (self.host / "AGENTS.md").read_text(encoding="utf-8"))
        self.assertTrue((self.host / "CLAUDE.md").is_file())
        self.assertTrue((self.host / "GEMINI.md").is_file())
        self.assertTrue((self.host / ".cursor/rules/agent-team.mdc").is_file())
        self.assertTrue((self.host / ".github/copilot-instructions.md").is_file())
        for name in installer.LOCAL_DIRS:
            self.assertTrue((self.host / ".agent-team-local" / name).is_dir())

    def test_install_is_idempotent(self):
        first = self.run_installer()
        self.assertEqual(first.returncode, 0, first.stderr + first.stdout)
        before = {p.relative_to(self.host): p.read_bytes() for p in self.host.rglob("*") if p.is_file()}
        second = self.run_installer()
        self.assertEqual(second.returncode, 0, second.stderr + second.stdout)
        after = {p.relative_to(self.host): p.read_bytes() for p in self.host.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_existing_user_content_is_preserved(self):
        original = "# My project instructions\nUse our architecture and style.\n"
        (self.host / "AGENTS.md").write_text(original, encoding="utf-8")
        result = self.run_installer("--platforms", "codex")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        actual = (self.host / "AGENTS.md").read_text(encoding="utf-8")
        self.assertTrue(actual.startswith(original))
        self.assertEqual(actual.count(original), 1)
        self.assertIn(installer.BEGIN, actual)

    def test_dry_run_writes_nothing(self):
        result = self.run_installer("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertEqual(list(self.host.iterdir()), [self.host / ".agent-team"])

    def test_check_detects_drift(self):
        self.assertEqual(self.run_installer().returncode, 0)
        path = self.host / "AGENTS.md"
        path.write_text(path.read_text(encoding="utf-8").replace("canonical policy", "Drifted policy"), encoding="utf-8")
        result = self.run_installer("--check")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("drift detected", result.stdout.lower())

    def test_uninstall_removes_only_managed_blocks(self):
        original = "# User-owned instructions\nKeep this paragraph.\n"
        (self.host / "AGENTS.md").write_text(original, encoding="utf-8")
        self.assertEqual(self.run_installer("--platforms", "codex").returncode, 0)
        result = self.run_installer("--platforms", "codex", "--uninstall")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((self.host / "AGENTS.md").read_text(encoding="utf-8"), original)
        self.assertTrue((self.host / ".agent-team-local").is_dir())

    def test_broken_marker_errors_without_changing_files(self):
        (self.host / "AGENTS.md").write_text("user text\n<!-- agent-team:begin -->\n", encoding="utf-8")
        before = {p.relative_to(self.host): p.read_bytes() for p in self.host.rglob("*") if p.is_file()}
        result = self.run_installer()
        self.assertEqual(result.returncode, 2)
        self.assertIn("marker", result.stderr.lower())
        after = {p.relative_to(self.host): p.read_bytes() for p in self.host.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_custom_submodule_path(self):
        (self.host / ".agent-team").rename(self.host / "vendor" if (self.host / "vendor").exists() else self.host / "agent-team-framework")
        result = self.run_installer("--submodule-path", "agent-team-framework", "--platforms", "codex")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("agent-team-framework/AGENTS.md", (self.host / "AGENTS.md").read_text(encoding="utf-8"))

    def test_missing_submodule_has_actionable_error(self):
        (self.host / ".agent-team" / "AGENTS.md").unlink()
        result = self.run_installer()
        self.assertEqual(result.returncode, 2)
        self.assertIn("git submodule update --init --recursive", result.stderr)

    def test_unknown_platform_is_usage_error(self):
        result = self.run_installer("--platforms", "not-a-platform")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Invalid --platforms", result.stderr)


if __name__ == "__main__":
    unittest.main()
