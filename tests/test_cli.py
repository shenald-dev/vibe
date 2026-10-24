from typer.testing import CliRunner
from vibe.cli import app

runner = CliRunner()

def test_create_default_template():
    result = runner.invoke(app, ["myproject"])
    assert result.exit_code == 0
    assert "Generating Vibe Project:" in result.stdout
    assert "myproject" in result.stdout
    assert "created successfully using the react template" in result.stdout

def test_create_custom_template():
    result = runner.invoke(app, ["myapi", "--template", "fastapi"])
    assert result.exit_code == 0
    assert "Generating Vibe Project:" in result.stdout
    assert "myapi" in result.stdout
    assert "created successfully using the fastapi template" in result.stdout
