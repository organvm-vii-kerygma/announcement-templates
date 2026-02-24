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


class TestBuildContextWithProfile:
    """Tests for per-project voice variables via profile parameter."""

    def _make_profile(self, **kwargs):
        """Create a minimal profile-like object."""
        from types import SimpleNamespace
        defaults = {
            "profile_id": "test",
            "display_name": "Test Project",
            "voice": {
                "tone": "friendly",
                "hashtags": ["#test", "#project"],
                "tagline": "A test project",
            },
        }
        defaults.update(kwargs)
        return SimpleNamespace(**defaults)

    def test_profile_adds_project_context(self):
        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        event = EventContext(event_type="repo-launch", repo_name="recursive-engine")
        profile = self._make_profile()
        ctx = loader.build_context(event, profile=profile)
        assert "project" in ctx
        assert ctx["project"]["name"] == "Test Project"
        assert ctx["project"]["tagline"] == "A test project"
        assert ctx["project"]["tone"] == "friendly"
        assert "#test" in ctx["project"]["hashtags"]
        assert "#project" in ctx["project"]["hashtags"]

    def test_no_profile_no_project_key(self):
        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        event = EventContext(event_type="repo-launch", repo_name="recursive-engine")
        ctx = loader.build_context(event)
        assert "project" not in ctx

    def test_profile_none_voice(self):
        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        event = EventContext(event_type="repo-launch", repo_name="recursive-engine")
        profile = self._make_profile(voice=None)
        ctx = loader.build_context(event, profile=profile)
        assert ctx["project"]["tagline"] == ""
        assert ctx["project"]["tone"] == "neutral"

    def test_profile_with_real_project_profile(self):
        """Test with an actual ProjectProfile dataclass if available."""
        try:
            from kerygma_profiles.registry import ProjectProfile
        except ImportError:
            return  # skip if not installed

        loader = RegistryLoader(FIXTURES / "sample_registry.json")
        event = EventContext(event_type="repo-launch", repo_name="recursive-engine")
        profile = ProjectProfile(
            profile_id="real",
            display_name="Real Product",
            organ="III",
            repos=["my-repo"],
            voice={"tone": "professional", "hashtags": ["#real"], "tagline": "Real deal"},
            platforms={},
            channels=[],
            calendar_events=[],
        )
        ctx = loader.build_context(event, profile=profile)
        assert ctx["project"]["name"] == "Real Product"
        assert ctx["project"]["tagline"] == "Real deal"
