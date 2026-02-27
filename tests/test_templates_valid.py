"""Parametrized validation tests for all 17 template files."""

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
    "digest": {
        "week_label": "Feb 24 – Mar 1, 2026",
        "essay_1_title": "First Essay Title",
        "essay_1_url": "https://example.com/essay-1",
        "essay_1_summary": "Summary of the first essay.",
        "essay_2_title": "Second Essay Title",
        "essay_2_url": "https://example.com/essay-2",
        "essay_2_summary": "Summary of the second essay.",
        "essay_3_title": "Third Essay Title",
        "essay_3_url": "https://example.com/essay-3",
        "essay_3_summary": "Summary of the third essay.",
        "site_url": "https://organvm-v-logos.github.io/public-process/",
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


def test_all_17_templates_discovered():
    """Verify we have exactly 17 template files."""
    assert len(TEMPLATE_FILES) == 17, (
        f"Expected 17 templates, found {len(TEMPLATE_FILES)}: "
        f"{[f.stem for f in TEMPLATE_FILES]}"
    )
