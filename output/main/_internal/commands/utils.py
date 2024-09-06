from rich.console import Console
from rich.table import Table

console = Console()

def show_help():
    help_text = """
    Available commands:
    
    [bold cyan]flipper[/bold cyan]
    Opens a screen session with the flipper device.

    [bold cyan]calc <operation> <x> <y>[/bold cyan]
    Perform a calculation where operation is one of [add, sub, mul, div].
    
    [bold cyan]help[/bold cyan]
    Show this help message.

    [bold cyan]clear[/bold cyan]
    Clear the screen.
    
    [bold cyan]cd <path>[/bold cyan]
    Change directory to the specified path.

    [bold cyan] new tab[/bold cyan]
    Opens a new tab in the terminal.
    
    [bold cyan]exit[/bold cyan]
    Exit the CLI.
    """
    console.print(help_text)
