from modules.colorsModule import COLOR

def show_help():
    print(f"")
    print(f" {COLOR.NEON_RED}┌{'─' * 90}┐")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.LIGHT_RED}MCPFuckTool - Command Help{COLOR.RESET} {' ' * 60} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}├{'─' * 90}┤")

    # Section: Server Information
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Server Information:{COLOR.RESET} {' ' * 67} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}info <ip:port>{COLOR.RESET}             ➜ Get server details (Title, Players, Version, etc.) {' ' * 5} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}details <ip>{COLOR.RESET}               ➜ Get advanced server information {' ' * 24} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {' ' * 30} (Geo, Secure Chat, Forge, etc.) {' ' * 24} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    # Section: Scanning Tools
    #print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Scanning Tools:{COLOR.RESET} {' ' * 71} {COLOR.NEON_RED}│")
    #print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}scan <ip> <port> <type>{COLOR.RESET}    ➜ Scan a Minecraft server with a specific scanner {' ' * 8} {COLOR.NEON_RED}│")
    #print(f" {COLOR.NEON_RED}│{COLOR.RESET}      Available types: {COLOR.CYAN}qubo, old_qubo, nmap, masscan, rustscan{COLOR.RESET} {' ' * 26} {COLOR.NEON_RED}│")

    #print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    # Section: Exploits
    #print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Exploits:{COLOR.RESET} {' ' * 77} {COLOR.NEON_RED}│")
    #print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}exploit{COLOR.RESET}                    ➜ Run an exploit {' ' * 41} {COLOR.NEON_RED}│")
    #print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}list{COLOR.RESET}                       ➜ List available exploits {' ' * 32} {COLOR.NEON_RED}│")

    #print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    # Section: Utilities
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Utilities:{COLOR.RESET} {' ' * 76} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}clear{COLOR.RESET}                      ➜ Clear the screen {' ' * 39} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}exit{COLOR.RESET}                       ➜ Quit MCPFuckTool {' ' * 39} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}└{'─' * 90}┘\n")