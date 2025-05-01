from core.colors import NEON_RED, RESET, LIGHT_RED, BOLD, YELLOW, GREEN, WHITE

def handle_help(args=None):
    print(f"")
    print(f" {NEON_RED}┌{'─' * 90}┐")
    print(f" {NEON_RED}│{RESET}  {LIGHT_RED}FuckTool - Command Help{RESET} {' ' * 63} {NEON_RED}│")
    print(f" {NEON_RED}├{'─' * 90}┤")

    # Section: Server Information
    print(f" {NEON_RED}│{RESET}  {BOLD}{YELLOW}Server Information:{RESET} {' ' * 67} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}  - {GREEN}info <ip:port>{RESET}             ➜ Get server details (Title, Players, Version, etc.) {' ' * 5} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}  - {GREEN}details <ip>{RESET}               ➜ Get advanced server information {' ' * 24} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}  {' ' * 30} (Geo, Secure Chat, Forge, etc.) {' ' * 24} {NEON_RED}│")

    print(f" {NEON_RED}│  {' ' * 86}  │{RESET}")

    # Nouvelle Section: Network Tools
    print(f" {NEON_RED}│{RESET}  {BOLD}{YELLOW}Network Tools:{RESET} {' ' * 72} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}  - {GREEN}dns <ip|domain>{RESET}            ➜ Perform DNS lookup and show records {' ' * 20} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}  {' ' * 30} (A, AAAA, MX, TXT, etc.) {' ' * 31} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}  - {GREEN}stress <ip:port>{RESET}           ➜ Advanced network stress tester (500 workers max) {' ' * 7} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}    {WHITE}--persistent{RESET}               ➜ Maintains long-lived connections (L4) {' ' * 18} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}    {WHITE}--minecraft{RESET}                ➜ MC protocol flood with keep-alives (L7) {' ' * 16} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}    {WHITE}--http{RESET}                     ➜ HTTP flood with realistic headers {' ' * 22} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}    {WHITE}--duration 60{RESET}              ➜ Test duration (30-600s, default: 60) {' ' * 19} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}    {WHITE}Note:{RESET} Auto-HTTPS on port 443 {' ' * 56} {NEON_RED}│")

    print(f" {NEON_RED}│  {' ' * 86}  │{RESET}")

    print(f" {NEON_RED}│  {' ' * 86}  │{RESET}")

    # Section: Utilities
    print(f" {NEON_RED}│{RESET}  {BOLD}{YELLOW}Utilities:{RESET} {' ' * 76} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}  - {GREEN}clear{RESET}                      ➜ Clear the screen {' ' * 39} {NEON_RED}│")
    print(f" {NEON_RED}│{RESET}  - {GREEN}exit{RESET}                       ➜ Quit FuckTool {' ' * 39} {NEON_RED}│")

    print(f" {NEON_RED}└{'─' * 90}┘\n")