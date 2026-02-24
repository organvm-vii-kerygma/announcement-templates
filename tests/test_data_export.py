"""Tests for kerygma_templates.data_export module."""
import json
from pathlib import Path

import pytest

from kerygma_templates.data_export import (
    build_quality_summary,
    build_template_registry,
    export_all,
)


@pytest.fixture
def templates_dir():
    d = Path(__file__).parent.parent / "templates"
    if not d.is_dir():
        pytest.skip("templates directory not found")
    return d


@pytest.fixture
def tmp_output(tmp_path):
    return tmp_path / "data"


def test_build_template_registry(templates_dir):
    result = build_template_registry(templates_dir)
    assert result["template_count"] > 0
    assert len(result["categories"]) > 0
    assert len(result["all_channels"]) > 0
    assert len(result["templates"]) == result["template_count"]


def test_registry_template_entries_have_required_fields(templates_dir):
    result = build_template_registry(templates_dir)
    for entry in result["templates"]:
        assert "template_id" in entry
        assert "category" in entry
        assert "channels" in entry
        assert "variables" in entry


def test_build_quality_summary(templates_dir):
    result = build_quality_summary(templates_dir)
    assert result["total_checks"] > 0
    assert result["passed"] >= 0
    assert result["failed"] >= 0
    assert result["warnings"] >= 0
    assert result["passed"] + result["failed"] + result["warnings"] == result["total_checks"]


def test_export_all_creates_file(templates_dir, tmp_output):
    paths = export_all(templates_dir, tmp_output)
    assert len(paths) == 1
    assert paths[0].name == "template-registry.json"
    assert paths[0].exists()


def test_export_all_valid_json(templates_dir, tmp_output):
    paths = export_all(templates_dir, tmp_output)
    data = json.loads(paths[0].read_text())
    assert data["organ"] == "VII"
    assert data["organ_name"] == "Kerygma"
    assert data["repo"] == "announcement-templates"
    assert "generated_at" in data


def test_export_all_includes_channel_limits(templates_dir, tmp_output):
    paths = export_all(templates_dir, tmp_output)
    data = json.loads(paths[0].read_text())
    assert "channel_limits" in data
    assert "mastodon" in data["channel_limits"]
    assert data["channel_limits"]["mastodon"] == 500


def test_export_all_includes_quality_summary(templates_dir, tmp_output):
    paths = export_all(templates_dir, tmp_output)
    data = json.loads(paths[0].read_text())
    assert "quality_summary" in data
    assert data["quality_summary"]["total_checks"] > 0
