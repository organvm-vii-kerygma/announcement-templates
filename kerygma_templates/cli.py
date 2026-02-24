"""CLI entry point for announcement-templates.

Usage:
    announce list                         — list all registered templates
    announce render <template_id> <channel> — render a template (uses sample context)
    announce validate                     — validate all templates parse correctly
    announce check <template_id> <channel> — run quality checks on rendered output
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from kerygma_templates.engine import TemplateEngine
from kerygma_templates.quality_checker import QualityChecker


def _find_templates_dir() -> Path:
    """Locate the templates/ directory relative to this package."""
    # Look relative to the package installation
    pkg_dir = Path(__file__).parent.parent / "templates"
    if pkg_dir.is_dir():
        return pkg_dir
    # Fallback to cwd
    cwd_dir = Path.cwd() / "templates"
    if cwd_dir.is_dir():
        return cwd_dir
    return pkg_dir


def _sample_context() -> dict[str, object]:
    """Build a sample context for rendering demos."""
    return {
        "repo": {
            "name": "sample-repo",
            "organ": "i-theoria",
            "description": "A sample repository for testing",
            "tier": "standard",
            "url": "https://github.com/organvm-i-theoria/sample-repo",
            "implementation_status": "PRODUCTION",
        },
        "event": {
            "type": "repo-launch",
            "title": "Sample Event",
            "summary": "This is a sample event for template testing.",
            "url": "https://organvm-v-logos.github.io/public-process/",
            "version": "1.0.0",
            "date": "2026-02-17",
            "tags": ["organvm", "launch"],
            "series_name": "Meta-System Essays",
            "part_number": "1",
            "quote": "The system is the artwork.",
            "book_title": "Gödel, Escher, Bach",
            "author": "Douglas Hofstadter",
            "time": "18:00 UTC",
            "location": "Online",
            "duration": "2 hours",
            "contact": "hello@organvm.example",
            "partner_name": "Example Foundation",
            "funder": "Knight Foundation",
        },
        "system": {
            "name": "organvm",
            "total_organs": 8,
            "site_url": "https://organvm-v-logos.github.io/public-process/",
        },
    }


def cmd_list(engine: TemplateEngine) -> None:
    templates = engine.list_templates()
    if not templates:
        print("No templates found.")
        return
    print(f"{'ID':<25} {'Category':<15} {'Channels'}")
    print("-" * 65)
    for t in templates:
        channels = ", ".join(t.channels)
        print(f"{t.template_id:<25} {t.category:<15} {channels}")


def cmd_render(engine: TemplateEngine, template_id: str, channel: str) -> None:
    context = _sample_context()
    result = engine.render(template_id, context, channel)
    print(result.text)
    if result.unresolved_vars:
        print(f"\n[WARN] Unresolved: {', '.join(result.unresolved_vars)}", file=sys.stderr)


def cmd_validate(engine: TemplateEngine) -> None:
    templates = engine.list_templates()
    context = _sample_context()
    errors = 0
    for t in templates:
        for ch in t.channels:
            try:
                engine.render(t.template_id, context, ch)
                print(f"  OK  {t.template_id}/{ch}")
            except Exception as exc:
                print(f"  FAIL {t.template_id}/{ch}: {exc}", file=sys.stderr)
                errors += 1
    total = sum(len(t.channels) for t in templates)
    print(f"\nValidated {total - errors}/{total} template-channel combinations.")
    if errors:
        sys.exit(1)


def cmd_check(engine: TemplateEngine, template_id: str, channel: str) -> None:
    context = _sample_context()
    result = engine.render(template_id, context, channel)
    checker = QualityChecker()
    report = checker.check(result.text, channel, template_id, result.unresolved_vars)
    print(report.summary())
    for c in report.checks:
        status = "PASS" if c.passed else "FAIL"
        print(f"  [{status}] {c.check_name}: {c.message}")
    if not report.passed:
        sys.exit(1)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="announce", description="Kerygma announcement tools")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="List all templates")

    render_p = sub.add_parser("render", help="Render a template")
    render_p.add_argument("template_id")
    render_p.add_argument("channel")

    sub.add_parser("validate", help="Validate all templates")

    check_p = sub.add_parser("check", help="Quality-check a rendered template")
    check_p.add_argument("template_id")
    check_p.add_argument("channel")

    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return

    engine = TemplateEngine()
    templates_dir = _find_templates_dir()
    if templates_dir.is_dir():
        engine.load_directory(templates_dir)

    if args.command == "list":
        cmd_list(engine)
    elif args.command == "render":
        cmd_render(engine, args.template_id, args.channel)
    elif args.command == "validate":
        cmd_validate(engine)
    elif args.command == "check":
        cmd_check(engine, args.template_id, args.channel)


if __name__ == "__main__":
    main()
