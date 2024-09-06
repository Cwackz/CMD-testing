import os
from rich.console import Console

console = Console()

def change_directory(args):
    if len(args) != 2:
        console.print("[bold red]Error:[/bold red] cd command requires exactly one argument.")
        return

    new_path = args[1]
    try:
        os.chdir(new_path)
        console.print(f"[bold green]Changed directory to {new_path}[/bold green]")
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] Directory '{new_path}' not found.")
    except NotADirectoryError:
        console.print(f"[bold red]Error:[/bold red] '{new_path}' is not a directory.")
    except PermissionError:
        console.print(f"[bold red]Error:[/bold red] Permission denied to access '{new_path}'.")
