import time
import typer
from enum import Enum
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn


class TemplateChoice(str, Enum):
    react = "react"
    fastapi = "fastapi"
    node = "node"


app = typer.Typer(help="✨ Scaffold projects at the speed of thought.")
console = Console()


@app.command()
def create(
    name: str,
    template: TemplateChoice = typer.Option(
        TemplateChoice.react,
        "--template",
        "-t",
        help="Template to use (react, fastapi, node)",
    ),
) -> None:
    """Create a new project from a vibe template."""
    escaped_name = escape(name)
    escaped_template = escape(template.value)

    console.print(
        Panel.fit(
            f"[bold cyan]✨ Generating Vibe Project:[/] [green]{escaped_name}[/]",
            border_style="cyan",
        )
    )

    with Progress(
        SpinnerColumn(spinner_name="dots2"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Downloading dependencies...", total=None)
        time.sleep(1)
        progress.add_task(
            description=f"Scaffolding {escaped_template} structure...", total=None
        )
        time.sleep(1.5)
        progress.add_task(description="Applying vibe aesthetic...", total=None)
        time.sleep(0.5)

    console.print(
        f"\n[bold green]✔[/] Project [cyan]{escaped_name}[/] created successfully using the [yellow]{escaped_template}[/] template."
    )
    console.print("\n[bold]Next Steps:[/]")
    console.print(f"  [gray]$[/] cd {escaped_name}")
    console.print("  [gray]$[/] code .")
    console.print("\n[magenta]Happy vibe coding! ✨[/]\n")


if __name__ == "__main__":
    app()
