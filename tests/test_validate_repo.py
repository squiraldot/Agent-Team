"""Unit tests for repository validation helpers."""
import importlib.util
import tempfile
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

    def test_routing_config_has_per_role_budgets_and_disabled_cross_provider_fallback(self):
        errors = validator.collect_errors()
        routing_errors = [e for e in errors if "fallback" in e or "model tier" in e or "role " in e and "config" in e]
        self.assertEqual(routing_errors, [])

    def test_secret_scan_passes_current_repository(self):
        self.assertEqual(validator.secret_errors(validator.ROOT), [])

    def test_front_matter_rejects_invalid_semver(self):
        _, error = validator.parse_front_matter("---\nname: demo\ndescription: demo\nversion: nope\nowner: team\nstatus: active\n---\n")
        self.assertIn("semantic versioning", error)

    def test_front_matter_accepts_valid_semver(self):
        fields, error = validator.parse_front_matter("---\nname: demo\ndescription: demo\nversion: 1.2.3\nowner: team\nstatus: active\n---\n")
        self.assertIsNone(error)
        self.assertEqual(fields["name"], "demo")

    def test_role_folder_requires_contract_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "agents" / "demo"
            folder.mkdir(parents=True)
            (folder / "role.md").write_text("role", encoding="utf-8")
            self.assertTrue(validator.required_role_files(root))

    def test_broken_relative_link_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "guide.md").write_text("[missing](nope.md)", encoding="utf-8")
            self.assertTrue(validator.broken_links(root))

    def test_template_placeholder_link_is_not_treated_as_a_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENTS.md").write_text("[policy]({{SUBMODULE_PATH}}/AGENTS.md)", encoding="utf-8")
            self.assertEqual(validator.broken_links(root), [])

    def test_secret_scan_detects_key_marker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            marker = "-----" + "BEGIN " + "PRIVATE KEY" + "-----"
            (root / "sample.md").write_text(marker, encoding="utf-8")
            self.assertTrue(validator.secret_errors(root))

    def test_placeholder_scan_detects_unfilled_marker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "draft.md").write_text("TODO: write policy", encoding="utf-8")
            self.assertTrue(validator.placeholder_errors(root))

    def test_index_check_requires_phase_eight_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("empty", encoding="utf-8")
            self.assertTrue(validator.index_errors(root))

    def test_current_tree_has_no_broken_links_or_placeholders(self):
        self.assertEqual(validator.broken_links(validator.ROOT), [])
        self.assertEqual(validator.placeholder_errors(validator.ROOT), [])


    def test_routing_validator_rejects_unknown_fallback_tier(self):
        content = (validator.ROOT / "config/agent-team.example.yaml").read_text(encoding="utf-8")
        mutated = content.replace("    fallback_order: [balanced, fast]\n    max_input_tokens: 24000", "    fallback_order: [balanced, imaginary]\n    max_input_tokens: 24000", 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "config").mkdir()
            (root / "config/agent-team.example.yaml").write_text(mutated, encoding="utf-8")
            errors = validator.collect_errors(root)
            self.assertTrue(any("unknown fallback tier" in e for e in errors))

    def test_routing_validator_rejects_primary_tier_in_fallback_order(self):
        content = (validator.ROOT / "config/agent-team.example.yaml").read_text(encoding="utf-8")
        mutated = content.replace("    fallback_order: [balanced, fast]\n    max_input_tokens: 24000", "    fallback_order: [deep-reasoning, fast]\n    max_input_tokens: 24000", 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "config").mkdir()
            (root / "config/agent-team.example.yaml").write_text(mutated, encoding="utf-8")
            errors = validator.collect_errors(root)
            self.assertTrue(any("must not include its primary tier" in e for e in errors))


    def test_development_standards_are_indexed(self):
        self.assertEqual(validator.index_errors(validator.ROOT), [])
        for relative in (
            "docs/standards/README.md",
            "docs/standards/web.md",
            "docs/standards/android.md",
            "docs/standards/plugins-modules.md",
            "docs/standards/software.md",
        ):
            self.assertTrue((validator.ROOT / relative).is_file(), relative)


    def test_phase_twelve_governance_docs_are_indexed(self):
        self.assertEqual(validator.index_errors(validator.ROOT), [])
        for relative in (
            "docs/CONFLICT_RESOLUTION.md",
            "docs/IP_AND_LICENSING.md",
            "docs/VERSIONING.md",
            "MIGRATION.md",
        ):
            self.assertTrue((validator.ROOT / relative).is_file(), relative)

    def test_phase_eleven_standards_and_templates_are_indexed(self):
        self.assertEqual(validator.index_errors(validator.ROOT), [])
        for relative in ("docs/standards/ui-ux.md", "docs/standards/graphic-branding.md", "docs/standards/illustration.md", "docs/standards/content.md", "docs/DELIVERABLE_FORMATS.md", "templates/handoff-spec.md", "templates/image-brief.md", "templates/brand-kit/README.md"):
            self.assertTrue((validator.ROOT / relative).is_file(), relative)

    def test_phase_thirteen_demo_pipeline_is_complete_and_valid(self):
        self.assertEqual(validator.demo_errors(validator.ROOT), [])
        self.assertEqual(validator.index_errors(validator.ROOT), [])
        for relative in validator.DEMO_REQUIRED:
            self.assertTrue((validator.ROOT / relative).is_file(), relative)

    def test_phase_thirteen_demo_validator_rejects_missing_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            errors = validator.demo_errors(Path(tmp))
            self.assertTrue(any("Missing demo artifact" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
