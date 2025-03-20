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
from commands.ssh import establish_ssh_connection
from commands.raspberry import pi
from datetime import datetime
import platform
import getpass

console = Console()

command_handlers = {
    'flipper': flipper,
    'help': show_help,
    'clear': lambda: (os.system('clear'), console.print(logo, justify="center")),
    'cd': change_directory,
    'ssh': lambda: establish_ssh_connection("", ""),
    'pi': pi
}

style = Style.from_dict({
    'prompt': 'bold #ffffff',
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

INSTALL_VERSION = "1.0"  

def check_installation():
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
    current_dir = os.getcwd()
    last_two_folders = "/".join(current_dir.rstrip("/").split(os.sep)[-2:])
    
    current_time = datetime.now().strftime("%H:%M:%S")
    
    git_info = get_git_branch()
    
    python_ver = get_python_version()

    dir_segment = f'<style fg="black" bg="#81A1C1"> {last_two_folders}</style>'
    time_segment = f'<style fg="black" bg="#5E81AC"> {current_time}</style>'
    git_segment = f'<style fg="black" bg="#B48EAD">{git_info}</style>' if git_info else ''
    python_segment = f'<style fg="black" bg="#A3BE8C">{python_ver}</style>'
    
    return f'{dir_segment}{time_segment}{git_segment}{python_segment} <style fg="#ffffff">❯</style> '

def main():
    if not check_installation():
        subprocess.run(["python3", "install.py"])
    os.system("echo -e '\033]0; Terminal For Newbies\007'") 
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

            if command in command_handlers:
                if command == 'cd':
                    command_handlers[command](args)
                else:
                    command_handlers[command]()
            else:
                run_shell_command(user_input)
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
    
