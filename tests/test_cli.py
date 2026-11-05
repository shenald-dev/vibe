import pytest
from typer.testing import CliRunner
from vibe.cli import app

runner = CliRunner()


@pytest.fixture(autouse=True)
def mock_sleep(monkeypatch):
    """Mock time.sleep to make tests run instantly."""
    import time

    monkeypatch.setattr(time, "sleep", lambda _: None)


def test_create_default_template():
    result = runner.invoke(app, ["myproject"])
    assert result.exit_code == 0
    assert "Generating Vibe Project:" in result.output
    assert "myproject" in result.output
    assert "created successfully using the react template" in result.output


def test_create_uppercase_template():
    result = runner.invoke(app, ["myproject", "--template", "REACT"])
    assert result.exit_code != 0
    assert "Invalid value for '--template'" in result.output


def test_create_ansi_escape_injection():
    result = runner.invoke(app, ["\033[2J\033[Hcleared"])
    assert result.exit_code != 0
    assert "Project name cannot contain control characters." in result.output


def test_create_control_characters():
    result = runner.invoke(app, ["my\x07project"])
    assert result.exit_code != 0
    assert "Project name cannot contain control characters." in result.output


def test_create_cd_command_escaping_single_quote():
    result = runner.invoke(app, ["my'[red]project"])
    assert result.exit_code == 0
    assert "cd 'my'\"'\"'[red]project'" in result.output


def test_create_cd_command_escaping():
    result = runner.invoke(app, ["my new project"])
    assert result.exit_code == 0
    assert "cd 'my new project'" in result.output


def test_create_name_with_spaces_in_middle():
    result = runner.invoke(app, ["my new project"])
    assert result.exit_code == 0
    assert "Generating Vibe Project: my new project" in result.output
    assert (
        "Project my new project created successfully using the react template"
        in result.output
    )


def test_create_unexpected_extra_arguments():
    result = runner.invoke(app, ["create", "my-new-project"])
    assert result.exit_code != 0
    assert "Got unexpected extra argument" in result.output


def test_create_name_with_whitespace():
    result = runner.invoke(app, ["  myproject  "])
    assert result.exit_code == 0
    assert "Generating Vibe Project: myproject" in result.output
    assert (
        "Project myproject created successfully using the react template"
        in result.output
    )


def test_create_custom_template():
    result = runner.invoke(app, ["myapi", "--template", "fastapi"])
    assert result.exit_code == 0
    assert "Generating Vibe Project:" in result.output
    assert "myapi" in result.output
    assert "created successfully using the fastapi template" in result.output


def test_create_escape_rich_markup_injection():
    result = runner.invoke(app, ["[red]myproject[/red]"])
    assert result.exit_code == 0
    assert "Generating Vibe Project: [red]myproject[/red]" in result.output
    assert (
        "Project [red]myproject[/red] created successfully "
        "using the react template" in result.output
    )


def test_create_invalid_template():
    result = runner.invoke(app, ["myapi", "--template", "invalid"])
    assert result.exit_code != 0
    assert "Invalid value for '--template'" in result.output


def test_create_missing_name_argument():
    result = runner.invoke(app, [])
    assert result.exit_code != 0
    assert "Missing argument 'name'" in result.output


def test_create_node_template():
    result = runner.invoke(app, ["mynodeapp", "--template", "node"])
    assert result.exit_code == 0
    assert "Generating Vibe Project:" in result.output
    assert "mynodeapp" in result.output
    assert "created successfully using the node template" in result.output


def test_help_flag():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Create a new project from a vibe template." in result.output
    assert "--template" in result.output


def test_create_empty_name_argument():
    result = runner.invoke(app, ["  "])
    assert result.exit_code != 0
    assert "Project name cannot be empty." in result.output


def test_create_exact_empty_string_name_argument():
    result = runner.invoke(app, [""])
    assert result.exit_code != 0
    assert "Project name cannot be empty." in result.output


def test_create_name_with_newlines_and_tabs():
    result = runner.invoke(app, ["\n\t  \n"])
    assert result.exit_code != 0
    assert "Project name cannot be empty." in result.output


def test_create_short_template_flag():
    result = runner.invoke(app, ["myproject", "-t", "react"])
    assert result.exit_code == 0
    assert "Generating Vibe Project:" in result.output
    assert "myproject" in result.output
    assert "created successfully using the react template" in result.output


def test_create_keyboard_interrupt(monkeypatch):
    def mock_sleep_interrupt(_):
        raise KeyboardInterrupt()

    import time

    monkeypatch.setattr(time, "sleep", mock_sleep_interrupt)

    result = runner.invoke(app, ["myproject"])
    assert result.exit_code == 130
    assert "Scaffolding aborted by user." in result.output
