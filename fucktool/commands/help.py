from core.command_manager import BaseCommand, register_command, get_command_metadata
from core.colors import NEON_RED, RESET, LIGHT_RED, BOLD, YELLOW, GREEN, WHITE

@register_command
class HelpCommand(BaseCommand):
    name = "help"
    description = "Display all available commands."
    usage = "help"

    def run(self, args=None):
        print(f"\n {NEON_RED}┌{'─' * 90}┐")
        print(f" {NEON_RED}│{RESET}  {LIGHT_RED}FuckTool - Command Help{RESET} {' ' * 63} {NEON_RED}│")
        print(f" {NEON_RED}├{'─' * 90}┤")

        for cmd in get_command_metadata():
            spacing = 30 - len(cmd["name"])
            print(f" {NEON_RED}│{RESET}  - {GREEN}{cmd['name']}{RESET}{' ' * spacing}➜ {cmd['description']}{' ' * (40 - len(cmd['description']))} {NEON_RED}│")

        print(f" {NEON_RED}└{'─' * 90}┘\n")
