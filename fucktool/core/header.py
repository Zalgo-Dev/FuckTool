import os
import shutil
import getpass
from core.colors import WHITE, NEON_RED, UNDERLINE, RESET, LIGHT_RED, NEON_YELLOW

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
        f"{NEON_RED}                                          {' ' * offset}╒{border}╕",
        f"{NEON_RED}          ╔═╗╷ ╷╭─┐┬ ╷{WHITE}╔╦╗┌─┐┌─┐┬          {NEON_RED}{' ' * offset}│{WHITE} Account Information {pad_right('', box_width - 23)}{NEON_RED}│",
        f"{NEON_RED}          ╠╡ │ ││  ├─╯{WHITE} ║ │ ││ ││          {NEON_RED}{' ' * offset}│{WHITE} Username: {username} {pad_right('', user_pad)}{NEON_RED}│",
        f"{NEON_RED}          ╩  ╰─╯╰─┘┴ ╵{WHITE} ╩ └─┘└─┘┴─┘        {NEON_RED}{' ' * offset}│{WHITE} Plan: {NEON_YELLOW}TOTALLY FREE 🖕 {pad_right('', plan_pad)}{NEON_RED}│",
        f"{NEON_RED}    ═══╦═══════════════════════════╦═══   {' ' * offset}╘{border}╛",
        f"{NEON_RED}  ╒════╩═══════════════════════════╩════╕",
        f"{NEON_RED}  │{WHITE} Advanced Minecraft Pentesting Tool  {NEON_RED}│",
        f"{NEON_RED}  │{WHITE}            By ZalgoDev              {NEON_RED}│",
        f"{NEON_RED}  ╘═════════════════════════════════════╛"
    ]

    print("\n".join(header_lines))
    print(f"\n     {WHITE}Hello {UNDERLINE}@{username}{RESET}. {WHITE}Welcome to {LIGHT_RED}FuckTool{RESET}")
    print(f"   {WHITE}To view available commands, type {LIGHT_RED}help{RESET}\n")