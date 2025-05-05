# fucktool/commands/clear.py

import os
from core.command_manager import BaseCommand, register_command
from core.header import display_header
from core.colors import NEON_RED, WHITE, RESET, GREEN

@register_command
class ClearCommand(BaseCommand):
    name = "clear"
    description = "Clear the screen and re-display the banner"
    usage = "clear"

    def run(self, args):
        os.system("cls" if os.name == "nt" else "clear")
        display_header()
        