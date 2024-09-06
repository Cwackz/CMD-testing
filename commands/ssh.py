import os
from rich.console import Console

console = Console()



def establish_ssh_connection(hostname, username):
    hostname = input("Enter your ssh hostname: ")
    username = input("Enter your ssh username: ")
    port = input("Enter your ssh port (no need to enter if port 22 is used): ") or 22

    os.system(f"ssh -p {port} {username}@{hostname}")