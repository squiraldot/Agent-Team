"""Unit tests for the static repository validator."""
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_repo.py"
SPEC = importlib.util.spec_from_file_location("validate_repo", SCRIPT)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class RepositoryValidatorTests(unittest.TestCase):
    def test_required_files_are_present_in_repository(self):
        missing = [p for p in validator.REQUIRED if not (validator.ROOT / p).is_file()]
        self.assertEqual(missing, [])

    def test_example_config_keeps_cross_provider_fallback_disabled(self):
        content = (validator.ROOT / "config/agent-team.example.yaml").read_text(encoding="utf-8")
        self.assertIn("fallback_enabled: false", content)

    def test_secret_patterns_do_not_match_core_docs(self):
        for relative in ("AGENTS.md", "README.md", "docs/SECURITY.md"):
            content = (validator.ROOT / relative).read_text(encoding="utf-8")
            for pattern in validator.SECRET_PATTERNS:
                self.assertIsNone(pattern.search(content), f"Potential secret-like value in {relative}")


if __name__ == "__main__":
    unittest.main()
