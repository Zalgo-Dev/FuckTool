from modules.colorsModule import COLOR

def handle_help(args=None):
    print(f"")
    print(f" {COLOR.NEON_RED}┌{'─' * 90}┐")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.LIGHT_RED}FuckTool - Command Help{COLOR.RESET} {' ' * 60} {COLOR.NEON_RED}│")
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
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}stress <ip:port>{COLOR.RESET}           ➜ Advanced network stress tester (500 workers max) {' ' * 7} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}    {COLOR.WHITE}--persistent{COLOR.RESET}               ➜ Maintains long-lived connections (L4) {' ' * 18} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}    {COLOR.WHITE}--minecraft{COLOR.RESET}                ➜ MC protocol flood with keep-alives (L7) {' ' * 16} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}    {COLOR.WHITE}--http{COLOR.RESET}                     ➜ HTTP flood with realistic headers {' ' * 22} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}    {COLOR.WHITE}--duration 60{COLOR.RESET}              ➜ Test duration (30-600s, default: 60) {' ' * 19} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}    {COLOR.WHITE}Note:{COLOR.RESET} Auto-HTTPS on port 443 {' ' * 56} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    print(f" {COLOR.NEON_RED}│  {' ' * 86}  │{COLOR.RESET}")

    # Section: Utilities
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  {COLOR.BOLD}{COLOR.YELLOW}Utilities:{COLOR.RESET} {' ' * 76} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}clear{COLOR.RESET}                      ➜ Clear the screen {' ' * 39} {COLOR.NEON_RED}│")
    print(f" {COLOR.NEON_RED}│{COLOR.RESET}  - {COLOR.GREEN}exit{COLOR.RESET}                       ➜ Quit MCPFuckTool {' ' * 39} {COLOR.NEON_RED}│")

    print(f" {COLOR.NEON_RED}└{'─' * 90}┘\n")