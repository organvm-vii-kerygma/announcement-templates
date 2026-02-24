"""Registry loader for building template context from the organ registry.

Loads registry-v2.json and event data to produce the context dict
that feeds into template rendering.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class RepoContext:
    """Context extracted from a single registry entry."""
    name: str
    organ: str
    description: str
    tier: str
    url: str
    implementation_status: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class EventContext:
    """Context for an announcement event."""
    event_type: str
    repo_name: str = ""
    organ: str = ""
    title: str = ""
    summary: str = ""
    url: str = ""
    version: str = ""
    date: str = ""
    tags: list[str] = field(default_factory=list)
    extras: dict[str, Any] = field(default_factory=dict)


class RegistryLoader:
    """Loads organ registry JSON and builds template context dicts."""

    def __init__(self, registry_path: Path | None = None) -> None:
        self._registry: dict[str, Any] = {}
        self._repos: dict[str, RepoContext] = {}
        if registry_path and registry_path.exists():
            self.load(registry_path)

    def load(self, path: Path) -> int:
        """Load registry JSON. Returns number of repo entries parsed."""
        raw = json.loads(path.read_text(encoding="utf-8"))
        self._registry = raw

        # Parse repos from each organ section
        count = 0
        organs = raw.get("organs", raw)
        if isinstance(organs, dict):
            for organ_key, organ_data in organs.items():
                repos = organ_data.get("repos", []) if isinstance(organ_data, dict) else []
                for repo in repos:
                    if isinstance(repo, dict) and "name" in repo:
                        ctx = RepoContext(
                            name=repo["name"],
                            organ=organ_key,
                            description=repo.get("description", ""),
                            tier=repo.get("tier", "standard"),
                            url=repo.get("url", ""),
                            implementation_status=repo.get("implementation_status", ""),
                            metadata=repo,
                        )
                        self._repos[repo["name"]] = ctx
                        count += 1
        return count

    def get_repo(self, name: str) -> RepoContext | None:
        return self._repos.get(name)

    def list_repos(self, organ: str | None = None) -> list[RepoContext]:
        if organ:
            return [r for r in self._repos.values() if r.organ == organ]
        return list(self._repos.values())

    def build_context(
        self,
        event: EventContext,
        repo_name: str | None = None,
        profile: Any | None = None,
    ) -> dict[str, Any]:
        """Build a full template context dict from event + registry data.

        Args:
            event: Event context with type, title, summary, etc.
            repo_name: Repository name for registry lookup.
            profile: Optional ProjectProfile for per-project voice variables.
        """
        ctx: dict[str, Any] = {
            "event": {
                "type": event.event_type,
                "title": event.title or f"New {event.event_type}",
                "summary": event.summary,
                "url": event.url,
                "version": event.version,
                "date": event.date or datetime.now().strftime("%Y-%m-%d"),
                "tags": event.tags,
            },
        }
        ctx["event"].update(event.extras)

        # Add repo context if available
        target = repo_name or event.repo_name
        repo = self._repos.get(target) if target else None
        if repo:
            ctx["repo"] = {
                "name": repo.name,
                "organ": repo.organ,
                "description": repo.description,
                "tier": repo.tier,
                "url": repo.url,
                "implementation_status": repo.implementation_status,
            }
        else:
            ctx["repo"] = {
                "name": target or "",
                "organ": event.organ,
                "description": "",
                "tier": "",
                "url": event.url,
            }

        # System-level metadata
        ctx["system"] = {
            "name": "organvm",
            "total_organs": 8,
            "site_url": "https://organvm-v-logos.github.io/public-process/",
            "org_prefix": "organvm",
        }

        # Per-project voice variables from profile
        if profile:
            voice = getattr(profile, "voice", {}) or {}
            ctx["project"] = {
                "name": getattr(profile, "display_name", ""),
                "tagline": voice.get("tagline", ""),
                "hashtags": " ".join(voice.get("hashtags", [])),
                "tone": voice.get("tone", "neutral"),
            }

        return ctx

    @property
    def repo_count(self) -> int:
        return len(self._repos)

    @property
    def raw_registry(self) -> dict[str, Any]:
        return self._registry
