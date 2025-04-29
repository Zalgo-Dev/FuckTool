import os
import subprocess
import platform
import toml
from core.colors import COLOR
from colorama import init, Fore, Back, Style
from time import sleep
from time import strftime
import re

Black = Fore.BLACK
Blue = Fore.BLUE
Red = Fore.RED
Green = Fore.GREEN
Cyan = Fore.CYAN
Magenta = Fore.MAGENTA
White = Fore.WHITE
Yellow = Fore.YELLOW
LightWhite = Fore.LIGHTWHITE_EX
LightBlue = Fore.LIGHTBLUE_EX
LightGreen = Fore.LIGHTGREEN_EX
LightRed = Fore.LIGHTRED_EX
Bold = Style.BRIGHT
Reset = Style.RESET_ALL

def validate_fakeproxy_input(parts):
    if len(parts) < 3:
        print(White + Bold + "\n[" + Reset + Red + Bold + "!" + Reset + White + Bold + "] Usage: fakeproxy [ServerIP] [Method]\n")
        return False
    
    server_ip = parts[1]
    method = parts[2].lower()

    valid_methods = ["modern", "none", "other_method"]
    if method not in valid_methods:
        print(White + Bold + "[" + Reset + Red + Bold + "#" + Reset + White + Bold + "] Incorrect method! Valid methods: 'modern', 'none', 'other_method'")
        return False

    return True

def handle_pinggy_io():
    print(White + Bold + "[" + Reset + Green + Bold + "#" + Reset + White + Bold + "] Do you want to use pinggy.io for a public IP? (y/n)")
    choice = input(White + Bold + "[" + Reset + Green + Bold + "#" + Reset + White + Bold + "] Enter your choice: ").lower()

    if choice == 'n':
        return "skip"  # Instead of None, return a flag to indicate skipping

    elif choice == 'y':
        print(White + Bold + "[" + Reset + Green + Bold + "#" + Reset + White + Bold + "] Run this SSH command in a separate terminal to obtain a public IP:\n")
        ssh_command = " ssh -p 443 -R0:localhost:25577 tcp@a.pinggy.io"
        print(White + Bold + "[" + Reset + Green + Bold + "#" + Reset + White + Bold + "]" f"{ssh_command}\n")

        public_url = input(White + Bold + "[" + Reset + Green + Bold + "#" + Reset + White + Bold + "] Enter the public URL obtained from pinggy.io: ").strip()
        public_url = public_url.replace("tcp://", "")
        domain, port = public_url.split(":")

        print(White + Bold + "[" + Reset + Green + Bold + "*" + Reset + White + Bold + "]" f" Resolving public IP for: {domain}...")
        nslookup_command = f"nslookup {domain}"
        result = subprocess.run(nslookup_command, capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            output = result.stdout.splitlines()
            for i, line in enumerate(output):
                if line.strip().startswith("Addresses:") and i + 1 < len(output):
                    ip_line = output[i + 1].strip()
                    if "." in ip_line:
                        public_ip_with_port = f"{ip_line}:{port}"
                        print(White + Bold + "[" + Reset + Green + Bold + "#" + Reset + White + Bold + "]" f" Public IP obtained: {public_ip_with_port}\n")
                        return public_ip_with_port

        print(White + Bold + "[" + Reset + Red + Bold + "#" + Reset + White + Bold + "] Error: Could not retrieve a valid IPv4 address from nslookup.")
        return None
    
    return None

global base_dir
def configure_proxy(server_ip, method):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    proxy_config_file = os.path.join(base_dir, '../FakeProxy/velocity.toml')


    if not os.path.exists(proxy_config_file):
        print(White + Bold + "[" + Reset + Red + Bold + "#" + Reset + White + Bold + "] Error: Proxy configuration file does not exist.")
        return False

    print(White + Bold + "[" + Reset + Green + Bold + "#" + Reset + White + Bold + "] Configuring Proxy...")

    try:
        # Load existing TOML configuration
        with open(proxy_config_file, 'r') as file:
            config = toml.load(file)

        # Update settings correctly
        config['servers'] = {"lobby": server_ip}
        config['player-info-forwarding-mode'] = method
        config['bind'] = "0.0.0.0:25577"
        config["forced-hosts"][server_ip] = ["lobby"]
        config['log-commands'] = True
        config['log-connections'] = True

        # Write back the corrected TOML file
        with open(proxy_config_file, 'w') as file:
            toml.dump(config, file)

        print(White + Bold + "[" + Reset + Green + Bold + "#" + Reset + White + Bold + "] Proxy configured successfully.")

    except Exception as e:
        print(White + Bold + "[" + Reset + Red + Bold + "#" + Reset + White + Bold + f"] Error configuring proxy: {e}")
        return False

    return True

def get_time():
    """Extracts and formats the current timestamp."""
    return strftime("%H:%M:%S")

def format_log(message):
    """Formats logs with timestamp and FakeProxy tag."""
    return f"[{get_time()}] FakeProxy Log - {message}"

def extract_velocity_log(line):
    """Parses raw Velocity logs and extracts useful information."""
    
    # Regex patterns
    join_pattern = re.compile(r"\[(\d{2}:\d{2}:\d{2}) INFO\]: \[connected player\] (\S+) \(\/(\S+):\d+\) has connected")
    leave_pattern = re.compile(r"\[(\d{2}:\d{2}:\d{2}) INFO\]: \[connected player\] (\S+) \(\/(\S+):\d+\) has disconnected")
    command_pattern = re.compile(r"\[(\d{2}:\d{2}:\d{2}) INFO\]: \[connected player\] (\S+) \(\/(\S+):\d+\) -> executed command (.+)")
    
    # Matching logs
    if join_match := join_pattern.search(line):
        timestamp, user, ip = join_match.groups()
        return f"{White}{Bold}[{Reset}{Green}{Bold}#{Reset}{White}{Bold}][{timestamp}] FakeProxy Log - {user} ({ip}) Joined the fakeproxy!"
    
    elif leave_match := leave_pattern.search(line):
        timestamp, user, ip = leave_match.groups()
        return f"{White}{Bold}[{Reset}{Green}{Bold}#{Reset}{White}{Bold}][{timestamp}] FakeProxy Log - {user} ({ip}) leaved the fakeproxy!"
    
    elif command_match := command_pattern.search(line):
        timestamp, user, ip, command = command_match.groups()
        return f"{White}{Bold}[{Reset}{Green}{Bold}#{Reset}{White}{Bold}][{timestamp}] FakeProxy Log - {user} ({ip}) executed command {Bold}{Green}{command} {Reset} on the fakeproxy!"
    
    return None  # No matching log format


def run_velocity():
    """Runs the Velocity proxy and captures logs."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    proxy_folder = os.path.join(base_dir, '../FakeProxy')
    velocity_path = os.path.join(proxy_folder, "velocity.jar")

    if not os.path.exists(velocity_path):
        print(format_log("Error: velocity.jar not found in Proxy folder!"))
        return

    print(format_log("Starting Proxy..."))

    try:
        process = subprocess.Popen(
            ["java", "-jar", velocity_path],
            cwd=proxy_folder,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        # Create a Windows toast notification object
        toaster = ToastNotifier()

        while True:
            line = process.stdout.readline()
            if not line:
                break

            line = line.strip()
            custom_log = extract_velocity_log(line)
            if "Done" in line:
                print(format_log("Velocity Proxy Started Successfully!"))

            if custom_log:
                print(custom_log)  # Print only relevant logs

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] CTRL+C detected. Shutting down FakeProxy...")
    finally:
        try:
            process.terminate()
            process.wait(timeout=5)
        except Exception:
            process.kill()
        print(f"{Fore.YELLOW}[FakeProxy] Process terminated cleanly.")



def main_fakeproxy(parts):
    if not validate_fakeproxy_input(parts):
        return  # Only show usage, no "Returning to main menu"
    global public_ip

    server_ip = parts[1]
    method = parts[2].lower()
    public_ip = handle_pinggy_io()

    # ✅ If "n" is chosen, just continue using server_ip instead of public_ip
    if public_ip == "skip":
        public_ip = "localhost:25577"  # Use the server's IP instead

    elif public_ip is None:
        print(White + Bold + "[" + Reset + Red + Bold + "#" + Reset + White + Bold + "] No valid public IP obtained.")
        print(White + Bold + "[" + Reset + Yellow + Bold + "#" + Reset + White + Bold + "] Do you want to retry? (y/n)")
        choice = input(White + Bold + "[" + Reset + Yellow + Bold + "#" + Reset + White + Bold + "] Enter your choice: ").lower()
        if choice == "y":
            return main_fakeproxy(parts)  # Retry fakeproxy setup
        else:
            print(White + Bold + "[" + Reset + Red + Bold + "#" + Reset + White + Bold + "] Returning to main menu...")
            return

    print(White + Bold + "[" + Reset + Green + Bold + "#" + Reset + White + Bold + "]" f" Using IP: {public_ip}")

    if configure_proxy(server_ip, method):
        run_velocity()
    else:
        print(White + Bold + "[" + Reset + Red + Bold + "#" + Reset + White + Bold + "] Proxy configuration failed.")
        print(White + Bold + "[" + Reset + Yellow + Bold + "#" + Reset + White + Bold + "] Do you want to retry? (y/n)")
        choice = input(White + Bold + "[" + Reset + Yellow + Bold + "#" + Reset + White + Bold + "] Enter your choice: ").lower()
        if choice == "y":
            return main_fakeproxy(parts)  # Retry fakeproxy setup
        else:
            print(White + Bold + "[" + Reset + Red + Bold + "#" + Reset + White + Bold + "] Returning to main menu...")
            return

# Function Completed for V 1.2.0"
