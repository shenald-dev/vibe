import pytest
from typer.testing import CliRunner
from vibe.cli import app

runner = CliRunner()

@pytest.fixture(autouse=True)
def mock_sleep(monkeypatch):
    """Mock time.sleep to make tests run instantly."""
    import time
    monkeypatch.setattr(time, "sleep", lambda x: None)

def test_create_default_template():
    result = runner.invoke(app, ["myproject"])
    assert result.exit_code == 0
    assert "Generating Vibe Project:" in result.output
    assert "myproject" in result.output
    assert "created successfully using the react template" in result.output


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
        "Project [red]myproject[/red] created successfully using the react template"
        in result.output
    )


def test_create_invalid_template():
    result = runner.invoke(app, ["myapi", "--template", "invalid"])
    assert result.exit_code != 0
    assert "Invalid value for '--template'" in result.output


def test_create_missing_name_argument():
    result = runner.invoke(app, [])
    assert result.exit_code != 0
    assert "Missing argument 'name'" in result.output
