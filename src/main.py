"""
Vibe: The minimalist project engine.
"""
import click
from rich.console import Console

console = Console()

@click.group()
def cli():
    """✨ Vibe: Create with intention."""
    pass

@cli.command()
@click.argument('name')
def init(name):
    """Initialize a new minimalist project."""
    console.print(f"[bold green]Initializing {name}...[/bold green]")
    # Logic to create structure...
    console.print("✨ [bold]Vibe check complete.[/bold] Project ready.")

if __name__ == '__main__':
    cli()
