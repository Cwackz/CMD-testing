import os
from typing import List

def get_system_commands() -> List[str]:
    commands = set()
    
    # Get PATH environment variable
    paths = os.environ.get("PATH", "").split(os.pathsep)
    
    # Search for executables in each PATH directory
    for path in paths:
        if os.path.exists(path):
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isfile(item_path) and os.access(item_path, os.X_OK):
                    commands.add(item)
    
    return sorted(list(commands))