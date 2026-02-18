"""Tests for the template engine."""

import pytest
from kerygma_templates.engine import (
    TemplateEngine,
    Template,
    parse_frontmatter,
    _resolve_var,
    _is_truthy,
)


class TestParseFrontmatter:
    def test_basic_frontmatter(self):
        text = "---\ntemplate_id: test\ncategory: launch\n---\nBody text"
        meta, body = parse_frontmatter(text)
        assert meta["template_id"] == "test"
        assert meta["category"] == "launch"
        assert body == "Body text"

    def test_no_frontmatter(self):
        text = "Just body text"
        meta, body = parse_frontmatter(text)
        assert meta == {}
        assert body == "Just body text"

    def test_inline_list(self):
        text = "---\nchannels: [mastodon, discord, bluesky]\n---\nBody"
        meta, body = parse_frontmatter(text)
        assert meta["channels"] == ["mastodon", "discord", "bluesky"]

    def test_block_list(self):
        text = "---\nvariables:\n  - repo.name\n  - repo.url\n---\nBody"
        meta, body = parse_frontmatter(text)
        assert meta["variables"] == ["repo.name", "repo.url"]

    def test_boolean_values(self):
        text = "---\nenabled: true\ndisabled: false\n---\nBody"
        meta, _ = parse_frontmatter(text)
        assert meta["enabled"] is True
        assert meta["disabled"] is False

    def test_integer_values(self):
        text = "---\ncount: 42\n---\nBody"
        meta, _ = parse_frontmatter(text)
        assert meta["count"] == 42


class TestResolveVar:
    def test_simple_key(self):
        assert _resolve_var({"name": "test"}, "name") == "test"

    def test_dotted_path(self):
        ctx = {"repo": {"name": "foo", "organ": "bar"}}
        assert _resolve_var(ctx, "repo.name") == "foo"

    def test_missing_key(self):
        assert _resolve_var({"a": 1}, "b") is None

    def test_deep_nesting(self):
        ctx = {"a": {"b": {"c": "deep"}}}
        assert _resolve_var(ctx, "a.b.c") == "deep"


class TestIsTruthy:
    def test_none_is_falsy(self):
        assert _is_truthy(None) is False

    def test_empty_string_is_falsy(self):
        assert _is_truthy("") is False

    def test_nonempty_string_is_truthy(self):
        assert _is_truthy("hello") is True

    def test_empty_list_is_falsy(self):
        assert _is_truthy([]) is False


class TestTemplateFromString:
    def test_parse_template(self):
        text = "---\ntemplate_id: repo-launch\ncategory: launch\nchannels: [mastodon]\nvariables: [repo.name]\n---\n{{ repo.name }}"
        tmpl = Template.from_string(text)
        assert tmpl.template_id == "repo-launch"
        assert tmpl.channels == ["mastodon"]


class TestTemplateEngine:
    def _make_engine(self) -> TemplateEngine:
        engine = TemplateEngine()
        tmpl = Template.from_string(
            "---\ntemplate_id: test\ncategory: test\nchannels: [mastodon, discord]\n---\n"
            "{{#channel mastodon}}Mastodon: {{ title }}{{/channel}}\n"
            "{{#channel discord}}Discord: {{ title }}{{/channel}}"
        )
        engine.register(tmpl)
        return engine

    def test_render_mastodon_channel(self):
        engine = self._make_engine()
        result = engine.render("test", {"title": "Hello"}, "mastodon")
        assert result.text == "Mastodon: Hello"
        assert result.channel == "mastodon"

    def test_render_discord_channel(self):
        engine = self._make_engine()
        result = engine.render("test", {"title": "Hello"}, "discord")
        assert result.text == "Discord: Hello"

    def test_unresolved_var_tracked(self):
        engine = self._make_engine()
        result = engine.render("test", {}, "mastodon")
        assert "title" in result.unresolved_vars

    def test_conditional_true(self):
        engine = TemplateEngine()
        tmpl = Template.from_string(
            "---\ntemplate_id: cond\ncategory: test\nchannels: [mastodon]\n---\n"
            "{{#if show}}Visible{{/if}}"
        )
        engine.register(tmpl)
        result = engine.render("cond", {"show": True}, "mastodon")
        assert "Visible" in result.text

    def test_conditional_false(self):
        engine = TemplateEngine()
        tmpl = Template.from_string(
            "---\ntemplate_id: cond2\ncategory: test\nchannels: [mastodon]\n---\n"
            "{{#if show}}Visible{{#else}}Hidden{{/if}}"
        )
        engine.register(tmpl)
        result = engine.render("cond2", {"show": False}, "mastodon")
        assert "Hidden" in result.text
        assert "Visible" not in result.text

    def test_missing_template_raises(self):
        engine = TemplateEngine()
        with pytest.raises(KeyError):
            engine.render("nonexistent", {}, "mastodon")

    def test_load_directory(self, tmp_path):
        tmpl_dir = tmp_path / "templates"
        tmpl_dir.mkdir()
        (tmpl_dir / "test.md").write_text(
            "---\ntemplate_id: file-test\ncategory: test\nchannels: [mastodon]\n---\n{{ msg }}"
        )
        engine = TemplateEngine()
        count = engine.load_directory(tmpl_dir)
        assert count == 1
        assert engine.get_template("file-test") is not None

    def test_dotted_var_in_render(self):
        engine = TemplateEngine()
        tmpl = Template.from_string(
            "---\ntemplate_id: dot\ncategory: test\nchannels: [mastodon]\n---\n{{ repo.name }}"
        )
        engine.register(tmpl)
        result = engine.render("dot", {"repo": {"name": "my-repo"}}, "mastodon")
        assert result.text == "my-repo"

    def test_sibling_if_blocks(self):
        """Two sibling {{#if}} blocks should render independently."""
        engine = TemplateEngine()
        tmpl = Template.from_string(
            "---\ntemplate_id: sibling\ncategory: test\nchannels: [mastodon]\n---\n"
            "{{#if alpha}}ALPHA{{/if}} mid {{#if beta}}BETA{{/if}}"
        )
        engine.register(tmpl)
        result = engine.render("sibling", {"alpha": True, "beta": True}, "mastodon")
        assert "ALPHA" in result.text
        assert "BETA" in result.text
        assert "mid" in result.text

    def test_sibling_if_one_false(self):
        """One sibling true, one false — only the true block renders."""
        engine = TemplateEngine()
        tmpl = Template.from_string(
            "---\ntemplate_id: sib2\ncategory: test\nchannels: [mastodon]\n---\n"
            "{{#if alpha}}ALPHA{{/if}} mid {{#if beta}}BETA{{/if}}"
        )
        engine.register(tmpl)
        result = engine.render("sib2", {"alpha": True, "beta": False}, "mastodon")
        assert "ALPHA" in result.text
        assert "BETA" not in result.text

    def test_nested_conditionals(self):
        """Nested {{#if}} blocks should resolve from inside out."""
        engine = TemplateEngine()
        tmpl = Template.from_string(
            "---\ntemplate_id: nested\ncategory: test\nchannels: [mastodon]\n---\n"
            "{{#if outer}}OUTER-{{#if inner}}INNER{{/if}}-END{{/if}}"
        )
        engine.register(tmpl)
        result = engine.render("nested", {"outer": True, "inner": True}, "mastodon")
        assert "OUTER-INNER-END" in result.text


class TestFrontmatterEdgeCases:
    def test_negative_number_parsed_as_string(self):
        """isdigit() rejects negative numbers — they stay as strings (known limitation)."""
        text = "---\noffset: -5\n---\nBody"
        meta, _ = parse_frontmatter(text)
        # Current parser treats -5 as string since isdigit() returns False for "-5"
        assert meta["offset"] == "-5"

    def test_float_parsed_as_string(self):
        """Floats are not caught by isdigit() — stored as strings."""
        text = "---\nrate: 3.14\n---\nBody"
        meta, _ = parse_frontmatter(text)
        assert meta["rate"] == "3.14"

    def test_zero_parsed_as_int(self):
        text = "---\ncount: 0\n---\nBody"
        meta, _ = parse_frontmatter(text)
        assert meta["count"] == 0
