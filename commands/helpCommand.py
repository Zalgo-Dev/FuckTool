from modules.colorsModule import COLOR

def handle_help():
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

    # Section: Utilities
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Utilities:{COLOR.RESET} {' ' * 76} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}clear{COLOR.RESET}                      ➜ Clear the screen {' ' * 39} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}exit{COLOR.RESET}                       ➜ Quit MCPFuckTool {' ' * 39} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}└{'─' * 90}┘\n")