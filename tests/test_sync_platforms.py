"""Unit tests for deterministic native-adapter generation and drift detection."""
import importlib.util
import tempfile
import unittest
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

    def tearDown(self):
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

    def test_missing_canonical_policy_fails_clearly(self):
        (self.root / "AGENTS.md").unlink()
        with self.assertRaises(FileNotFoundError):
            sync_platforms.render_adapters(self.root)


if __name__ == "__main__":
    unittest.main()
