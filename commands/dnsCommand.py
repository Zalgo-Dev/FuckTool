import dns.resolver
import socket
from modules.colorsModule import COLOR

def handle_dns(args):
    if len(args) != 1:
        print(f"\n  {COLOR.RED}[{COLOR.LIGHT_ORANGE}Error{COLOR.RED}] {COLOR.YELLOW}Usage: dns <ip/domain>{COLOR.RESET}\n")
        return
    
    target = args[0].strip()
    
    try:
        print(f"\n  {COLOR.GRAY}[{COLOR.RED}#{COLOR.GRAY}]{COLOR.WHITE} Analyzing DNS records for {COLOR.NEON_GREEN}{target}{COLOR.RESET}...\n")
        
        # Résolution de base
        try:
            ip = socket.gethostbyname(target)
            print(f"  {COLOR.BLUE}🔍 Basic Resolution:{COLOR.RESET}")
            print(f"  {'─' * 50}")
            print(f"  {COLOR.WHITE}• {COLOR.GREEN}Hostname/IP:{COLOR.RESET} {COLOR.LIGHT_BLUE}{target}{COLOR.RESET}")
            print(f"  {COLOR.WHITE}• {COLOR.GREEN}Resolved IP:{COLOR.RESET} {COLOR.NEON_BLUE}{ip}{COLOR.RESET}")
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
            hostname, _, _ = socket.gethostbyaddr(ip)
            print(f"  {COLOR.WHITE}• {COLOR.GREEN}IP:{COLOR.RESET} {COLOR.LIGHT_BLUE}{ip}{COLOR.RESET}")
            print(f"  {COLOR.WHITE}• {COLOR.GREEN}Hostname:{COLOR.RESET} {COLOR.NEON_BLUE}{hostname}{COLOR.RESET}")
        except (socket.herror, socket.gaierror):
            print(f"  {COLOR.RED}❌ No reverse DNS record found{COLOR.RESET}")
        
        print(f"\n  {COLOR.GREEN}✅ DNS analysis completed{COLOR.RESET}\n")
        
    except Exception as e:
        print(f"\n  {COLOR.RED}❌ Critical error: {e}{COLOR.RESET}\n")