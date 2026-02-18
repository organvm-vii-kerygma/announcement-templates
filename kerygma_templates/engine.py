"""Regex-based template engine for announcement rendering.

Supports:
- Variable interpolation: {{ var }} and {{ var.path }}
- Conditionals: {{#if condition}} ... {{/if}} and {{#if condition}} ... {{#else}} ... {{/if}}
- Channel blocks: {{#channel mastodon}} ... {{/channel}}
- No external dependencies — stdlib only.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# --- YAML frontmatter parser (minimal, no pyyaml dependency) ---

_FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse YAML-like frontmatter from template text.

    Returns (metadata_dict, body_text). Handles simple key: value,
    lists (- item), and comma-separated inline lists [a, b].
    """
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    raw = match.group(1)
    body = text[match.end():]
    meta: dict[str, Any] = {}
    current_key: str | None = None
    current_list: list[str] | None = None

    for line in raw.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # List continuation (indented "- item")
        if stripped.startswith("- ") and current_key is not None and current_list is not None:
            current_list.append(stripped[2:].strip())
            meta[current_key] = current_list
            continue

        # Key-value line
        if ":" in stripped:
            # Flush any pending list
            current_list = None

            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip()
            current_key = key

            if not value:
                # Next lines might be a list
                current_list = []
                meta[key] = current_list
            elif value.startswith("[") and value.endswith("]"):
                # Inline list: [a, b, c]
                items = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
                meta[key] = items
            elif value.lower() in ("true", "false"):
                meta[key] = value.lower() == "true"
            elif value.isdigit():
                meta[key] = int(value)
            else:
                meta[key] = value.strip("'\"")

    return meta, body


# --- Template engine ---

_VAR_RE = re.compile(r"\{\{\s*([\w.]+)\s*\}\}")
_IF_RE = re.compile(
    r"\{\{#if\s+([\w.]+)\s*\}\}(.*?)(?:\{\{#else\}\}(.*?))?\{\{/if\}\}",
    re.DOTALL,
)
_CHANNEL_RE = re.compile(
    r"\{\{#channel\s+([\w]+)\s*\}\}(.*?)\{\{/channel\}\}",
    re.DOTALL,
)


def _resolve_var(context: dict[str, Any], path: str) -> Any:
    """Resolve a dotted variable path against a nested context dict."""
    parts = path.split(".")
    current: Any = context
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return None
    return current


def _is_truthy(value: Any) -> bool:
    """Determine if a value should be considered truthy for conditionals."""
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return len(value) > 0
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return bool(value)


@dataclass
class RenderResult:
    """Result of rendering a template."""
    template_id: str
    channel: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)
    unresolved_vars: list[str] = field(default_factory=list)


@dataclass
class Template:
    """A parsed template with frontmatter metadata and body."""
    template_id: str
    category: str
    channels: list[str]
    variables: list[str]
    body: str
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_file(cls, path: Path) -> Template:
        """Load and parse a template from a file."""
        text = path.read_text(encoding="utf-8")
        return cls.from_string(text)

    @classmethod
    def from_string(cls, text: str) -> Template:
        """Parse a template from a string."""
        meta, body = parse_frontmatter(text)
        return cls(
            template_id=meta.get("template_id", "unknown"),
            category=meta.get("category", "general"),
            channels=meta.get("channels", []),
            variables=meta.get("variables", []),
            body=body,
            metadata=meta,
        )


class TemplateEngine:
    """Renders templates with variable interpolation, conditionals, and channel blocks."""

    def __init__(self) -> None:
        self._templates: dict[str, Template] = {}

    def register(self, template: Template) -> None:
        self._templates[template.template_id] = template

    def load_directory(self, directory: Path) -> int:
        """Load all .md templates from a directory tree. Returns count loaded."""
        count = 0
        for path in sorted(directory.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            if text.startswith("---\n"):
                tmpl = Template.from_file(path)
                self.register(tmpl)
                count += 1
        return count

    def get_template(self, template_id: str) -> Template | None:
        return self._templates.get(template_id)

    def list_templates(self) -> list[Template]:
        return list(self._templates.values())

    def render(self, template_id: str, context: dict[str, Any], channel: str) -> RenderResult:
        """Render a template for a specific channel with the given context."""
        tmpl = self._templates.get(template_id)
        if tmpl is None:
            raise KeyError(f"Template '{template_id}' not found")

        text = tmpl.body
        # 1. Extract channel block (or use full body if no channel blocks)
        text = self._extract_channel(text, channel)
        # 2. Process conditionals
        text = self._process_conditionals(text, context)
        # 3. Interpolate variables
        text, unresolved = self._interpolate(text, context)
        # 4. Clean up whitespace
        text = self._clean(text)

        return RenderResult(
            template_id=template_id,
            channel=channel,
            text=text,
            metadata=tmpl.metadata,
            unresolved_vars=unresolved,
        )

    def _extract_channel(self, text: str, channel: str) -> str:
        """Extract the content for the specified channel block."""
        matches = list(_CHANNEL_RE.finditer(text))
        if not matches:
            return text

        for match in matches:
            if match.group(1) == channel:
                return match.group(2).strip()

        # Channel not found — return text outside channel blocks
        result = _CHANNEL_RE.sub("", text)
        return result.strip()

    def _process_conditionals(self, text: str, context: dict[str, Any]) -> str:
        """Process {{#if}} ... {{/if}} blocks."""
        def replacer(match: re.Match[str]) -> str:
            var_path = match.group(1)
            true_block = match.group(2)
            false_block = match.group(3) or ""
            value = _resolve_var(context, var_path)
            if _is_truthy(value):
                return true_block.strip()
            return false_block.strip()

        # Repeatedly process until no more conditionals (handles nesting)
        prev = ""
        while prev != text:
            prev = text
            text = _IF_RE.sub(replacer, text)
        return text

    def _interpolate(self, text: str, context: dict[str, Any]) -> tuple[str, list[str]]:
        """Replace {{ var.path }} with values from context. Returns (text, unresolved_vars)."""
        unresolved: list[str] = []

        def replacer(match: re.Match[str]) -> str:
            path = match.group(1)
            value = _resolve_var(context, path)
            if value is None:
                unresolved.append(path)
                return match.group(0)  # Leave unresolved vars as-is
            return str(value)

        result = _VAR_RE.sub(replacer, text)
        return result, unresolved

    def _clean(self, text: str) -> str:
        """Clean up excess blank lines."""
        lines = text.split("\n")
        cleaned: list[str] = []
        prev_blank = False
        for line in lines:
            is_blank = line.strip() == ""
            if is_blank and prev_blank:
                continue
            cleaned.append(line)
            prev_blank = is_blank
        return "\n".join(cleaned).strip()

    @property
    def template_count(self) -> int:
        return len(self._templates)
