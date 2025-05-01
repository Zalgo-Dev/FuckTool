import requests
from core.colors import RED, LIGHT_ORANGE, YELLOW, RESET, GRAY, WHITE, NEON_GREEN, BOLD, LIGHT_BLUE, CYAN, LIGHT_GREEN, ORANGE, GREEN, PURPLE

def handle_info(args):
    if len(args) != 1:
        print(f"\n  {RED}[{LIGHT_ORANGE}Error{RED}] {YELLOW}Usage: info <ip:port>{RESET}\n")
        return
    
    server = args[0].strip()
    url = f"https://api.mcstatus.io/v2/status/java/{server}"
    
    try:
        print(f"\n  {GRAY}[{RED}#{GRAY}]{WHITE} Fetching server data from {NEON_GREEN}{server}{RESET}...\n")
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            print(f"  {RED}[❌ Error] Failed to fetch server info (Status Code: {response.status_code}){RESET}\n")
            return
        
        data = response.json()
        
        if "online" not in data:
            print(f"  {RED}[❌ Error] Missing 'online' key in response.{RESET}\n")
            return

        if not data["online"]:  # Accès direct sans `get()`
            print(f"  {RED}[❌ Error] The server {server} is offline.{RESET}\n")
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
        print(f"  🌍 {BOLD}{NEON_GREEN}Server Info : {server}{RESET}")
        print(f"  {"=" * 60}")
        print(f"  📡 {BOLD}Host:{RESET} {YELLOW}{host}{RESET}")
        print(f"  🌐 {BOLD}IP:{RESET} {LIGHT_BLUE}{ip_address}:{port}{RESET}")
        print(f"  📝 {BOLD}MOTD:{RESET} {CYAN}{motd}{RESET}")
        print(f"  🎮 {BOLD}Version:{RESET} {LIGHT_GREEN}{version}{RESET} (Protocol: {PURPLE}{protocol}{RESET})")
        print(f"  👥 {BOLD}Players:{RESET} {GREEN}{players_online}{RESET}/{RED}{max_players}{RESET}")
        print(f"  🏗️ {BOLD}Software:{RESET} {ORANGE}{software}{RESET}")
        print(f"  {"=" * 60}")

        # 🔧 Affichage des mods installés
        if mods:
            print(f"\n  🔧 {BOLD}Mods Installed ({len(mods)}):{RESET}")
            print(f"  {'-' * 50}")
            for mod in mods:
                mod_name = mod.get("name", "Unknown")
                mod_version = mod.get("version", "Unknown")
                print(f"    📦 {LIGHT_BLUE}{mod_name} {GRAY}- {YELLOW}v{mod_version}{RESET}")
            print(f"  {'-' * 50}")
        else:
            print(f"  ❌ {BOLD}No mods detected.{RESET}")

        # 🛠️ Affichage des plugins installés avec tri alphabétique
        if plugins:
            plugins_sorted = sorted(plugins, key=lambda x: x.get("name", "").lower())  # Tri alphabétique
            print(f"\n  🛠️ {BOLD}Plugins Installed ({len(plugins_sorted)}):{RESET}")
            print(f"  {'-' * 50}")
            for plugin in plugins_sorted:
                plugin_name = plugin.get("name", "Unknown")
                plugin_version = plugin.get("version", "Unknown")
                print(f"    📦 {LIGHT_BLUE}{plugin_name} {GRAY}- {YELLOW}v{plugin_version}{RESET}")
            print(f"  {'-' * 50}")
        else:
            print(f"  ❌ {BOLD}No plugins detected.{RESET}")

        # 🎭 Affichage des joueurs connectés
        if players_list:
            print(f"\n  🎭 {BOLD}Connected Players ({len(players_list)}):{RESET}")
            print(f"  {'-' * 50}")
            for player in players_list:
                player_name = player.get("name_clean", "Unknown")
                player_uuid = player.get("uuid", "Unknown")
                print(f"    👤 {LIGHT_GREEN}{player_name}{RESET} ({GRAY}{player_uuid}{RESET})")
            print(f"  {'-' * 50}")
        else:
            print(f"  ❌ {BOLD}No players currently detected.{RESET}\n")

    except requests.exceptions.RequestException as e:
        print(f"  {RED}[❌ Error] Failed to connect to API: {e}{RESET}\n")
