from modules.colorsModule import COLOR

def handle_help(args=None):
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

    # Nouvelle Section: Network Tools
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Network Tools:{COLOR.RESET} {' ' * 72} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}dns <ip|domain>{COLOR.RESET}            ➜ Perform DNS lookup and show records {' ' * 20} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {' ' * 30} (A, AAAA, MX, TXT, etc.) {' ' * 31} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}stress <ip:port>{COLOR.RESET}           ➜ DDOS {' ' * 51} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}    {COLOR.WHITE}--layer 4{COLOR.RESET}                  ➜ TCP SYN flood (transport layer) {' ' * 24} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}    {COLOR.WHITE}--layer 7{COLOR.RESET}                  ➜ MC protocol flood (application layer) {' ' * 18} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}    {COLOR.WHITE}--duration 30{COLOR.RESET}              ➜ Max test duration (seconds) {' ' * 28} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    # Section: Utilities
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Utilities:{COLOR.RESET} {' ' * 76} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}clear{COLOR.RESET}                      ➜ Clear the screen {' ' * 39} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}exit{COLOR.RESET}                       ➜ Quit MCPFuckTool {' ' * 39} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}└{'─' * 90}┘\n")