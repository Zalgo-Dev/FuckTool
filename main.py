import os
import sys
import time
from modules.colorsModule import COLOR
from modules.headerModule import display_header
from modules.historyManager import setup_history
from modules.readlineSetup import setup_completer
from commands.commands_handler import get_all_commands, handle_command

BASE_DIR = os.path.dirname(__file__)
COMMANDS = get_all_commands()

setup_completer(COMMANDS)
setup_history(os.path.join(BASE_DIR, ".fucktool_history"))

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
