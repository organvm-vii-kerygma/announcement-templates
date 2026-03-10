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
**Org:** `organvm-vii-kerygma` | **Repo:** `announcement-templates`

### Edges
- **Produces** → `ORGAN-IV`: template_pack

### Siblings in Marketing
`social-automation`, `distribution-strategy`, `.github`

### Governance
- *Standard ORGANVM governance applies*

*Last synced: 2026-03-08T20:11:35Z*

## Session Review Protocol

At the end of each session that produces or modifies files:
1. Run `organvm session review --latest` to get a session summary
2. Check for unimplemented plans: `organvm session plans --project .`
3. Export significant sessions: `organvm session export <id> --slug <slug>`
4. Run `organvm prompts distill --dry-run` to detect uncovered operational patterns

Transcripts are on-demand (never committed):
- `organvm session transcript <id>` — conversation summary
- `organvm session transcript <id> --unabridged` — full audit trail
- `organvm session prompts <id>` — human prompts only


## Active Directives

| Scope | Phase | Name | Description |
|-------|-------|------|-------------|
| system | any | prompting-standards | Prompting Standards |
| system | any | research-standards-bibliography | APPENDIX: Research Standards Bibliography |
| system | any | research-standards | METADOC: Architectural Typology & Research Standards |
| system | any | sop-ecosystem | METADOC: SOP Ecosystem — Taxonomy, Inventory & Coverage |
| system | any | autopoietic-systems-diagnostics | SOP: Autopoietic Systems Diagnostics (The Mirror of Eternity) |
| system | any | cicd-resilience-and-recovery | SOP: CI/CD Pipeline Resilience & Recovery |
| system | any | cross-agent-handoff | SOP: Cross-Agent Session Handoff |
| system | any | document-audit-feature-extraction | SOP: Document Audit & Feature Extraction |
| system | any | essay-publishing-and-distribution | SOP: Essay Publishing & Distribution |
| system | any | market-gap-analysis | SOP: Full-Breath Market-Gap Analysis & Defensive Parrying |
| system | any | pitch-deck-rollout | SOP: Pitch Deck Generation & Rollout |
| system | any | promotion-and-state-transitions | SOP: Promotion & State Transitions |
| system | any | repo-onboarding-and-habitat-creation | SOP: Repo Onboarding & Habitat Creation |
| system | any | research-to-implementation-pipeline | SOP: Research-to-Implementation Pipeline (The Gold Path) |
| system | any | security-and-accessibility-audit | SOP: Security & Accessibility Audit |
| system | any | session-self-critique | session-self-critique |
| system | any | source-evaluation-and-bibliography | SOP: Source Evaluation & Annotated Bibliography (The Refinery) |
| system | any | stranger-test-protocol | SOP: Stranger Test Protocol |
| system | any | strategic-foresight-and-futures | SOP: Strategic Foresight & Futures (The Telescope) |
| system | any | typological-hermeneutic-analysis | SOP: Typological & Hermeneutic Analysis (The Archaeology) |

Linked skills: evaluation-to-growth


**Prompting (Anthropic)**: context 200K tokens, format: XML tags, thinking: extended thinking (budget_tokens)

<!-- ORGANVM:AUTO:END -->


## ⚡ Conductor OS Integration
This repository is a managed component of the ORGANVM meta-workspace.
- **Orchestration:** Use `conductor patch` for system status and work queue.
- **Lifecycle:** Follow the `FRAME -> SHAPE -> BUILD -> PROVE` workflow.
- **Governance:** Promotions are managed via `conductor wip promote`.
- **Intelligence:** Conductor MCP tools are available for routing and mission synthesis.
