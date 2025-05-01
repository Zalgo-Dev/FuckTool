import os
import sys
import time
from core.colors import NEON_RED, WHITE, RESET, YELLOW
from core.header import display_header
from commands.details import handle_details
from commands.fakeproxy import main_fakeproxy
from commands.dns import handle_dns
from commands.help import handle_help
from commands.info import handle_info
from commands.stress import handle_stress

def get_all_commands():
    """Retourne toutes les commandes disponibles pour la complétion"""

    return ["clear", "details", "dns", "exit", "fakeproxy", "help", "info", "stress"]

def handle_command(command):
    parts = command.split()
    if not parts:
        return
    
    cmd = parts[0]
    args = parts[1:]

    if cmd == "clear":
        display_header()
    elif cmd == "details":
        handle_details(args)
    elif cmd == "dns":
        handle_dns(args)
    elif cmd == "stress":
        handle_stress(args)
    elif cmd == "fakeproxy":
        main_fakeproxy(parts)
    elif cmd == "exit":
        print(f"\n {NEON_RED}[{WHITE}!{NEON_RED}] {WHITE}Exiting {NEON_RED}Fuck{WHITE}Tool...{RESET}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)
    elif cmd == "help":
        handle_help()
    elif cmd == "info":
        handle_info(args)
    else:
        print(f"")
        print(f"  {YELLOW}[Error] Unknown command: \"{cmd}\"{RESET}")
        print(f"")
