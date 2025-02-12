import os
import sys
import time

BASE_DIR = os.path.dirname(__file__)
MODULES_DIR = os.path.join(BASE_DIR, "modules")
COMMANDS_DIR = os.path.join(BASE_DIR, "commands")

for directory in [MODULES_DIR, COMMANDS_DIR]:
    if directory not in sys.path:
        sys.path.append(directory)

from modules import colorsModule, headerModule
from commands import commands_handler

def main():
    """Boucle principale du terminal"""
    headerModule.display_header()

    try:
        while True:
            command = input(f"{colorsModule.COLOR.NEON_RED} [{colorsModule.COLOR.WHITE}>{colorsModule.COLOR.NEON_RED}] {colorsModule.COLOR.RESET}").strip().lower()
            if command:
                commands_handler.handle_command(command)

    except KeyboardInterrupt:
        print(f"\n{colorsModule.COLOR.RED}Exiting MCPFuckTool...{colorsModule.COLOR.RESET}")
        time.sleep(1)
        sys.exit(0)  # Sort proprement

if __name__ == "__main__":
    main()
