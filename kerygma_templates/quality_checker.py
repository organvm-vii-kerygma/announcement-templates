"""Quality checker for rendered announcement content.

Validates character limits, unresolved variables, anti-patterns,
hashtag counts, and link presence before distribution.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

# Platform character limits
CHANNEL_LIMITS: dict[str, int] = {
    "mastodon": 500,
    "discord": 4096,
    "linkedin": 1300,
    "bluesky": 300,
    "twitter": 280,
}

# Words to flag in announcements
ANTI_PATTERNS: list[str] = [
    "todo",
    "fixme",
    "hack",
    "placeholder",
    "lorem ipsum",
    "tbd",
    "coming soon",
    "stay tuned",
    "click here",
    "buy now",
]


@dataclass
class CheckResult:
    """Result of a single quality check."""
    check_name: str
    passed: bool
    message: str
    severity: str = "error"  # "error", "warning", "info"


@dataclass
class QualityReport:
    """Aggregated quality report for a rendered announcement."""
    template_id: str
    channel: str
    checks: list[CheckResult] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks if c.severity == "error")

    @property
    def warnings(self) -> list[CheckResult]:
        return [c for c in self.checks if not c.passed and c.severity == "warning"]

    @property
    def errors(self) -> list[CheckResult]:
        return [c for c in self.checks if not c.passed and c.severity == "error"]

    def summary(self) -> str:
        total = len(self.checks)
        passed = sum(1 for c in self.checks if c.passed)
        status = "PASS" if self.passed else "FAIL"
        return f"[{status}] {self.template_id}/{self.channel}: {passed}/{total} checks passed"


class QualityChecker:
    """Runs quality checks on rendered announcement text."""

    def __init__(
        self,
        channel_limits: dict[str, int] | None = None,
        anti_patterns: list[str] | None = None,
    ) -> None:
        self._limits = channel_limits or CHANNEL_LIMITS
        self._anti_patterns = anti_patterns or ANTI_PATTERNS

    def check(
        self,
        text: str,
        channel: str,
        template_id: str = "",
        unresolved_vars: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> QualityReport:
        """Run all quality checks on rendered text."""
        report = QualityReport(template_id=template_id, channel=channel)

        report.checks.append(self._check_char_limit(text, channel))
        report.checks.append(self._check_not_empty(text))
        report.checks.append(self._check_unresolved_vars(text, unresolved_vars))
        report.checks.append(self._check_anti_patterns(text))
        report.checks.append(self._check_has_link(text))
        report.checks.append(self._check_hashtag_count(text, channel))

        return report

    def _check_char_limit(self, text: str, channel: str) -> CheckResult:
        limit = self._limits.get(channel, 0)
        if limit == 0:
            return CheckResult("char_limit", True, f"No limit defined for {channel}", "info")

        length = len(text)
        if length <= limit:
            return CheckResult("char_limit", True, f"{length}/{limit} characters")
        return CheckResult(
            "char_limit", False,
            f"Exceeds {channel} limit: {length}/{limit} characters ({length - limit} over)",
        )

    def _check_not_empty(self, text: str) -> CheckResult:
        if text.strip():
            return CheckResult("not_empty", True, "Content is not empty")
        return CheckResult("not_empty", False, "Rendered content is empty")

    def _check_unresolved_vars(
        self, text: str, unresolved: list[str] | None,
    ) -> CheckResult:
        if unresolved:
            return CheckResult(
                "unresolved_vars", False,
                f"Unresolved variables: {', '.join(unresolved)}",
            )
        # Also check for leftover {{ }} patterns in text
        leftover = re.findall(r"\{\{.*?\}\}", text)
        if leftover:
            return CheckResult(
                "unresolved_vars", False,
                f"Found unresolved template syntax: {', '.join(leftover)}",
            )
        return CheckResult("unresolved_vars", True, "All variables resolved")

    def _check_anti_patterns(self, text: str) -> CheckResult:
        lower = text.lower()
        found = [p for p in self._anti_patterns if p in lower]
        if found:
            return CheckResult(
                "anti_patterns", False,
                f"Anti-patterns found: {', '.join(found)}",
                severity="warning",
            )
        return CheckResult("anti_patterns", True, "No anti-patterns found")

    def _check_has_link(self, text: str) -> CheckResult:
        if "http://" in text or "https://" in text:
            return CheckResult("has_link", True, "Contains at least one link")
        return CheckResult(
            "has_link", False,
            "No links found — announcements should link to canonical content",
            severity="warning",
        )

    def _check_hashtag_count(self, text: str, channel: str) -> CheckResult:
        hashtags = re.findall(r"#\w+", text)
        count = len(hashtags)

        if channel == "mastodon" and count > 10:
            return CheckResult(
                "hashtag_count", False,
                f"Too many hashtags for Mastodon: {count} (max 10)",
                severity="warning",
            )
        if channel == "linkedin" and count > 5:
            return CheckResult(
                "hashtag_count", False,
                f"Too many hashtags for LinkedIn: {count} (max 5)",
                severity="warning",
            )
        return CheckResult("hashtag_count", True, f"{count} hashtags — acceptable for {channel}")
