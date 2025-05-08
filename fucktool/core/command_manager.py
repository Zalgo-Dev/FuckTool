# fucktool/core/command_manager.py

import sys
import time
from core.colors import NEON_RED, WHITE, RESET, RED, GRAY, NEON_ORANGE

COMMAND_REGISTRY = {}

class BaseCommand:
    name = ""
    description = ""
    usage = ""
    exemple = ""

    def run(self, args):
        raise NotImplementedError("run() must be implemented by subclasses")

def register_command(cls):
    """Décorateur pour enregistrer automatiquement une commande"""
    if not issubclass(cls, BaseCommand):
        raise ValueError("Command must inherit from BaseCommand")
    COMMAND_REGISTRY[cls.name] = cls()
    return cls

def handle_command(command_line):
    parts = command_line.strip().split()
    if not parts:
        return

    cmd = parts[0]
    args = parts[1:]

    if cmd == "exit":
        print(f"\n {NEON_RED}[{WHITE}!{NEON_RED}] {WHITE}Exiting {NEON_RED}Fuck{WHITE}Tool...{RESET}")
        time.sleep(1)
        sys.exit(0)
    elif cmd in COMMAND_REGISTRY:
        try:
            COMMAND_REGISTRY[cmd].run(args)
        except Exception as e:
            print(f"\n {GRAY}[{NEON_ORANGE}ERROR{GRAY}]{RESET} {e}{RESET}\n")
    else:
        print(f"\n {WHITE}[{RED}ERROR{WHITE}]{RESET} Unknown command: '{cmd}'{RESET}\n")

def get_all_commands():
    return list(COMMAND_REGISTRY.keys())

def get_command_metadata():
    return [
        {
            "name": cmd.name,
            "description": cmd.description,
            "usage": cmd.usage,
            "exemple": cmd.exemple
        }
        for cmd in COMMAND_REGISTRY.values()
    ]
