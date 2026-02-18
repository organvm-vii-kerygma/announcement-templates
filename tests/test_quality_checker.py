"""Tests for the quality checker."""

from kerygma_templates.quality_checker import QualityChecker, CHANNEL_LIMITS


class TestQualityChecker:
    def _checker(self) -> QualityChecker:
        return QualityChecker()

    def test_passing_check(self):
        checker = self._checker()
        report = checker.check(
            "Check out our new release: https://example.com #organvm",
            "mastodon",
            "test-template",
        )
        assert report.passed

    def test_char_limit_exceeded(self):
        checker = self._checker()
        text = "x" * 501 + " https://example.com"
        report = checker.check(text, "mastodon", "test")
        errors = [c for c in report.checks if c.check_name == "char_limit"]
        assert not errors[0].passed

    def test_char_limit_ok(self):
        checker = self._checker()
        report = checker.check("Short https://example.com", "mastodon", "test")
        limit_check = next(c for c in report.checks if c.check_name == "char_limit")
        assert limit_check.passed

    def test_empty_content_fails(self):
        checker = self._checker()
        report = checker.check("", "mastodon", "test")
        empty_check = next(c for c in report.checks if c.check_name == "not_empty")
        assert not empty_check.passed

    def test_unresolved_vars_fail(self):
        checker = self._checker()
        report = checker.check(
            "Hello {{ name }} https://example.com",
            "mastodon",
            "test",
            unresolved_vars=["name"],
        )
        var_check = next(c for c in report.checks if c.check_name == "unresolved_vars")
        assert not var_check.passed

    def test_anti_pattern_warning(self):
        checker = self._checker()
        report = checker.check(
            "This is a TODO placeholder https://example.com",
            "mastodon",
            "test",
        )
        ap_check = next(c for c in report.checks if c.check_name == "anti_patterns")
        assert not ap_check.passed
        assert ap_check.severity == "warning"

    def test_no_link_warning(self):
        checker = self._checker()
        report = checker.check("No links here at all", "mastodon", "test")
        link_check = next(c for c in report.checks if c.check_name == "has_link")
        assert not link_check.passed
        assert link_check.severity == "warning"

    def test_excessive_hashtags_warning(self):
        checker = self._checker()
        tags = " ".join(f"#tag{i}" for i in range(12))
        text = f"Message {tags} https://example.com"
        report = checker.check(text, "mastodon", "test")
        hash_check = next(c for c in report.checks if c.check_name == "hashtag_count")
        assert not hash_check.passed

    def test_report_summary(self):
        checker = self._checker()
        report = checker.check("Good content https://example.com", "mastodon", "test-id")
        summary = report.summary()
        assert "test-id" in summary
        assert "mastodon" in summary

    def test_unknown_channel_no_limit(self):
        checker = self._checker()
        report = checker.check("Content https://example.com", "unknown_channel", "test")
        limit_check = next(c for c in report.checks if c.check_name == "char_limit")
        assert limit_check.passed
        assert limit_check.severity == "info"
