import os
from prompt_toolkit.completion import Completer, Completion
from .commands import commands

class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        parts = text.split()
        
        if len(parts) == 0:
            return
        
        elif parts[0] == 'cd':
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
            for command in commands:
                if command.startswith(text):
                    yield Completion(command, start_position=-len(text))