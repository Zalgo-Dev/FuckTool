import os
import sys
import time
from core.colors import COLOR
from core.header import display_header
from commands.info import handle_info
from commands.details import handle_details
from commands.fakeproxy import main_fakeproxy
from commands.dns import handle_dns
from commands.help import handle_help
from commands.stress import handle_stress

def get_all_commands():
    """Retourne toutes les commandes disponibles pour la complétion"""
    return ["help", "info", "details", "dns", "fakeproxy", "stress", "clear", "exit"]

def handle_command(command):
    parts = command.split()
    if not parts:
        return
    
    cmd = parts[0]
    args = parts[1:]

    if cmd == "help":
        handle_help()
    elif cmd == "info":
        handle_info(args)
    elif cmd == "details":
        handle_details(args)
    elif cmd == "dns":
        handle_dns(args)
    elif cmd == "stress":
        handle_stress(args)
    elif cmd == "fakeproxy":
        main_fakeproxy(parts)
    elif cmd == "clear":
        display_header()
    elif cmd == "exit":
        print(f"\n {COLOR.NEON_RED}[{COLOR.WHITE}!{COLOR.NEON_RED}] {COLOR.WHITE}Exiting {COLOR.NEON_RED}Fuck{COLOR.WHITE}Tool...{COLOR.RESET}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)
    else:
        print(f"")
        print(f"  {COLOR.YELLOW}[Error] Unknown command: \"{cmd}\"{COLOR.RESET}")
        print(f"")
