import os
import shutil
from modules.colorsModule import COLOR

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    return shutil.get_terminal_size().columns

def pad_right(text, length):
    return text + " " * max(0, length - len(text))

def display_header():
    clear_screen()

    cols = get_terminal_width()
    username = os.getlogin()
    user_length = len(username)
    min_box_width = 25
    box_width = max(user_length + 20, min_box_width)

    # Ajustement de l'offset pour l'alignement dynamique
    offset = max(0, cols - box_width - 45)  # 45 = Largeur moyenne du logo

    # Si l'écran est trop petit, on met l'info box en dessous du logo
    right_align = offset > 10  # Vérification si on peut l'afficher à droite

    border = "═" * (box_width - 2)
    user_padding = " " * max(0, box_width - user_length - 15)
    plan_padding = " " * max(0, box_width - 19)

    # Construction du header complet avec le logo
    header_lines = [
        f"{COLOR.NEON_RED}                                          {' ' * offset}╒{border}╕",
        f"{COLOR.NEON_RED}     ╔╦╗╔═╗╔═╗{COLOR.WHITE}╔═╗╷ ╷╭─┐┬ ╷╔╦╗{COLOR.NEON_RED}┌─┐┌─┐┬      {' ' * offset}│{COLOR.WHITE} Account Information {pad_right('', box_width - 23)}{COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}     ║║║║  ╠═╝{COLOR.WHITE}╠╡ │ ││  ├─╯ ║ {COLOR.NEON_RED}│ ││ ││      {' ' * offset}│{COLOR.WHITE} Username: {username} {pad_right('', box_width - user_length - 14)}{COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}     ╩ ╩╚═╝╩  {COLOR.WHITE}╩  ╰─╯╰─┘┴ ╵ ╩ {COLOR.NEON_RED}└─┘└─┘┴─┘    {' ' * offset}│{COLOR.WHITE} Plan: {COLOR.NEON_YELLOW}TOTALLY FREE 🖕 {pad_right('', box_width - 25)}{COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}    ═══╦═══════════════════════════╦═══   {' ' * offset}╘{border}╛",
        f"{COLOR.NEON_RED}  ╒════╩═══════════════════════════╩════╕",
        f"{COLOR.NEON_RED}  │{COLOR.WHITE} Advanced Minecraft Pentesting Tool  {COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}  │{COLOR.WHITE}            By ZalgoDev              {COLOR.NEON_RED}│",
        f"{COLOR.NEON_RED}  ╘═════════════════════════════════════╛"
    ]

    # Affichage de l'interface principale
    for line in header_lines:
        print(line)

    # Message de bienvenue
    print(f"     {COLOR.WHITE}Hello {COLOR.UNDERLINE}@{username}{COLOR.RESET}. {COLOR.WHITE}Welcome to {COLOR.LIGHT_RED}MCPFuckTool{COLOR.RESET}")
    print(f"   {COLOR.WHITE}To view available commands, type {COLOR.LIGHT_RED}help{COLOR.RESET}")
    print(f"")