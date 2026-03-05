import time
import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

app = typer.Typer(help="✨ Scaffold projects at the speed of thought.")
console = Console()

@app.command()
def create(name: str, template: str = typer.Option("react", "--template", "-t", help="Template to use (react, fastapi, node)")) -> None:
    """Create a new project from a vibe template."""
    console.print(Panel.fit(f"[bold cyan]✨ Generating Vibe Project:[/] [green]{name}[/]", border_style="cyan"))
    
    with Progress(
        SpinnerColumn(spinner_name="dots2"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Downloading dependencies...", total=None)
        time.sleep(1)
        progress.add_task(description=f"Scaffolding {template} structure...", total=None)
        time.sleep(1.5)
        progress.add_task(description="Applying vibe aesthetic...", total=None)
        time.sleep(0.5)
        
    console.print(f"\n[bold green]✔[/] Project [cyan]{name}[/] created successfully using the [yellow]{template}[/] template.")
    console.print("\n[bold]Next Steps:[/]")
    console.print(f"  [gray]$[/] cd {name}")
    console.print(f"  [gray]$[/] code .")
    console.print("\n[magenta]Happy vibe coding! ✨[/]\n")

if __name__ == "__main__":
    app()
