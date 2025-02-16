import json
import urllib.parse
import requests
from datetime import datetime, timezone
from modules.colorsModule import COLOR

def format_timestamp(timestamp):
    """Convertit un timestamp UNIX en une date lisible avec timezone UTC"""
    try:
        return datetime.fromtimestamp(int(timestamp), timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
    except (ValueError, TypeError):
        return "Unknown"

def handle_details(args):
    if len(args) < 1:
        print(f"\n  {COLOR.RED}[{COLOR.LIGHT_ORANGE}Error{COLOR.RED}] {COLOR.YELLOW}Usage: details <ip> [--full]{COLOR.RESET}\n")
        return
    
    server_ip = args[0].strip()
    full_mode = "--full" in args  # Vérifie si l'option --full est activée

    # Encodage du filtre JSON pour l'API
    query = json.dumps({"ip": server_ip})
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.cornbread2100.com/servers?limit=100&query={encoded_query}"

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

        # Boucle sur tous les serveurs trouvés
        for index, server in enumerate(data):
            print(f"\n  {COLOR.NEON_BLUE}📌 Server {index + 1}/{len(data)}:{COLOR.RESET}")

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

            print("\n")

    except requests.exceptions.RequestException as e:
        print(f"  {COLOR.RED}[Error]{COLOR.YELLOW} Failed to connect to API: {e}{COLOR.RESET}\n")
