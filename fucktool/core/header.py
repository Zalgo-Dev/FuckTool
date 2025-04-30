import os
import shutil
import getpass
from core.colors import COLOR

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80  # Fallback width

def pad_right(text, length):
    return text + " " * max(0, length - len(text))

def display_header():
    clear_screen()
    
    try:
        username = getpass.getuser()
    except:
        username = "User"
    
    cols = get_terminal_width()
    user_length = len(username)
    min_box_width = 25
    box_width = max(user_length + 20, min_box_width)
    offset = max(0, cols - box_width - 45)
    
    # Pré-calcul des valeurs répétitives
    border = "═" * (box_width - 2)
    user_pad = box_width - user_length - 14
    plan_pad = box_width - 25
    
    header_lines = [
        f"{COLOR.NEON_RED}                                          {' ' * offset}╒{border}╕",
        f"{COLOR.NEON_RED}          ╔═╗╷ ╷╭─┐┬ ╷{COLOR.WHITE}╔╦╗┌─┐┌─┐┬          {COLOR.NEON_RED}{' ' * offset}│{COLOR.WHITE} Account Information {pad_right('', box_width - 23)}{COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}          ╠╡ │ ││  ├─╯{COLOR.WHITE} ║ │ ││ ││          {COLOR.NEON_RED}{' ' * offset}│{COLOR.WHITE} Username: {username} {pad_right('', user_pad)}{COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}          ╩  ╰─╯╰─┘┴ ╵{COLOR.WHITE} ╩ └─┘└─┘┴─┘        {COLOR.NEON_RED}{' ' * offset}│{COLOR.WHITE} Plan: {COLOR.NEON_YELLOW}TOTALLY FREE 🖕 {pad_right('', plan_pad)}{COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}    ═══╦═══════════════════════════╦═══   {' ' * offset}╘{border}╛",
        f"{COLOR.NEON_RED}  ╒════╩═══════════════════════════╩════╕",
        f"{COLOR.NEON_RED}  │{COLOR.WHITE} Advanced Minecraft Pentesting Tool  {COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}  │{COLOR.WHITE}            By ZalgoDev              {COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}  ╘═════════════════════════════════════╛"
    ]

    print("\n".join(header_lines))
    print(f"\n     {COLOR.WHITE}Hello {COLOR.UNDERLINE}@{username}{COLOR.RESET}. {COLOR.WHITE}Welcome to {COLOR.LIGHT_RED}FuckTool{COLOR.RESET}")
    print(f"   {COLOR.WHITE}To view available commands, type {COLOR.LIGHT_RED}help{COLOR.RESET}\n")