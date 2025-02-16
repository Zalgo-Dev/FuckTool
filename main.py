import os
import sys
import time
import readline

from modules.colorsModule import COLOR
from modules.headerModule import display_header
from commands.commands_handler import get_all_commands, handle_command

BASE_DIR = os.path.dirname(__file__)
MODULES_DIR = os.path.join(BASE_DIR, "modules")
COMMANDS_DIR = os.path.join(BASE_DIR, "commands")

for directory in [MODULES_DIR, COMMANDS_DIR]:
    if directory not in sys.path:
        sys.path.append(directory)

COMMANDS = get_all_commands()

def completer(text, state):
    options = [cmd for cmd in COMMANDS if cmd.startswith(text)]
    return options[state] if state < len(options) else None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

HISTORY_FILE = os.path.join(BASE_DIR, ".mcpfucktool_history")

try:
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    open(HISTORY_FILE, 'wb').close()

import atexit
atexit.register(readline.write_history_file, HISTORY_FILE)


def main():
    """Boucle principale du terminal"""
    display_header()

    try:
        while True:
            sys.stdout.write(f"{COLOR.NEON_RED} [{COLOR.WHITE}>{COLOR.NEON_RED}] {COLOR.RESET}")
            sys.stdout.flush()
            command = input().strip().lower()
            if command:
                handle_command(command)

    except KeyboardInterrupt:
        print(f"  {COLOR.RED}\n\n  {COLOR.NEON_RED}[{COLOR.WHITE}!{COLOR.NEON_RED}] {COLOR.WHITE}Exiting {COLOR.NEON_RED}Fuck{COLOR.WHITE}Tool...{COLOR.RESET}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)

if __name__ == "__main__":
    main()
