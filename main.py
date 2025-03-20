#!/usr/bin/env python

import os
import subprocess
from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.panel import Panel
from commands.command_completer import CommandCompleter
from commands.flipper import flipper
from commands.utils import show_help
from commands.directory import change_directory
from commands.shell_command import run_shell_command
from commands.commands import commands
from commands.ssh import establish_ssh_connection
from datetime import datetime
import platform
import getpass

console = Console()

style = Style.from_dict({
    'prompt': 'bold #00ff00',
})

command_completer = CommandCompleter()
session = PromptSession()

logo = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠴⠒⠒⠒⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠁⠀⠀⣠⠖⠛⠛⠲⢤⠀⠀⠀⣰⠚⠛⢷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⣸⠃⠀⠀⢀⣀⠈⢧⣠⣤⣯⢠⣤⠘⣆⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⡇⠀⠀⠀⠻⠟⠠⣏⣀⣀⣨⡇⠉⢀⣿⠀⠀⠀
⠀⠀⠀⠀⢀⡟⠀⠀⠹⡄⠀⠀⠀⠀⠀⠉⠑⠚⠉⠀⣠⡞⢿⠀⠀⠀
⠀⠀⠀⢀⡼⠁⠀⠀⠀⠙⠳⢤⡄⠀⠀⠀⠀⠀⠀⠀⠁⠙⢦⠳⣄⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠤⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠙⡆
⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⡇
⠀⠀⣏⠀⠀⠀⠀⠲⣄⡀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⢸⠀⢀⡼⠁
⢀⡴⢿⠀⠀⠀⠀⠀⢸⠟⢦⡀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠘⠗⣿⠁⠀
⠸⣦⡘⣦⠀⠀⠀⠀⣸⣄⠀⡉⠓⠚⠀⠀⠀⠀⠀⠀⠀⠀⡴⢹⣦⡀
⠀⠀⠉⠛⠳⢤⣴⠾⠁⠈⠟⠉⣇⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⣠⠞⠁
⠀⠀⠀⠀⠀⠀⠙⢧⣀⠀⠀⣠⠏⠀⠀⢀⣀⣠⠴⠛⠓⠚⠋⠀⠀⠀
"""

INSTALL_VERSION = "1.0"  # This should match the version in install.py

def check_installation():
    # Check if the installation has been run for the current version
    if not os.path.isfile(".install_version"):
        return False
    
    with open(".install_version", "r") as f:
        installed_version = f.read().strip()
    
    return installed_version == INSTALL_VERSION

def get_git_branch():
    try:
        with open(os.devnull, 'w') as fnull:
            branch = subprocess.check_output(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                stderr=fnull
            ).decode('utf-8').strip()
        return f" 󰊢 {branch}"
    except:
        return ""

def get_python_version():
    version = platform.python_version()
    return f" 󰌠 {version}"

def create_powerlevel_prompt():
    # Get current directory name
    current_dir = os.path.basename(os.getcwd())
    if not current_dir:  # If we're at root
        current_dir = os.getcwd()

    # Get username
    username = getpass.getuser()
    
    # Get current time
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Get git branch
    git_info = get_git_branch()
    
    # Get Python version
    python_ver = get_python_version()

    # Create segments
    user_segment = f'<style fg="black" bg="#00875f">{username}</style>'
    dir_segment = f'<style fg="black" bg="#d75f00"> {current_dir}</style>'
    time_segment = f'<style fg="black" bg="#5f8700"> {current_time}</style>'
    git_segment = f'<style fg="black" bg="#0087af">{git_info}</style>' if git_info else ''
    python_segment = f'<style fg="black" bg="#af5f00">{python_ver}</style>'
    
    return f'{user_segment}{dir_segment}{time_segment}{git_segment}{python_segment} <style fg="#00ff00">❯</style> '

# Update the main loop to use the new prompt
def main():
    if not check_installation():
        # Run install.py if the current version is not installed
        subprocess.run(["python3", "install.py"])
    os.system("echo -e '\033]0; CMD\007'") #title of program
    os.system("clear")
    console.print(logo, justify="center")
    while True:
        try:
            user_input = session.prompt(
                HTML(create_powerlevel_prompt()),
                completer=command_completer,
                style=style
            )
            if user_input.strip().lower() == 'exit':
                break
            args = user_input.split()

            if not args:
                continue

            command = args[0].lower()

            if command == 'flipper':
                flipper()
            elif command == 'help':
                show_help()
            elif command == 'clear':
                os.system('clear')
                console.print(logo, justify="center")
            elif command == 'cd':
                change_directory(args)
            elif command == "ssh":
                establish_ssh_connection("", "")
            elif command == "newtab":
                script = f"""
                osascript -e 'tell application "System Events" to keystroke "t" using command down' \
                        -e 'delay 0.5' \
                        -e 'tell application "Terminal" to do script "python3 {os.path.abspath(__file__)}" in front window'\
                        -e 'tell application "Terminal" to do script "clear" in front window'
                """
                os.system(script)
            # everything under here will not act as a custom command
            elif command in commands:
                os.system(user_input)
            else:
                run_shell_command(user_input)
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
    