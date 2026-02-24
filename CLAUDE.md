# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

`kerygma_templates` — the template engine and announcement library for ORGAN-VII (Kerygma). Renders multi-channel announcements from Markdown templates with YAML frontmatter. Stdlib-only (no Jinja2, no pyyaml for template parsing).

## Package Structure

Source is in `kerygma_templates/`, installed as the `kerygma_templates` package:

| Module | Purpose |
|--------|---------|
| `engine.py` | `TemplateEngine` — loads `.md` templates, renders with `{{ var }}` interpolation, `{{#if}}` conditionals, `{{#channel name}}` blocks. Custom frontmatter parser using regex (not pyyaml). |
| `quality_checker.py` | `QualityChecker` — validates rendered text: char limits per platform (`CHANNEL_LIMITS`), unresolved vars, anti-patterns, hashtag counts, link presence. Returns `QualityReport`. |
| `registry_loader.py` | `RegistryLoader` — loads ORGAN-IV's `registry-v2.json`, builds template context dicts. `EventContext` dataclass carries event metadata. `build_context()` merges event + repo + system data. |
| `cli.py` | CLI entry point (`announce`): `list`, `render <id> <channel>`, `validate`, `check <id> <channel>`. Uses `sample_context()` for demo rendering. |
| `data_export.py` | Generates `data/template-registry.json` — template inventory, channel limits, quality summary with per-failure detail. CLI: `announce-export` or `python -m kerygma_templates.data_export`. |

## Templates

Templates live in `templates/` organized by category: `launch/`, `release/`, `essay/`, `community/`, `institutional/`. Each `.md` file has YAML frontmatter defining `template_id`, `channels` (list), and `variables` (list). Template IDs use kebab-case (e.g., `essay-announce`, `repo-launch`).

Template syntax:
- `{{ var.path }}` — dot-path variable interpolation
- `{{#if condition}} ... {{#else}} ... {{/if}}` — conditionals (supports nesting)
- `{{#channel mastodon}} ... {{/channel}}` — channel-specific blocks (engine extracts matching block, discards others)

## Development Commands

```bash
# Install (from superproject root or this directory)
pip install -e .[dev]

# Tests
pytest tests/ -v
pytest tests/test_engine.py::TestTemplateEngine::test_render_with_channel -v

# Lint
ruff check kerygma_templates/
```

## Key Design Details

- **Frontmatter parser** in `engine.py:parse_frontmatter()` is a minimal custom implementation — handles `key: value`, `- item` lists, inline `[a, b]` lists, booleans, and integers. Not a full YAML parser.
- **Quality checker** treats `severity="error"` checks as blocking (fail the report) and `severity="warning"` as advisory. Platform char limits: Mastodon 500, Discord 4096, Bluesky 300, Twitter 280, LinkedIn 1300, Ghost unlimited.
- **Template loading** via `TemplateEngine.load_directory()` recurses `.md` files that start with `---\n` frontmatter. Templates without frontmatter are skipped.
- **No runtime dependencies** — the package has zero `dependencies` in `pyproject.toml`. Dev dependencies are pytest and ruff.

## Test Structure

Tests in `tests/` with `fixtures/` directory for test templates:
- `test_engine.py` — rendering, interpolation, conditionals, channel blocks
- `test_quality_checker.py` — char limits, anti-patterns, unresolved vars
- `test_registry_loader.py` — registry loading, context building
- `test_cli.py` — CLI subcommand smoke tests
- `test_templates_valid.py` — validates all templates in `templates/` parse and render

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** ORGAN-VII (Marketing) | **Tier:** archive | **Status:** GRADUATED
**Org:** `unknown` | **Repo:** `announcement-templates`

### Edges
- *No inter-repo edges declared in seed.yaml*

### Siblings in Marketing
`social-automation`, `distribution-strategy`, `.github`

### Governance
- *Standard ORGANVM governance applies*

*Last synced: 2026-02-24T12:41:28Z*
<!-- ORGANVM:AUTO:END -->
