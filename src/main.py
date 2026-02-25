"""
Vibe: The minimalist project engine.
"""
import click
import os
import shutil
from rich.console import Console

console = Console()

# Path to templates (relative to this file's location in the dev environment)
# In a real deployed CLI, this would be bundled or in a user config dir.
TEMPLATES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../vault/templates"))

@click.group()
def cli():
    """🚀 Vibe: Create with intention."""
    pass

@cli.command()
@click.argument('name')
@click.option('--template', '-t', default='python', help='Project template to use')
def init(name, template):
    """Initialize a new minimalist project."""
    console.print(f"[bold green]Initializing {name} using '{template}' template...[/bold green]")
    
    target_dir = os.path.abspath(name)
    template_path = os.path.join(TEMPLATES_DIR, template)

    if not os.path.exists(template_path):
        console.print(f"[bold red]Error:[/bold red] Template '{template}' not found in {TEMPLATES_DIR}")
        return

    try:
        if os.path.exists(target_dir):
            console.print(f"[bold yellow]Warning:[/bold yellow] Directory {name} already exists. Skipping folder creation.")
        else:
            os.makedirs(target_dir)
        
        # Copy template files
        for item in os.listdir(template_path):
            s = os.path.join(template_path, item)
            d = os.path.join(target_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
                
        console.print("🚀 [bold]Vibe check complete.[/bold] Project ready.")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == '__main__':
    cli()
