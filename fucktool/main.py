import os
import sys
import time
import importlib
import pkgutil
from pathlib import Path
import commands
import atexit

from core.colors import NEON_RED, WHITE, RESET
from core.header import display_header
from core.debug import handle_exception, debug_print
from core.command_manager import get_all_commands, handle_command
from core.sdk import init_sdk, shutdown_sdk
from config import Config

def set_terminal_title(title):
    """Fonction robuste pour définir le titre du terminal"""
    try:
        if os.name == 'nt':  # Windows
            os.system(f'title {title}')
        else:  # Linux/macOS
            if 'TERM' in os.environ and 'xterm' in os.environ['TERM']:
                sys.stdout.write(f"\x1b]0;{title}\x07")
            else:  # Pour les terminaux modernes
                sys.stdout.write(f"\033]0;{title}\007")
            sys.stdout.flush()
    except Exception as e:
        debug_print(f"Failed to set terminal title: {e}")

def setup_process_title():
    """Configure le nom du processus"""
    try:
        import setproctitle
        setproctitle.setproctitle("FuckTool - Terminal")
    except ImportError:
        set_terminal_title("FuckTool - Terminal")

def load_commands():
    """Charge dynamiquement toutes les commandes"""
    for loader, name, is_pkg in pkgutil.iter_modules(commands.__path__):
        importlib.import_module(f"commands.{name}")

def initialize_sdk():
    """Initialise le SDK et gère les erreurs"""
    if not init_sdk(Config.PACKET_SDK_KEY):
        debug_print("[!] SDK initialization failed")
        return False
    return True

def cleanup():
    """Nettoyage avant sortie"""
    shutdown_sdk()
    time.sleep(0.5)  # Laisse le temps à la fermeture
    os.system('cls' if os.name == 'nt' else 'clear')

def main_loop(commands):
    """Boucle principale de l'application"""
    try:
        while True:
            try:
                command = get_input(commands)
                if command:
                    handle_command(command)
            except Exception as e:
                handle_exception(e)
    except KeyboardInterrupt:
        print(f"\n {NEON_RED}[{WHITE}!{NEON_RED}] {WHITE}Exiting {NEON_RED}Fuck{WHITE}Tool...{RESET}")
        sys.exit(0)

def get_input(commands):
    """Gère l'entrée utilisateur selon les capacités du système"""
    try:
        from core.input_manager import get_command_input
        return get_command_input(commands).strip().lower()
    except ImportError:
        return input(f"{NEON_RED} [{WHITE}>{NEON_RED}] {RESET}").strip().lower()

def main():
    setup_process_title()
    load_commands()
    atexit.register(cleanup)
    initialize_sdk()
    display_header()
    debug_print(f"Commandes disponibles: {', '.join(get_all_commands())}")
    main_loop(get_all_commands())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        handle_exception(e)
        sys.exit(1)