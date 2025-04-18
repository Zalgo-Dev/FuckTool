import os
import sys
import time
from modules.colorsModule import COLOR
from modules.headerModule import display_header
from commands.infoCommand import handle_info
from commands.detailsCommand import handle_details
from commands.dnsCommand import handle_dns
from commands.helpCommand import handle_help
from commands.stressCommand import handle_stress

def get_all_commands():
    """Retourne toutes les commandes disponibles pour la complétion"""
    return ["help", "info", "details", "dns", "stress", "clear", "exit"]

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
    elif cmd == "clear":
        display_header()
    elif cmd == "exit":
        print(f"{COLOR.RED}\n  {COLOR.NEON_RED}[{COLOR.WHITE}!{COLOR.NEON_RED}] {COLOR.WHITE}Exiting {COLOR.NEON_RED}Fuck{COLOR.WHITE}Tool...{COLOR.RESET}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)
    else:
        print(f"")
        print(f"  {COLOR.YELLOW}[Error] Unknown command: \"{cmd}\"{COLOR.RESET}")
        print(f"")