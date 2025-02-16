#   ███╗   ███╗     ██████╗    ██████╗     ███████╗    ██╗   ██╗     ██████╗    ██╗  ██╗    ████████╗     ██████╗      ██████╗     ██╗     
#   ████╗ ████║    ██╔════╝    ██╔══██╗    ██╔════╝    ██║   ██║    ██╔════╝    ██║ ██╔╝    ╚══██╔══╝    ██╔═══██╗    ██╔═══██╗    ██║     
#   ██╔████╔██║    ██║         ██████╔╝    █████╗      ██║   ██║    ██║         █████╔╝        ██║       ██║   ██║    ██║   ██║    ██║     
#   ██║╚██╔╝██║    ██║         ██╔═══╝     ██╔══╝      ██║   ██║    ██║         ██╔═██╗        ██║       ██║   ██║    ██║   ██║    ██║     
#   ██║ ╚═╝ ██║    ╚██████╗    ██║         ██║         ╚██████╔╝    ╚██████╗    ██║  ██╗       ██║       ╚██████╔╝    ╚██████╔╝    ███████╗
#   ╚═╝     ╚═╝     ╚═════╝    ╚═╝         ╚═╝          ╚═════╝      ╚═════╝    ╚═╝  ╚═╝       ╚═╝        ╚═════╝      ╚═════╝     ╚══════╝

# Name      =   MCPFuckTool
# Author    =   ZalgoDev
# Date      =   05.02.2025 (day.month.year)
# Version   =   0.1

# This tool is free to use.
# dsc.gg/rcelibs
# Have a good hacking session :P

import os
import shutil
import time
import sys
import requests
from datetime import datetime, timezone
import urllib.parse
import json

#   ██╗   ██╗     █████╗     ██████╗     ███████╗
#   ██║   ██║    ██╔══██╗    ██╔══██╗    ██╔════╝
#   ██║   ██║    ███████║    ██████╔╝    ███████╗
#   ╚██╗ ██╔╝    ██╔══██║    ██╔══██╗    ╚════██║
#    ╚████╔╝     ██║  ██║    ██║  ██║    ███████║
#     ╚═══╝      ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚══════╝

# 🌈 Palette de couleurs
class COLOR:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"

    # ⚪ Blanc & Gris (Clair → Foncé)
    BRIGHT_WHITE = "\033[97m"
    WHITE = "\033[37m"
    LIGHT_GRAY = "\033[37m"
    SILVER = "\033[38;5;247m"
    GRAY = "\033[90m"
    DARK_GRAY = "\033[38;5;235m"
    BRIGHT_BLACK = "\033[90m"
    BLACK = "\033[30m"

    # 🔴 Rouge (Clair → Foncé)
    LIGHT_RED = "\033[38;5;203m"
    BRIGHT_RED = "\033[91m"
    NEON_RED = "\033[38;5;196m"
    RED = "\033[31m"
    DARK_RED = "\033[38;5;124m"

    # 🟢 Vert (Clair → Foncé)
    LIGHT_GREEN = "\033[92m"
    BRIGHT_GREEN = "\033[92m"
    NEON_GREEN = "\033[38;5;46m"
    MINT_GREEN = "\033[38;5;48m"
    GREEN = "\033[32m"
    DARK_GREEN = "\033[38;5;28m"

    # 🟡 Jaune (Clair → Foncé)
    LIGHT_YELLOW = "\033[38;5;228m"
    BRIGHT_YELLOW = "\033[93m"
    NEON_YELLOW = "\033[38;5;226m"
    YELLOW = "\033[33m"
    GOLD = "\033[38;5;214m"
    DARK_YELLOW = "\033[38;5;136m"

    # 🟠 Orange (Clair → Foncé)
    LIGHT_ORANGE = "\033[38;5;215m"
    BRIGHT_ORANGE = "\033[38;5;214m"
    NEON_ORANGE = "\033[38;5;202m"
    ORANGE = "\033[38;5;208m"
    SUNSET_ORANGE = "\033[38;5;166m"
    DARK_ORANGE = "\033[38;5;130m"

    # 🔵 Bleu (Clair → Foncé)
    SKY_BLUE = "\033[38;5;117m"
    LIGHT_BLUE = "\033[94m"
    BRIGHT_BLUE = "\033[94m"
    NEON_BLUE = "\033[38;5;51m"
    TURQUOISE = "\033[38;5;45m"
    BLUE = "\033[34m"
    DARK_BLUE = "\033[38;5;19m"

    # 🟣 Violet / Magenta (Clair → Foncé)
    PINK = "\033[38;5;205m"
    MAGENTA = "\033[38;5;200m"
    LIGHT_PURPLE = "\033[95m"
    BRIGHT_PURPLE = "\033[95m"
    NEON_PURPLE = "\033[38;5;201m"
    PURPLE = "\033[35m"
    DARK_PURPLE = "\033[38;5;54m"

    # 🟦 Cyan (Clair → Foncé)
    AQUA = "\033[38;5;14m"
    LIGHT_CYAN = "\033[38;5;51m"
    BRIGHT_CYAN = "\033[96m"
    NEON_CYAN = "\033[38;5;50m"
    CYAN = "\033[36m"
    DARK_CYAN = "\033[38;5;30m"

#   ███████╗    ██╗   ██╗    ███╗   ██╗     ██████╗    ████████╗    ██╗     ██████╗     ███╗   ██╗    ███████╗
#   ██╔════╝    ██║   ██║    ████╗  ██║    ██╔════╝    ╚══██╔══╝    ██║    ██╔═══██╗    ████╗  ██║    ██╔════╝
#   █████╗      ██║   ██║    ██╔██╗ ██║    ██║            ██║       ██║    ██║   ██║    ██╔██╗ ██║    ███████╗
#   ██╔══╝      ██║   ██║    ██║╚██╗██║    ██║            ██║       ██║    ██║   ██║    ██║╚██╗██║    ╚════██║
#   ██║         ╚██████╔╝    ██║ ╚████║    ╚██████╗       ██║       ██║    ╚██████╔╝    ██║ ╚████║    ███████║
#   ╚═╝          ╚═════╝     ╚═╝  ╚═══╝     ╚═════╝       ╚═╝       ╚═╝     ╚═════╝     ╚═╝  ╚═══╝    ╚══════╝

# Fonction pour effacer l'écran
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour obtenir la largeur du terminal
def get_terminal_width():
    return shutil.get_terminal_size().columns

# Fonction pour générer un padding dynamique
def pad_right(text, length):
    return text + " " * max(0, length - len(text))

def format_timestamp(timestamp):
    """Convertit un timestamp UNIX en une date lisible avec timezone UTC"""
    try:
        return datetime.fromtimestamp(int(timestamp), timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
    except (ValueError, TypeError):
        return "Unknown"

def extract_text(description):
    """Extrait le texte brut d'un JSON de description"""
    if isinstance(description, str):
        return description.strip()  # Si c'est déjà une chaîne, on la retourne directement

    if isinstance(description, dict):
        text_parts = []

        # Récupère le texte principal
        if "text" in description and isinstance(description["text"], str):
            text_parts.append(description["text"].strip())

        # Vérifie si "extra" contient d'autres éléments de texte
        if "extra" in description and isinstance(description["extra"], list):
            for item in description["extra"]:
                text_parts.append(extract_text(item))  # Récursivité pour extraire tout le texte

        return " ".join(filter(None, text_parts)).strip()  # Assemble tout proprement

    return "No Description"  # Valeur par défaut si le format est inconnu

def format_plugins(plugins):
    """Formate et trie la liste des plugins pour un affichage propre et trié alphabétiquement."""
    if isinstance(plugins, list) and len(plugins) > 0:
        sorted_plugins = sorted(plugins, key=lambda p: p.get('name', '').lower())  # Tri alphabétique
        return "\n  ".join([f"  ↪ {plugin['name']} ({plugin['version']})" for plugin in sorted_plugins if 'name' in plugin and 'version' in plugin])
    return "None"

#   ██╗  ██╗    ███████╗     █████╗     ██████╗     ███████╗    ██████╗ 
#   ██║  ██║    ██╔════╝    ██╔══██╗    ██╔══██╗    ██╔════╝    ██╔══██╗
#   ███████║    █████╗      ███████║    ██║  ██║    █████╗      ██████╔╝
#   ██╔══██║    ██╔══╝      ██╔══██║    ██║  ██║    ██╔══╝      ██╔══██╗
#   ██║  ██║    ███████╗    ██║  ██║    ██████╔╝    ███████╗    ██║  ██║
#   ╚═╝  ╚═╝    ╚══════╝    ╚═╝  ╚═╝    ╚═════╝     ╚══════╝    ╚═╝  ╚═╝

# Fonction pour afficher l'en-tête avec alignement dynamique et responsive
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

#   ██╗  ██╗    ███████╗    ██╗         ██████╗ 
#   ██║  ██║    ██╔════╝    ██║         ██╔══██╗
#   ███████║    █████╗      ██║         ██████╔╝
#   ██╔══██║    ██╔══╝      ██║         ██╔═══╝ 
#   ██║  ██║    ███████╗    ███████╗    ██║     
#   ╚═╝  ╚═╝    ╚══════╝    ╚══════╝    ╚═╝     

# Fonction pour afficher l'aide
def show_help():
    print(f"")
    print(f" {COLOR.NEON_RED}┌{'─' * 90}┐")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.LIGHT_RED}MCPFuckTool - Command Help{COLOR.RESET} {' ' * 60} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}├{'─' * 90}┤")

    # Section: Server Information
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Server Information:{COLOR.RESET} {' ' * 67} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}info <ip:port>{COLOR.RESET}             ➜ Get server details (Title, Players, Version, etc.) {' ' * 5} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}details <ip>{COLOR.RESET}               ➜ Get advanced server information {' ' * 24} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {' ' * 30} (Geo, Secure Chat, Forge, etc.) {' ' * 24} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    # Section: Scanning Tools
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Scanning Tools:{COLOR.RESET} {' ' * 71} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}scan <ip> <port> <type>{COLOR.RESET}    ➜ Scan a Minecraft server with a specific scanner {' ' * 8} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}      Available types: {COLOR.CYAN}qubo, old_qubo, nmap, masscan, rustscan{COLOR.RESET} {' ' * 26} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    # Section: Exploits
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Exploits:{COLOR.RESET} {' ' * 77} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}exploit{COLOR.RESET}                    ➜ Run an exploit {' ' * 41} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}list{COLOR.RESET}                       ➜ List available exploits {' ' * 32} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    # Section: Utilities
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Utilities:{COLOR.RESET} {' ' * 76} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}clear{COLOR.RESET}                      ➜ Clear the screen {' ' * 39} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}exit{COLOR.RESET}                       ➜ Quit MCPFuckTool {' ' * 39} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}└{'─' * 90}┘\n")

#   ██╗    ███╗   ██╗    ███████╗     ██████╗ 
#   ██║    ████╗  ██║    ██╔════╝    ██╔═══██╗
#   ██║    ██╔██╗ ██║    █████╗      ██║   ██║
#   ██║    ██║╚██╗██║    ██╔══╝      ██║   ██║
#   ██║    ██║ ╚████║    ██║         ╚██████╔╝
#   ╚═╝    ╚═╝  ╚═══╝    ╚═╝          ╚═════╝ 

# Fonction pour récupérer les infos d'un serveur


def handle_info(args):
    if len(args) != 1:
        print(f"\n  {COLOR.RED}[{COLOR.LIGHT_ORANGE}Error{COLOR.RED}] {COLOR.YELLOW}Usage: info <ip:port>{COLOR.RESET}\n")
        return
    
    server = args[0].strip()
    url = f"https://api.mcstatus.io/v2/status/java/{server}"
    
    try:
        print(f"\n  {COLOR.GRAY}[{COLOR.RED}#{COLOR.GRAY}]{COLOR.WHITE} Fetching server data from {COLOR.NEON_GREEN}{server}{COLOR.RESET}...\n")
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            print(f"  {COLOR.RED}[❌ Error] Failed to fetch server info (Status Code: {response.status_code}){COLOR.RESET}\n")
            return
        
        data = response.json()
        
        if "online" not in data:
            print(f"  {COLOR.RED}[❌ Error] Missing 'online' key in response.{COLOR.RESET}\n")
            return

        if not data["online"]:  # Accès direct sans `get()`
            print(f"  {COLOR.RED}[❌ Error] The server {server} is offline.{COLOR.RESET}\n")
            return
        
        # Récupération des informations essentielles
        host = data.get("host", server)
        port = data.get("port", "Unknown")
        ip_address = data.get("ip_address", "Unknown")
        motd = data.get("motd", {}).get("clean", "Unknown")
        version = data.get("version", {}).get("name_clean", "Unknown")
        protocol = data.get("version", {}).get("protocol", "Unknown")
        players_online = data.get("players", {}).get("online", 0)
        max_players = data.get("players", {}).get("max", 0)
        software = data.get("software", "Unknown")
        mods = data.get("mods", [])
        plugins = data.get("plugins", [])

        players_list = data.get("players", {}).get("list", [])

        # 🖥️ Affichage des informations principales
        print(f"  {"=" * 60}")
        print(f"  🌍 {COLOR.BOLD}{COLOR.NEON_GREEN}Server Info : {server}{COLOR.RESET}")
        print(f"  {"=" * 60}")
        print(f"  📡 {COLOR.BOLD}Host:{COLOR.RESET} {COLOR.YELLOW}{host}{COLOR.RESET}")
        print(f"  🌐 {COLOR.BOLD}IP:{COLOR.RESET} {COLOR.LIGHT_BLUE}{ip_address}:{port}{COLOR.RESET}")
        print(f"  📝 {COLOR.BOLD}MOTD:{COLOR.RESET} {COLOR.CYAN}{motd}{COLOR.RESET}")
        print(f"  🎮 {COLOR.BOLD}Version:{COLOR.RESET} {COLOR.LIGHT_GREEN}{version}{COLOR.RESET} (Protocol: {COLOR.PURPLE}{protocol}{COLOR.RESET})")
        print(f"  👥 {COLOR.BOLD}Players:{COLOR.RESET} {COLOR.GREEN}{players_online}{COLOR.RESET}/{COLOR.RED}{max_players}{COLOR.RESET}")
        print(f"  🏗️ {COLOR.BOLD}Software:{COLOR.RESET} {COLOR.ORANGE}{software}{COLOR.RESET}")
        print(f"  {"=" * 60}")

        # 🔧 Affichage des mods installés
        if mods:
            print(f"\n  🔧 {COLOR.BOLD}Mods Installed ({len(mods)}):{COLOR.RESET}")
            print(f"  {'-' * 50}")
            for mod in mods:
                mod_name = mod.get("name", "Unknown")
                mod_version = mod.get("version", "Unknown")
                print(f"    📦 {COLOR.LIGHT_BLUE}{mod_name} {COLOR.GRAY}- {COLOR.YELLOW}v{mod_version}{COLOR.RESET}")
            print(f"  {'-' * 50}")
        else:
            print(f"  ❌ {COLOR.BOLD}No mods detected.{COLOR.RESET}")

        # 🛠️ Affichage des plugins installés
        if plugins:
            print(f"\n  🛠️ {COLOR.BOLD}Plugins Installed ({len(plugins)}):{COLOR.RESET}")
            print(f"  {'-' * 50}")
            for plugin in plugins:
                plugin_name = plugin.get("name", "Unknown")
                plugin_version = plugin.get("version", "Unknown")
                print(f"    📦 {COLOR.LIGHT_BLUE}{plugin_name} {COLOR.GRAY}- {COLOR.YELLOW}v{plugin_version}{COLOR.RESET}")
            print(f"  {'-' * 50}")
        else:
            print(f"  ❌ {COLOR.BOLD}No plugins detected.{COLOR.RESET}")

        # 🎭 Affichage des joueurs connectés
        if players_list:
            print(f"\n  🎭 {COLOR.BOLD}Connected Players ({len(players_list)}):{COLOR.RESET}")
            print(f"  {'-' * 50}")
            for player in players_list:
                player_name = player.get("name_clean", "Unknown")
                player_uuid = player.get("uuid", "Unknown")
                print(f"    👤 {COLOR.LIGHT_GREEN}{player_name}{COLOR.RESET} ({COLOR.GRAY}{player_uuid}{COLOR.RESET})")
            print(f"  {'-' * 50}")
        else:
            print(f"  ❌ {COLOR.BOLD}No players currently online.{COLOR.RESET}\n")

    except requests.exceptions.RequestException as e:
        print(f"  {COLOR.RED}[❌ Error] Failed to connect to API: {e}{COLOR.RESET}\n")


#   ███████╗     ██████╗     █████╗     ███╗   ██╗
#   ██╔════╝    ██╔════╝    ██╔══██╗    ████╗  ██║
#   ███████╗    ██║         ███████║    ██╔██╗ ██║
#   ╚════██║    ██║         ██╔══██║    ██║╚██╗██║
#   ███████║    ╚██████╗    ██║  ██║    ██║ ╚████║
#   ╚══════╝     ╚═════╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝

# Fonction pour exécuter un scan avec arguments
def handle_scan(args):
    if len(args) != 3:
        print(f"\n  {COLOR.RED}[{COLOR.LIGHT_ORANGE}Error{COLOR.RED}] {COLOR.YELLOW}Usage: scan <ip> <port> <type>{COLOR.RESET}\n")
        return

    ip, port, scan_type = args

    valid_scanners = ["qubo", "old_qubo", "nmap", "masscan", "rustscan"]

    if scan_type not in valid_scanners:
        print(f"  {COLOR.YELLOW}[Error] Invalid scan type. Choose from: {', '.join(valid_scanners)}{COLOR.RESET}")
        print(f"")
        return

    print(f"  {COLOR.WHITE}\n🔍 Scanning {ip}:{port} using {scan_type}...{COLOR.RESET}")
    print(f"")
    time.sleep(2)
    print(f"  {COLOR.YELLOW}✔ Scan complete using {scan_type}.{COLOR.RESET}")
    print(f"")

#   ██████╗     ███████╗    ████████╗     █████╗     ██╗    ██╗         ███████╗
#   ██╔══██╗    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██║    ██║         ██╔════╝
#   ██║  ██║    █████╗         ██║       ███████║    ██║    ██║         ███████╗
#   ██║  ██║    ██╔══╝         ██║       ██╔══██║    ██║    ██║         ╚════██║
#   ██████╔╝    ███████╗       ██║       ██║  ██║    ██║    ███████╗    ███████║
#   ╚═════╝     ╚══════╝       ╚═╝       ╚═╝  ╚═╝    ╚═╝    ╚══════╝    ╚══════╝

def handle_details(args):
    if len(args) < 1:
        print(f"\n  {COLOR.RED}[{COLOR.LIGHT_ORANGE}Error{COLOR.RED}] {COLOR.YELLOW}Usage: details <ip> [--full]{COLOR.RESET}\n")
        return
    
    server_ip = args[0].strip()
    full_mode = "--full" in args  # Vérifie si l'option --full est activée

    # Encodage du filtre JSON pour l'API
    query = json.dumps({"ip": server_ip})
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.cornbread2100.com/servers?limit=1&query={encoded_query}"

    try:
        print(f"\n  {COLOR.GRAY}[{COLOR.RED}#{COLOR.GRAY}]{COLOR.WHITE} Fetching server details for {COLOR.NEON_GREEN}{server_ip}{COLOR.RESET}...\n")
        response = requests.get(url, timeout=60)

        if response.status_code != 200:
            print(f"  {COLOR.RED}[Error]{COLOR.YELLOW} Failed to fetch server info (Status Code: {response.status_code}){COLOR.RESET}\n")
            return

        data = response.json()

        if not isinstance(data, list) or len(data) == 0:
            print(f"  {COLOR.RED}[Error]{COLOR.YELLOW} No data found for {server_ip}.{COLOR.RESET}\n")
            return

        server = data[0]  # Premier résultat trouvé

        # Récupération des informations principales
        ip = server.get("ip", "Unknown")
        port = server.get("port", "Unknown")
        version = server.get("version", {}).get("name", "Unknown")
        online_players = server.get("players", {}).get("online", 0)
        max_players = server.get("players", {}).get("max", 0)
        cracked = server.get("cracked", False)
        country = server.get("geo", {}).get("country", "Unknown")
        last_seen = format_timestamp(server.get("lastSeen"))

        # Affichage des informations essentielles
        print(f"  {"=" * 50}")
        print(f"  🎮 {COLOR.NEON_GREEN}Server: {ip}:{port}{COLOR.RESET}")
        print(f"  {"=" * 50}")
        print(f"  🌍 Country: {COLOR.YELLOW}{country}{COLOR.RESET}")
        print(f"  🎮 Version: {COLOR.CYAN}{version}{COLOR.RESET}")
        print(f"  👥 Players: {COLOR.GREEN}{online_players}{COLOR.RESET}/{COLOR.RED}{max_players}{COLOR.RESET}")
        print(f"  🔓 Cracked: {'✅ Yes' if cracked else '❌ No'}")
        print(f"  🕒 Last Seen: {COLOR.PURPLE}{last_seen}{COLOR.RESET}")
        print(f"  {"=" * 50}")

        # Si l'utilisateur veut les détails complets (--full)
        if full_mode:
            org = server.get("org", "Unknown")
            city = server.get("geo", {}).get("city", "Unknown")
            latitude = server.get("geo", {}).get("lat", "Unknown")
            longitude = server.get("geo", {}).get("lon", "Unknown")
            enforces_secure_chat = server.get("enforcesSecureChat", "Unknown")
            has_favicon = server.get("hasFavicon", False)
            has_forge_data = server.get("hasForgeData", False)
            players_list = server.get("players", {}).get("sample", [])
            plugins = server.get("plugins", [])  # Récupération des plugins installés

            print(f"  🏢 Organization: {COLOR.ORANGE}{org}{COLOR.RESET}")
            print(f"  📍 Location: {COLOR.YELLOW}{city}, {country} (Lat: {latitude}, Lon: {longitude}){COLOR.RESET}")
            print(f"  🔒 Secure Chat Enforced: {enforces_secure_chat}")
            print(f"  🖼️ Has Favicon: {'✅ Yes' if has_favicon else '❌ No'}")
            print(f"  🔧 Has Forge Data: {'✅ Yes' if has_forge_data else '❌ No'}")

            # Liste des plugins si disponibles
            if plugins:
                print(f"\n  🔌 Installed Plugins ({len(plugins)}):")
                print("-" * 50)
                for plugin in plugins:
                    plugin_name = plugin.get("name", "Unknown")
                    plugin_version = plugin.get("version", "Unknown")
                    print(f"    📦 {COLOR.LIGHT_BLUE}{plugin_name} {COLOR.GRAY}- {COLOR.YELLOW}v{plugin_version}{COLOR.RESET}")
                print("-" * 50)
            else:
                print(f"  ❌ No plugins detected.")

            # Liste des joueurs récents si dispo
            if players_list:
                print(f"\n  🎭 Recently Connected Players:")
                print("-" * 50)
                for player in players_list:
                    player_name = player.get("name", "Unknown")
                    player_uuid = player.get("id", "Unknown")
                    last_seen = format_timestamp(player.get("lastSeen"))
                    print(f"    👤 {COLOR.LIGHT_GREEN}{player_name}{COLOR.RESET} ({player_uuid}) - Last Seen: {last_seen}")
                print("-" * 50)
            else:
                print(f"  ❌ No recent player data available.")

        print("")

    except requests.exceptions.RequestException as e:
        print(f"  {COLOR.RED}[Error]{COLOR.YELLOW} Failed to connect to API: {e}{COLOR.RESET}\n")

#    ██████╗     ██████╗     ███╗   ███╗    ███╗   ███╗     █████╗     ███╗   ██╗    ██████╗     ███████╗
#   ██╔════╝    ██╔═══██╗    ████╗ ████║    ████╗ ████║    ██╔══██╗    ████╗  ██║    ██╔══██╗    ██╔════╝
#   ██║         ██║   ██║    ██╔████╔██║    ██╔████╔██║    ███████║    ██╔██╗ ██║    ██║  ██║    ███████╗
#   ██║         ██║   ██║    ██║╚██╔╝██║    ██║╚██╔╝██║    ██╔══██║    ██║╚██╗██║    ██║  ██║    ╚════██║
#   ╚██████╗    ╚██████╔╝    ██║ ╚═╝ ██║    ██║ ╚═╝ ██║    ██║  ██║    ██║ ╚████║    ██████╔╝    ███████║
#    ╚═════╝     ╚═════╝     ╚═╝     ╚═╝    ╚═╝     ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝    ╚═════╝     ╚══════╝

# Fonction pour exécuter des commandes
def handle_command(command):
    parts = command.split()
    if not parts:
        return
    
    cmd = parts[0]
    args = parts[1:]

    if cmd == "help":
        show_help()
    elif cmd == "info":
        handle_info(args)
    elif cmd == "scan":
        handle_scan(args)
    elif cmd == "details":
        handle_details(args)
    elif cmd == "exploit":
        print(f"\n  💀 {COLOR.GREEN}Soon{COLOR.RESET}")
        print(f"")
    elif cmd == "list":
        print(f"\n  💀 {COLOR.GREEN}Soon{COLOR.RESET}")
        print(f"")
    elif cmd == "clear":
        display_header()
    elif cmd == "exit":
        print(f"{COLOR.RED}\n  {COLOR.NEON_RED}[{COLOR.WHITE}!{COLOR.NEON_RED}] {COLOR.LIGHT_RED}Exiting MCPFuckTool...{COLOR.RESET}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)
    else:
        print(f"")
        print(f"  {COLOR.YELLOW}[Error] Unknown command: \"{cmd}\"{COLOR.RESET}")
        print(f"")

# Fonction principale (boucle du faux terminal)
def main():
    display_header()    
    
    try:
        while True:
            command = input(f"{COLOR.NEON_RED} [{COLOR.WHITE}>{COLOR.NEON_RED}] {COLOR.RESET}").strip().lower()
            handle_command(command)
    except KeyboardInterrupt:
        print(f"")
        print(f" {COLOR.RED}{COLOR.NEON_RED}[{COLOR.WHITE}!{COLOR.NEON_RED}] {COLOR.LIGHT_RED}Exiting MCPFuckTool...{COLOR.RESET}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)

# Exécution du programme
if __name__ == "__main__":
    main()
