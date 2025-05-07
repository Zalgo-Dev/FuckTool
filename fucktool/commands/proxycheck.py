from core.command_manager import BaseCommand, register_command
from core.colors import GREEN, RED, YELLOW, RESET, WHITE, BOLD, GRAY
import requests
import re

@register_command
class ProxyCheckCommand(BaseCommand):
    name = "proxycheck"
    description = "Check if an IP or domain is a proxy/VPN or belongs to a datacenter"
    usage = "proxycheck <ip|domain>"

    def run(self, args):
        if len(args) != 1:
            print(f"\n {BOLD}{WHITE}[{RED}!{WHITE}] Usage: {self.usage}\n")
            return

        target = args[0]
        
        # Supprimer le port si présent (ex: domain.com:8080 -> domain.com)
        target = target.split(':')[0]
        
        # Vérifier si c'est une IP ou un domaine valide
        if not re.match(r'^([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', target) and not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', target):
            print(f"\n {BOLD}{WHITE}[{RED}!{WHITE}] Invalid IP or domain format\n")
            return

        print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Checking {BOLD}{target}{RESET} via ip-api.com...\n")

        try:
            response = requests.get(f"http://ip-api.com/json/{target}?fields=66846719", timeout=10)
            data = response.json()

            if data.get("status") != "success":
                print(f"{RED} Failed to get info for {target}: {data.get('message', 'Unknown error')}{RESET}")
                return

            isp = data.get("isp", "Unknown")
            org = data.get("org", "Unknown")
            country = data.get("country", "Unknown")
            hosting = data.get("hosting", False)
            mobile = data.get("mobile", False)
            proxy = data.get("proxy", False)

            print(f"{GREEN} IP Info:{RESET}")
            print(f"  {WHITE}• Country:{RESET} {YELLOW}{country}{RESET}")
            print(f"  {WHITE}• ISP:{RESET} {YELLOW}{isp}{RESET}")
            print(f"  {WHITE}• Org:{RESET} {YELLOW}{org}{RESET}")
            print(f"  {WHITE}• Proxy/VPN:{RESET} {RED if proxy else GREEN}{proxy}{RESET}")
            print(f"  {WHITE}• Hosting/DC:{RESET} {RED if hosting else GREEN}{hosting}{RESET}")
            print(f"  {WHITE}• Mobile:{RESET} {YELLOW if mobile else GREEN}{mobile}{RESET}\n")

        except requests.exceptions.RequestException as e:
            print(f"{RED} Request failed: {e}{RESET}")