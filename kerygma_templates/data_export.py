"""Generate static data artifacts for announcement-templates.

Produces:
  data/template-registry.json — template inventory, quality summary, channel limits

No external dependencies required.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from kerygma_templates.cli import _sample_context
from kerygma_templates.engine import TemplateEngine
from kerygma_templates.quality_checker import CHANNEL_LIMITS, QualityChecker


def _find_templates_dir() -> Path:
    """Locate the templates/ directory relative to this package."""
    pkg_dir = Path(__file__).parent.parent / "templates"
    if pkg_dir.is_dir():
        return pkg_dir
    cwd_dir = Path.cwd() / "templates"
    if cwd_dir.is_dir():
        return cwd_dir
    return pkg_dir


def build_template_registry(templates_dir: Path | None = None) -> dict[str, Any]:
    """Load all templates and build a registry with metadata."""
    templates_dir = templates_dir or _find_templates_dir()
    engine = TemplateEngine()
    if templates_dir.is_dir():
        engine.load_directory(templates_dir)

    templates = engine.list_templates()
    categories = sorted({t.category for t in templates})
    all_channels = sorted({ch for t in templates for ch in t.channels})

    template_entries = []
    for t in templates:
        template_entries.append({
            "template_id": t.template_id,
            "category": t.category,
            "channels": t.channels,
            "variables": t.variables,
        })

    return {
        "template_count": len(templates),
        "categories": categories,
        "all_channels": all_channels,
        "templates": template_entries,
    }


def build_quality_summary(templates_dir: Path | None = None) -> dict[str, Any]:
    """Run quality checks on all templates with sample context."""
    templates_dir = templates_dir or _find_templates_dir()
    engine = TemplateEngine()
    if templates_dir.is_dir():
        engine.load_directory(templates_dir)

    templates = engine.list_templates()
    context = _sample_context()
    checker = QualityChecker()

    total_checks = 0
    passed = 0
    failed = 0
    warnings = 0

    for t in templates:
        for ch in t.channels:
            try:
                result = engine.render(t.template_id, context, ch)
                report = checker.check(
                    result.text, ch, t.template_id, result.unresolved_vars,
                )
                for check in report.checks:
                    total_checks += 1
                    if check.passed:
                        passed += 1
                    elif check.severity == "warning":
                        warnings += 1
                    else:
                        failed += 1
            except Exception:
                total_checks += 1
                failed += 1

    return {
        "total_checks": total_checks,
        "passed": passed,
        "failed": failed,
        "warnings": warnings,
    }


def export_all(
    templates_dir: Path | None = None,
    output_dir: Path | None = None,
) -> list[Path]:
    """Generate all data artifacts and return output paths."""
    templates_dir = templates_dir or _find_templates_dir()
    output_dir = output_dir or Path(__file__).parent.parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []

    registry = build_template_registry(templates_dir)
    quality = build_quality_summary(templates_dir)

    data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "organ": "VII",
        "organ_name": "Kerygma",
        "repo": "announcement-templates",
        **registry,
        "channel_limits": CHANNEL_LIMITS,
        "quality_summary": quality,
    }

    registry_path = output_dir / "template-registry.json"
    registry_path.write_text(json.dumps(data, indent=2) + "\n")
    outputs.append(registry_path)

    return outputs


def main() -> None:
    """CLI entry point for data export."""
    paths = export_all()
    for p in paths:
        print(f"Written: {p}")


if __name__ == "__main__":
    main()
