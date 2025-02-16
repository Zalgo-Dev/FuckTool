import requests
from modules.colorsModule import COLOR

def handle_search(args):
    if len(args) != 0:
        print(f"\n  {COLOR.RED}[{COLOR.LIGHT_ORANGE}Error{COLOR.RED}] {COLOR.YELLOW}Usage: bungeecord{COLOR.RESET}\n")
        return
    
    url = "https://api.cornbread2100.com/servers?skip=0&limit=5&query={\"description\": {\"$regex\": \"bungeecord\", \"$options\": \"i\"}, \"players.online\": {\"$gte\": 20, \"$lte\": 100}}"
    
    try:
        print(f"\n  {COLOR.GRAY}[{COLOR.RED}#{COLOR.GRAY}]{COLOR.WHITE} Fetching BungeeCord servers...{COLOR.RESET}\n")
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            print(f"  {COLOR.RED}[❌ Error] Failed to fetch servers (Status Code: {response.status_code}){COLOR.RESET}\n")
            return
        
        data = response.json()
        
        if not data:
            print(f"  {COLOR.RED}[❌ Error] No BungeeCord servers found.{COLOR.RESET}\n")
            return
        
        for server in data:
            ip = server.get("ip", "Unknown")
            port = server.get("port", "Unknown")
            description = server.get("description", "No Description")
            country = server.get("geo", {}).get("country", "Unknown")
            city = server.get("geo", {}).get("city", "Unknown")
            players_online = server.get("players", {}).get("online", 0)
            max_players = server.get("players", {}).get("max", 0)
            version = server.get("version", {}).get("name", "Unknown")
            
            print(f"  {"=" * 60}")
            print(f"  🌍 {COLOR.BOLD}{COLOR.NEON_GREEN}BungeeCord Server:{COLOR.RESET}")
            print(f"  {"=" * 60}")
            print(f"  📡 {COLOR.BOLD}IP:{COLOR.RESET} {COLOR.LIGHT_BLUE}{ip}:{port}{COLOR.RESET}")
            print(f"  📝 {COLOR.BOLD}Description:{COLOR.RESET} {COLOR.CYAN}{description}{COLOR.RESET}")
            print(f"  🌍 {COLOR.BOLD}Location:{COLOR.RESET} {COLOR.YELLOW}{city}, {country}{COLOR.RESET}")
            print(f"  🎮 {COLOR.BOLD}Version:{COLOR.RESET} {COLOR.LIGHT_GREEN}{version}{COLOR.RESET}")
            print(f"  👥 {COLOR.BOLD}Players:{COLOR.RESET} {COLOR.GREEN}{players_online}{COLOR.RESET}/{COLOR.RED}{max_players}{COLOR.RESET}")
            print(f"  {"=" * 60}\n")
    
    except requests.exceptions.RequestException as e:
        print(f"  {COLOR.RED}[❌ Error] Failed to connect to API: {e}{COLOR.RESET}\n")