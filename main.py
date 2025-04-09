import os
import sys
import time
from pathlib import Path
from modules.colorsModule import COLOR
from modules.headerModule import display_header
from modules.historyManager import setup_history
from modules.readlineSetup import setup_completer
from commands.commands_handler import get_all_commands, handle_command

def main():
    """Boucle principale du terminal"""
    BASE_DIR = Path(__file__).parent
    COMMANDS = get_all_commands()
    
    setup_completer(COMMANDS)
    setup_history(BASE_DIR / ".fucktool_history")
    display_header()

    try:
        while True:
            try:
                # Prompt plus consistant
                command = input(f"{COLOR.NEON_RED} [{COLOR.WHITE}>{COLOR.NEON_RED}] {COLOR.RESET}").strip().lower()
                if command:
                    handle_command(command)
            except Exception as e:
                print(f"\n{COLOR.RED}Error: {e}{COLOR.RESET}")
                continue

    except KeyboardInterrupt:
        print(f"\n\n  {COLOR.NEON_RED}[{COLOR.WHITE}!{COLOR.NEON_RED}] {COLOR.WHITE}Exiting {COLOR.NEON_RED}Fuck{COLOR.WHITE}Tool...{COLOR.RESET}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)

if __name__ == "__main__":
    main()