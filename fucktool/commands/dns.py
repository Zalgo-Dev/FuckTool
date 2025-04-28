import dns.resolver
import socket
import requests
from bs4 import BeautifulSoup
from core.colors import COLOR
from urllib.parse import urlparse

def handle_dns(args):
    if len(args) != 1:
        print(f"\n  {COLOR.RED}[{COLOR.LIGHT_ORANGE}Error{COLOR.RED}] {COLOR.YELLOW}Usage: dns <ip/domain>{COLOR.RESET}\n")
        return
    
    target = args[0].strip()
    
    try:
        print(f"\n  {COLOR.GRAY}[{COLOR.RED}#{COLOR.GRAY}]{COLOR.WHITE} Analyzing DNS records for {COLOR.NEON_GREEN}{target}{COLOR.RESET}...\n")
        
        # Vérification initiale Cloudflare
        is_cloudflare, real_ip = check_cloudflare(target)
        
        # Résolution de base
        try:
            ip = socket.gethostbyname(target)
            print(f"  {COLOR.BLUE}🔍 Basic Resolution:{COLOR.RESET}")
            print(f"  {'─' * 50}")
            print(f"  {COLOR.WHITE}• {COLOR.GREEN}Hostname/IP:{COLOR.RESET} {COLOR.LIGHT_BLUE}{target}{COLOR.RESET}")
            
            if is_cloudflare and real_ip:
                print(f"  {COLOR.WHITE}• {COLOR.GREEN}Cloudflare Protected:{COLOR.RESET} {COLOR.RED}Yes{COLOR.RESET}")
                print(f"  {COLOR.WHITE}• {COLOR.GREEN}Real IP (possible):{COLOR.RESET} {COLOR.NEON_BLUE}{real_ip}{COLOR.RESET}")
            else:
                print(f"  {COLOR.WHITE}• {COLOR.GREEN}Resolved IP:{COLOR.RESET} {COLOR.NEON_BLUE}{ip}{COLOR.RESET}")
                if is_cloudflare:
                    print(f"  {COLOR.WHITE}• {COLOR.GREEN}Cloudflare Protected:{COLOR.RESET} {COLOR.RED}Yes{COLOR.RESET}")
            
            print(f"  {'─' * 50}\n")
        except socket.gaierror:
            print(f"  {COLOR.RED}❌ Could not resolve basic IP address{COLOR.RESET}\n")
        
        # Records DNS avancés
        record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'CNAME', 'SOA']
        
        print(f"  {COLOR.BLUE}📊 Advanced DNS Records:{COLOR.RESET}")
        print(f"  {'═' * 50}")
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(target, record_type)
                print(f"  {COLOR.WHITE}• {COLOR.YELLOW}{record_type} Records:{COLOR.RESET}")
                
                for rdata in answers:
                    if record_type == 'MX':
                        print(f"    {COLOR.LIGHT_GREEN}Priority {rdata.preference}:{COLOR.RESET} {COLOR.CYAN}{rdata.exchange}{COLOR.RESET}")
                    elif record_type == 'SOA':
                        print(f"    {COLOR.LIGHT_GREEN}Primary NS:{COLOR.RESET} {COLOR.CYAN}{rdata.mname}{COLOR.RESET}")
                        print(f"    {COLOR.LIGHT_GREEN}Admin Mail:{COLOR.RESET} {COLOR.CYAN}{rdata.rname}{COLOR.RESET}")
                        print(f"    {COLOR.LIGHT_GREEN}Serial:{COLOR.RESET} {COLOR.CYAN}{rdata.serial}{COLOR.RESET}")
                    else:
                        print(f"    {COLOR.CYAN}{rdata}{COLOR.RESET}")
                
                print(f"  {'─' * 25}")
            except dns.resolver.NoAnswer:
                print(f"  {COLOR.WHITE}• {COLOR.YELLOW}{record_type} Records:{COLOR.RESET} {COLOR.RED}None found{COLOR.RESET}")
                print(f"  {'─' * 25}")
            except dns.resolver.NXDOMAIN:
                print(f"  {COLOR.RED}❌ Domain does not exist{COLOR.RESET}")
                break
            except dns.resolver.Timeout:
                print(f"  {COLOR.RED}❌ DNS query timed out{COLOR.RESET}")
                break
            except dns.exception.DNSException as e:
                print(f"  {COLOR.RED}❌ DNS error: {e}{COLOR.RESET}")
                continue
        
        # Reverse DNS
        try:
            print(f"\n  {COLOR.BLUE}🔁 Reverse DNS Lookup:{COLOR.RESET}")
            print(f"  {'─' * 50}")
            hostname, _, _ = socket.gethostbyaddr(real_ip if is_cloudflare and real_ip else ip)
            print(f"  {COLOR.WHITE}• {COLOR.GREEN}IP:{COLOR.RESET} {COLOR.LIGHT_BLUE}{real_ip if is_cloudflare and real_ip else ip}{COLOR.RESET}")
            print(f"  {COLOR.WHITE}• {COLOR.GREEN}Hostname:{COLOR.RESET} {COLOR.NEON_BLUE}{hostname}{COLOR.RESET}")
        except (socket.herror, socket.gaierror):
            print(f"  {COLOR.RED}❌ No reverse DNS record found{COLOR.RESET}")
        
        print(f"\n  {COLOR.GREEN}✅ DNS analysis completed{COLOR.RESET}\n")
        
    except Exception as e:
        print(f"\n  {COLOR.RED}❌ Critical error: {e}{COLOR.RESET}\n")

def check_cloudflare(target):
    """Détecte si un domaine est protégé par Cloudflare et tente de trouver l'IP réelle"""
    try:
        # Vérification des serveurs DNS
        ns_records = dns.resolver.resolve(target, 'NS')
        for ns in ns_records:
            if 'cloudflare' in str(ns).lower():
                # Tentative de trouver l'IP réelle
                real_ip = find_real_ip(target)
                return True, real_ip
                
        # Vérification via les en-têtes HTTP
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
            
        response = requests.get(target, timeout=10)
        if 'cloudflare' in response.headers.get('server', '').lower():
            real_ip = find_real_ip(target)
            return True, real_ip
            
    except Exception:
        pass
        
    return False, None

def find_real_ip(domain):
    """Tente de trouver l'IP réelle derrière Cloudflare"""
    try:
        # Méthode 1: Vérification des sous-domaines communs
        subdomains = ['direct', 'origin', 'server', 'ip', 'ftp', 'mail']
        for sub in subdomains:
            try:
                ip = socket.gethostbyname(f"{sub}.{domain}")
                if ip:
                    return ip
            except:
                continue
                
        # Méthode 2: Analyse historique DNS
        try:
            url = f"https://viewdns.info/iphistory/?domain={domain}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            tables = soup.find_all('table')
            for table in tables:
                if 'IP Address' in table.text:
                    rows = table.find_all('tr')
                    for row in rows[1:]:  # Skip header
                        cols = row.find_all('td')
                        if len(cols) >= 2:
                            ip = cols[0].text.strip()
                            if ip and not ip.startswith(('104.', '172.', '192.', '141.')):
                                return ip
        except:
            pass
            
        # Méthode 3: Vérification des enregistrements DNS historiques
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