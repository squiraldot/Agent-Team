"""Unit tests for deterministic native-adapter generation and drift detection."""
import importlib.util
import tempfile
import shutil
import unittest
from unittest import mock
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_platforms.py"
SPEC = importlib.util.spec_from_file_location("sync_platforms", SCRIPT)
assert SPEC and SPEC.loader
sync_platforms = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync_platforms)


class SyncPlatformsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "AGENTS.md").write_text("# Canonical policy\n", encoding="utf-8")
        shutil.copytree(SCRIPT.parents[1] / "templates" / "host-bootstrap", self.root / "templates" / "host-bootstrap")
        # Route default-argument CLI calls to the disposable root as well; never
        # let a test invoke sync_platforms.main() against the real repository.
        self.original_root = sync_platforms.ROOT
        sync_platforms.ROOT = self.root

    def tearDown(self):
        sync_platforms.ROOT = self.original_root
        self.temp.cleanup()

    def test_sync_generates_all_adapters(self):
        self.assertEqual(sync_platforms.sync(self.root), [])
        for relative, expected in sync_platforms.render_adapters(self.root).items():
            self.assertEqual((self.root / relative).read_text(encoding="utf-8"), expected)

    def test_check_passes_when_synchronized(self):
        sync_platforms.sync(self.root)
        self.assertEqual(sync_platforms.sync(self.root, check=True), [])

    def test_check_detects_missing_and_modified_adapters(self):
        sync_platforms.sync(self.root)
        (self.root / "CLAUDE.md").write_text("manual edit\n", encoding="utf-8")
        (self.root / "GEMINI.md").unlink()
        errors = sync_platforms.sync(self.root, check=True)
        self.assertIn("drift: CLAUDE.md", errors)
        self.assertIn("missing: GEMINI.md", errors)

    def test_canonical_policy_change_marks_adapters_stale(self):
        sync_platforms.sync(self.root)
        (self.root / "AGENTS.md").write_text("# Updated canonical policy\n", encoding="utf-8")
        self.assertTrue(sync_platforms.sync(self.root, check=True))

    def test_cli_check_returns_nonzero_on_drift(self):
        sync_platforms.sync(self.root)
        with mock.patch.object(sync_platforms, "ROOT", self.root):
            self.assertEqual(sync_platforms.main(["--check"]), 0)
            (self.root / "CLAUDE.md").write_text("drift\\n", encoding="utf-8")
            self.assertEqual(sync_platforms.main(["--check"]), 1)

    def test_check_detects_bootstrap_template_drift(self):
        path = self.root / "templates/host-bootstrap/AGENTS.md.md"
        path.write_text(path.read_text(encoding="utf-8") + "drift\n", encoding="utf-8")
        self.assertIn("bootstrap template drift: templates/host-bootstrap/AGENTS.md.md", sync_platforms.bootstrap_template_errors(self.root))

    def test_missing_canonical_policy_fails_clearly(self):
        (self.root / "AGENTS.md").unlink()
        with self.assertRaises(FileNotFoundError):
            sync_platforms.render_adapters(self.root)


if __name__ == "__main__":
    unittest.main()
