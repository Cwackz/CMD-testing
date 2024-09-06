import os
import glob
from rich.console import Console

def flipper():
    device_path = glob.glob('/dev/cu.usbmodemflip_*')
    device_name = device_path[0] if device_path else None

    if device_name:
        os.system(f'screen {device_name}')
    else:
        console = Console()
        console.print("[bold red]No Flipper device found.[/bold red]")