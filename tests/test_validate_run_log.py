"""Tests for the standard-library run-log validator."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_run_log", ROOT / "scripts" / "validate_run_log.py")
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

def sample():
    return {
        "task_id": "task-test-001",
        "started_at": "2026-10-28T09:00:00Z",
        "finished_at": "2026-10-28T09:01:00Z",
        "roles_used": ["router"],
        "sources_consulted": [{"source": "https://example.org", "title": "Docs"}],
        "decisions": ["Used official docs."],
        "tools_called": [{"name": "fetch", "capability": "fetch", "status": "success", "duration_ms": 10}],
        "approvals_requested": [{"action": "deploy", "status": "not_requested"}],
        "outcome": {"status": "success", "summary": "Done."},
    }

class RunLogValidatorTests(unittest.TestCase):
    def test_template_is_valid(self):
        data = json.loads((ROOT / "templates" / "run-log-template.json").read_text(encoding="utf-8"))
        self.assertEqual(validator.validate_log(data), [])
    def test_valid_log(self):
        self.assertEqual(validator.validate_log(sample()), [])
    def test_requires_fields(self):
        self.assertTrue(validator.validate_log({"task_id": "x"}))
    def test_rejects_finished_before_started(self):
        data = sample()
        data["finished_at"] = "2026-10-28T08:59:00Z"
        self.assertTrue(any("must not precede" in e for e in validator.validate_log(data)))
    def test_rejects_missing_timezone(self):
        data = sample()
        data["started_at"] = "2026-10-28T09:00:00"
        self.assertTrue(any("timezone" in e for e in validator.validate_log(data)))
    def test_rejects_email_personal_data(self):
        data = sample()
        data["outcome"]["summary"] = "Contact user@example.com"
        self.assertTrue(any("email address" in e for e in validator.validate_log(data)))
    def test_rejects_secret_pattern(self):
        data = sample()
        data["decisions"] = ["api" + "_key='abcdefghijklmnop12345'"]
        self.assertTrue(any("secret pattern" in e for e in validator.validate_log(data)))
    def test_rejects_bad_tool_duration(self):
        data = sample()
        data["tools_called"][0]["duration_ms"] = -1
        self.assertTrue(any("duration_ms" in e for e in validator.validate_log(data)))
    def test_cli_rejects_invalid_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text("{", encoding="utf-8")
            self.assertEqual(validator.main([str(path)]), 1)

if __name__ == "__main__":
    unittest.main()
