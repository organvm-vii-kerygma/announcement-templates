"""Parametrized validation tests for all 15 template files."""

import pytest
from pathlib import Path

from kerygma_templates.engine import TemplateEngine, Template

TEMPLATES_DIR = Path(__file__).parent.parent / "templates"

# Discover all template files
TEMPLATE_FILES = sorted(TEMPLATES_DIR.rglob("*.md")) if TEMPLATES_DIR.exists() else []

SAMPLE_CONTEXT = {
    "repo": {
        "name": "test-repo",
        "organ": "i-theoria",
        "description": "A test repository",
        "tier": "standard",
        "url": "https://github.com/organvm-i-theoria/test-repo",
        "implementation_status": "PRODUCTION",
    },
    "event": {
        "type": "repo-launch",
        "title": "Test Event",
        "summary": "A test event summary.",
        "url": "https://example.com/test",
        "version": "1.0.0",
        "date": "2026-02-17",
        "tags": ["organvm", "test"],
        "organ": "i-theoria",
        "series_name": "Test Series",
        "part_number": "1",
        "quote": "Test quote.",
        "book_title": "Test Book",
        "author": "Test Author",
        "time": "18:00 UTC",
        "location": "Online",
        "duration": "2 hours",
        "contact": "test@example.com",
        "partner_name": "Test Partner",
        "funder": "Test Funder",
    },
    "system": {
        "name": "organvm",
        "total_organs": 8,
    },
}


@pytest.mark.parametrize("template_file", TEMPLATE_FILES, ids=lambda p: p.stem)
def test_template_parses(template_file: Path):
    """Each template file should parse without errors."""
    tmpl = Template.from_file(template_file)
    assert tmpl.template_id != "unknown", f"{template_file.name} missing template_id"
    assert len(tmpl.channels) > 0, f"{template_file.name} has no channels"


@pytest.mark.parametrize("template_file", TEMPLATE_FILES, ids=lambda p: p.stem)
def test_template_renders_all_channels(template_file: Path):
    """Each template should render for every declared channel."""
    tmpl = Template.from_file(template_file)
    engine = TemplateEngine()
    engine.register(tmpl)

    for channel in tmpl.channels:
        result = engine.render(tmpl.template_id, SAMPLE_CONTEXT, channel)
        assert len(result.text.strip()) > 0, (
            f"{tmpl.template_id}/{channel} rendered empty"
        )


def test_all_15_templates_discovered():
    """Verify we have exactly 15 template files."""
    assert len(TEMPLATE_FILES) == 15, (
        f"Expected 15 templates, found {len(TEMPLATE_FILES)}: "
        f"{[f.stem for f in TEMPLATE_FILES]}"
    )
