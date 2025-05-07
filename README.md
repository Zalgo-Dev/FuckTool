# FuckTool

![GitHub all releases downloads](https://img.shields.io/github/downloads/Zalgo-Dev/FuckTool/total) [![VirusTotal](https://img.shields.io/badge/VirusTotal-Scanned-brightgreen?logo=virustotal&style=flat-square)](https://www.virustotal.com/gui/file/27bfec696a504a8099f59ec7866894c8e2fc291c34783ab0f67dfc4ddc80453f)


FuckTool is a modular Minecraft penetration testing suite, built for researchers and ethical hackers. It includes tools to analyze, stress-test, and simulate proxy behavior on Minecraft servers.

> Educational use only. You are responsible for how you use this tool.

![image](https://github.com/user-attachments/assets/6ff708cd-d4ae-433a-a1c7-d54e4a790384)
---

## Features

- Server info gathering (MOTD, version, players, Forge, Secure Chat, etc.)

- DNS lookup (A, AAAA, MX, TXT, ...)

- Layer 4 and Layer 7 stress testing (TCP / Minecraft / HTTP)

- Fake Velocity proxy launcher (with plugin and forwarding support)

- Command-line history, autocomplete and modular CLI

- Clean output and structured help system

---

## Project Structure

```bash
FuckTool/
├── fucktool/
│   ├── main.py                     # Entry point
│   ├── config.py                   # Global constants
│   ├── commands/                   # All CLI commands
│   │   ├── info.py                 # Get Minecraft server info
│   │   ├── stress.py               # Run network stress tests
│   │   ├── dns.py                  # DNS lookup tool
│   │   └── ...                     # More tools
│   ├── core/                       # Internal engine (colors, header, input, etc.)
│   │   ├── command_manager.py
│   │   ├── input_manager.py
│   │   └── ...
│   ├── FakeProxy/                  # Velocity proxy with plugin
│   │   ├── velocity.jar
│   │   ├── plugins/
│   │   └── velocity.toml
│   └── resources/
│       ├── fucktool.ico
│       └── install.bat
├── counter.py                      # (Optional utility script)
├── requirements.txt
├── LICENSE.md
└── README.md
```

FuckTool is organized into isolated modules:

- `commands/` → CLI logic for each user command

- `core/` → Console rendering, banner, input hooks

- `FakeProxy/` → Prebuilt Velocity proxy for spoofing / IP-forward testing

- `resources/` → Icons, batch tools, structure documentation

Every command is a Python file. To add a new command, just drop a yourcmd.py file into commands/ and register it in the command manager.

📄 [How to create your own command module](docs/writing_custom_commands.md)

---

## Installation

```bash
git clone https://github.com/Zalgo-Dev/FuckTool.git

cd FuckTool

pip install -r requirements.txt

python fucktool/main.py
```

Alternatively, you can download the latest packaged installer from the **[releases page](https://github.com/Zalgo-Dev/FuckTool/releases)**.

> Type `help` to list all commands.

---

## Available Commands

| commands | descriptions |
|--|---|
| ``clear`` | - Clear the screen and re-display banner |
| ``dns`` | - Perform DNS record lookup |
| ``fakeproxy`` | - Launch a local Velocity proxy with config |
| ``help`` | - Show all available commands |
| ``info`` | - Get basic server info |
| ``stress`` | - Run L4/L7 stress tests (up to 500 workers) |

---

## FakeProxy Module

`fucktool/FakeProxy/` contains:

- A ready-to-use [Velocity](https://papermc.io/software/velocity) proxy

- A custom admin plugin (`FakeProxyAdmin`) to control behavior

- A valid `forwarding.secret` for IP-forwarding simulation

- Plugins folder and preconfigured TOML

This makes it easy to test how a Minecraft server handles fake proxies, spoofed IPs or modified handshake packets.

---

## Requirements

+ Python 3.8+

---

## Author
**Made by [ZalgoDev](https://github.com/Zalgo-Dev) – focused on security, Minecraft internals, and ethical exploitation.**

---

Disclaimer
This tool is for authorized testing only.
Using it without explicit permission on servers you do not own is illegal.
The author is not responsible for abuse or damages.