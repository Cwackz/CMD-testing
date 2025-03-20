import os
from prompt_toolkit.completion import Completer, Completion
from .command_utils import get_system_commands

class CommandCompleter(Completer):
    def __init__(self):
        self.custom_commands = ['flipper', 'clear', 'help', 'exit', 'cd', 'ssh', 'pi']
        self.system_commands = get_system_commands()
        self.all_commands = self.custom_commands + self.system_commands

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        text_lower = text.lower()
        parts = text.split()
        
        if len(parts) == 0:
            return
        
        elif parts[0].lower() == 'cd':
            prefix = ' '.join(parts[1:]) if len(parts) > 1 else ''
            if not prefix:
                directory = "./"
            else:
                directory = os.path.expanduser(prefix)
            
            try:
                with os.scandir(directory) as it:
                    for entry in it:
                        if entry.is_dir():
                            display_name = os.path.join(directory, entry.name)
                            if display_name.startswith(prefix):
                                yield Completion(display_name, start_position=-len(prefix))
            except FileNotFoundError:
                pass
        
        else:
            for command in self.all_commands:
                if command.lower().startswith(text_lower):
                    yield Completion(command, start_position=-len(text))