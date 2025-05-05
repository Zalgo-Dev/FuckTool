# fucktool/commands/dns.py

import dns.resolver
import socket
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from core.colors import (
    RED, LIGHT_ORANGE, YELLOW, RESET, GRAY, WHITE, GREEN, LIGHT_BLUE,
    NEON_GREEN, BLUE, NEON_BLUE, CYAN, LIGHT_GREEN, BOLD
)
from core.command_manager import BaseCommand, register_command


@register_command
class DNSCommand(BaseCommand):
    name = "dns"
    description = "Perform DNS lookup and show records"
    usage = "dns <ip|domain>"

    def run(self, args):
        if len(args) != 1:
            print(f"\n {BOLD}{WHITE}[{RED}!{WHITE}] Usage: {self.usage}\n")
            return

        target = args[0].strip()

        try:
            print(f"\n  {GRAY}[{RED}#{GRAY}]{WHITE} Analyzing DNS records for {NEON_GREEN}{target}{RESET}...\n")

            is_cloudflare, real_ip = self.check_cloudflare(target)

            try:
                ip = socket.gethostbyname(target)
                print(f"  {BLUE}🔍 Basic Resolution:{RESET}")
                print(f"  {'─' * 50}")
                print(f"  {WHITE}• {GREEN}Hostname/IP:{RESET} {LIGHT_BLUE}{target}{RESET}")

                if is_cloudflare and real_ip:
                    print(f"  {WHITE}• {GREEN}Cloudflare Protected:{RESET} {RED}Yes{RESET}")
                    print(f"  {WHITE}• {GREEN}Real IP (possible):{RESET} {NEON_BLUE}{real_ip}{RESET}")
                else:
                    print(f"  {WHITE}• {GREEN}Resolved IP:{RESET} {NEON_BLUE}{ip}{RESET}")
                    if is_cloudflare:
                        print(f"  {WHITE}• {GREEN}Cloudflare Protected:{RESET} {RED}Yes{RESET}")

                print(f"  {'─' * 50}\n")
            except socket.gaierror:
                print(f"  {RED}❌ Could not resolve basic IP address{RESET}\n")

            record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'CNAME', 'SOA']
            print(f"  {BLUE}📊 Advanced DNS Records:{RESET}")
            print(f"  {'═' * 50}")

            for record_type in record_types:
                try:
                    answers = dns.resolver.resolve(target, record_type)
                    print(f"  {WHITE}• {YELLOW}{record_type} Records:{RESET}")

                    for rdata in answers:
                        if record_type == 'MX':
                            print(f"    {LIGHT_GREEN}Priority {rdata.preference}:{RESET} {CYAN}{rdata.exchange}{RESET}")
                        elif record_type == 'SOA':
                            print(f"    {LIGHT_GREEN}Primary NS:{RESET} {CYAN}{rdata.mname}{RESET}")
                            print(f"    {LIGHT_GREEN}Admin Mail:{RESET} {CYAN}{rdata.rname}{RESET}")
                            print(f"    {LIGHT_GREEN}Serial:{RESET} {CYAN}{rdata.serial}{RESET}")
                        else:
                            print(f"    {CYAN}{rdata}{RESET}")

                    print(f"  {'─' * 25}")
                except dns.resolver.NoAnswer:
                    print(f"  {WHITE}• {YELLOW}{record_type} Records:{RESET} {RED}None found{RESET}")
                    print(f"  {'─' * 25}")
                except dns.resolver.NXDOMAIN:
                    print(f"  {RED}❌ Domain does not exist{RESET}")
                    break
                except dns.resolver.Timeout:
                    print(f"  {RED}❌ DNS query timed out{RESET}")
                    break
                except dns.exception.DNSException as e:
                    print(f"  {RED}❌ DNS error: {e}{RESET}")
                    continue

            try:
                print(f"\n  {BLUE}🔁 Reverse DNS Lookup:{RESET}")
                print(f"  {'─' * 50}")
                hostname, _, _ = socket.gethostbyaddr(real_ip if is_cloudflare and real_ip else ip)
                print(f"  {WHITE}• {GREEN}IP:{RESET} {LIGHT_BLUE}{real_ip if is_cloudflare and real_ip else ip}{RESET}")
                print(f"  {WHITE}• {GREEN}Hostname:{RESET} {NEON_BLUE}{hostname}{RESET}")
            except (socket.herror, socket.gaierror):
                print(f"  {RED}❌ No reverse DNS record found{RESET}")

            print(f"\n  {GREEN}✅ DNS analysis completed{RESET}\n")

        except Exception as e:
            print(f"\n  {RED}❌ Critical error: {e}{RESET}\n")

    def check_cloudflare(self, target):
        try:
            ns_records = dns.resolver.resolve(target, 'NS')
            for ns in ns_records:
                if 'cloudflare' in str(ns).lower():
                    real_ip = self.find_real_ip(target)
                    return True, real_ip

            if not target.startswith(('http://', 'https://')):
                target = 'http://' + target

            response = requests.get(target, timeout=10)
            if 'cloudflare' in response.headers.get('server', '').lower():
                real_ip = self.find_real_ip(target)
                return True, real_ip
        except Exception:
            pass

        return False, None

    def find_real_ip(self, domain):
        try:
            subdomains = ['direct', 'origin', 'server', 'ip', 'ftp', 'mail']
            for sub in subdomains:
                try:
                    ip = socket.gethostbyname(f"{sub}.{domain}")
                    if ip:
                        return ip
                except:
                    continue

            try:
                url = f"https://viewdns.info/iphistory/?domain={domain}"
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, headers=headers, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
                tables = soup.find_all('table')
                for table in tables:
                    if 'IP Address' in table.text:
                        rows = table.find_all('tr')
                        for row in rows[1:]:
                            cols = row.find_all('td')
                            if len(cols) >= 2:
                                ip = cols[0].text.strip()
                                if ip and not ip.startswith(('104.', '172.', '192.', '141.')):
                                    return ip
            except:
                pass

            try:
                url = f"https://securitytrails.com/domain/{domain}/dns"
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    ip_section = soup.find('section', {'id': 'A'})
                    if ip_section:
                        ips = ip_section.find_all('code')
                        for ip in ips:
                            ip_text = ip.text.strip()
                            if ip_text and not ip_text.startswith(('104.', '172.', '192.', '141.')):
                                return ip_text
            except:
                pass
        except Exception:
            return None

        return None
