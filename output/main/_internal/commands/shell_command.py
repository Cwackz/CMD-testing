import subprocess
from rich.console import Console

console = Console()

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        console.print(result.stdout)
        if result.stderr:
            console.print(f"[bold red]{result.stderr}[/bold red]")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
