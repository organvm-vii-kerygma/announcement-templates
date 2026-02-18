"""Tests for the registry loader."""

import json
from pathlib import Path

from kerygma_templates.registry_loader import RegistryLoader, EventContext

FIXTURES = Path(__file__).parent / "fixtures"


class TestRegistryLoader:
    def test_load_sample_registry(self):
        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        assert loader.repo_count == 3

    def test_get_repo(self):
        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        repo = loader.get_repo("recursive-engine")
        assert repo is not None
        assert repo.organ == "i-theoria"
        assert repo.tier == "flagship"

    def test_list_repos_by_organ(self):
        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        repos = loader.list_repos(organ="i-theoria")
        assert len(repos) == 2

    def test_build_context_with_repo(self):
        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        event = EventContext(
            event_type="repo-launch",
            repo_name="recursive-engine",
            title="Engine Launch",
            summary="The recursive engine is live.",
            url="https://example.com",
        )
        ctx = loader.build_context(event)
        assert ctx["repo"]["name"] == "recursive-engine"
        assert ctx["repo"]["tier"] == "flagship"
        assert ctx["event"]["title"] == "Engine Launch"
        assert ctx["system"]["total_organs"] == 8

    def test_build_context_missing_repo(self):
        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        event = EventContext(
            event_type="essay-published",
            repo_name="nonexistent",
            title="Test",
        )
        ctx = loader.build_context(event)
        assert ctx["repo"]["name"] == "nonexistent"

    def test_load_from_path(self, tmp_path):
        data = {"organs": {"test": {"repos": [{"name": "r1", "description": "d"}]}}}
        path = tmp_path / "registry.json"
        path.write_text(json.dumps(data))
        loader = RegistryLoader()
        count = loader.load(path)
        assert count == 1

    def test_missing_file_no_crash(self):
        loader = RegistryLoader(Path("/nonexistent/file.json"))
        assert loader.repo_count == 0

    def test_event_context_extras(self):
        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        event = EventContext(
            event_type="essay-published",
            repo_name="recursive-engine",
            extras={"custom_key": "custom_value"},
        )
        ctx = loader.build_context(event)
        assert ctx["event"]["custom_key"] == "custom_value"
