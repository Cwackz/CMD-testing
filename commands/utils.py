from rich.console import Console
from rich.table import Table

console = Console()

def show_help():
    commands = [
        ("flipper", "Opens a screen session with the flipper device."),
        ("help", "Show this help message."),
        ("clear", "Clear the screen."),
        ("cd <path>", "Change directory to the specified path."),
        ("new tab", "Opens a new tab in the terminal."),
        ("exit", "Exit the CLI."),
        ("ssh", "Establish an SSH connection to a remote server."),
        
    ]

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Command", style="bold cyan")
    table.add_column("Description")

    for command, description in commands:
        table.add_row(command, description)

    console.print(table)

