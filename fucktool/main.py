import os
import sys
import time
from pathlib import Path

from core.colors import COLOR
from core.header import display_header
from commands.handler import get_all_commands, handle_command

# Nouvelle importation du système d'input amélioré
try:
    from core.input_manager import get_command_input
    USE_PROMPT_TOOLKIT = True
except ImportError:
    USE_PROMPT_TOOLKIT = False

def main():
    """Boucle principale du terminal"""
    BASE_DIR = Path(__file__).parent
    COMMANDS = get_all_commands()

    display_header()

    try:
        while True:
            try:
                if USE_PROMPT_TOOLKIT:
                    command = get_command_input(COMMANDS).strip().lower()
                else:
                    command = input(f"{COLOR.NEON_RED} [{COLOR.WHITE}>{COLOR.NEON_RED}] {COLOR.RESET}").strip().lower()

                if command:
                    handle_command(command)

            except Exception as e:
                print(f"\n{COLOR.RED}Error: {e}{COLOR.RESET}")
                continue

    except KeyboardInterrupt:
        print(f"\n {COLOR.NEON_RED}[{COLOR.WHITE}!{COLOR.NEON_RED}] {COLOR.WHITE}Exiting {COLOR.NEON_RED}Fuck{COLOR.WHITE}Tool...{COLOR.RESET}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)

if __name__ == "__main__":
    main()
