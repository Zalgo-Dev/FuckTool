import requests
from modules.colorsModule import COLOR

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

        # 🛠️ Affichage des plugins installés avec tri alphabétique
        if plugins:
            plugins_sorted = sorted(plugins, key=lambda x: x.get("name", "").lower())  # Tri alphabétique
            print(f"\n  🛠️ {COLOR.BOLD}Plugins Installed ({len(plugins_sorted)}):{COLOR.RESET}")
            print(f"  {'-' * 50}")
            for plugin in plugins_sorted:
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
            print(f"  ❌ {COLOR.BOLD}No players currently detected.{COLOR.RESET}\n")

    except requests.exceptions.RequestException as e:
        print(f"  {COLOR.RED}[❌ Error] Failed to connect to API: {e}{COLOR.RESET}\n")
