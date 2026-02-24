"""Tests for the CLI module."""


from kerygma_templates.cli import main


class TestCLI:
    def test_list_command(self, capsys):
        main(["list"])
        captured = capsys.readouterr()
        # Should list at least some templates if templates dir exists
        assert "ID" in captured.out or "No templates" in captured.out

    def test_validate_command(self, capsys):
        main(["validate"])
        captured = capsys.readouterr()
        assert "Validated" in captured.out

    def test_render_command(self, capsys):
        main(["render", "repo-launch", "mastodon"])
        captured = capsys.readouterr()
        assert len(captured.out.strip()) > 0

    def test_check_command(self, capsys):
        main(["check", "repo-launch", "mastodon"])
        captured = capsys.readouterr()
        assert "repo-launch" in captured.out

    def test_no_command_shows_help(self, capsys):
        main([])
        captured = capsys.readouterr()
        assert "usage" in captured.out.lower() or "announce" in captured.out.lower()
