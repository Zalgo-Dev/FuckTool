import os
import re
import json
import subprocess
from core.command_manager import register_command, BaseCommand

@register_command
class ScanCommand(BaseCommand):
    name = "scan"
    description = "Scan dynamique d'une cible via nmap et ping Minecraft sur chaque port ouvert"
    usage = "scan <host> [ports]"

    # === 1) ping.js: JSON status ping ===
    def do_status_ping(self, ping_js: str, host: str, port: str) -> dict:
        """
        Appelle node ping.js pour un status ping Minecraft.
        Renvoie un dict: { success: bool, motd, version, players: {online, max}, error }
        """
        cmd = ["node", ping_js, host, port]
        try:
            proc = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8",
                timeout=7
            )
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "timeout"}
        except FileNotFoundError:
            return {"success": False, "error": "Node.js introuvable"}

        output = proc.stdout.strip() or proc.stderr.strip()
        try:
            data = json.loads(output)
        except json.JSONDecodeError:
            return {"success": False, "error": "JSON invalide", "raw": output}

        return data

    # === 2) bot.js: handshake complet + BungeeHack ===
    def do_ping(self, bot_js: str, host: str, port: str) -> None:
        # essai handshake standard
        result = self.try_ping(bot_js, host, port, "1.12.2")

        # si version requise, retente
        m = re.search(r"Please use version (\d+\.\d+(?:\.\d+)?)", result.get("message", ""))
        if m:
            result = self.try_ping(bot_js, host, port, m.group(1))

        msg = result.get("message", "Unknown error").replace("\n", " ").strip()
        if "Connected" in msg or "bungeehack" in msg.lower():
            ver = result.get("brand", "—")
            print(f"[scan] {host}:{port} – UP (version: {ver})")
            if result.get("plugin_channels"):
                print(f"       Plugins channels: {result['plugin_channels']}")
        else:
            print(f"[scan] {host}:{port} – DOWN ({msg})")

    def try_ping(self, bot_js: str, host: str, port: str, version: str) -> dict:
        """
        Exécute node bot.js et parse la sortie :
        message /#FuckTool#/ brand /#FuckTool#/ plugin_channels
        """
        SEP = "/#FuckTool#/"
        cmd = ["node", bot_js, host, port, version, "scanner"]
        try:
            proc = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8",
                errors="ignore",
                timeout=15
            )
        except subprocess.TimeoutExpired:
            return {"message": "Timeout"}
        except FileNotFoundError:
            return {"message": "Node.js non trouvé"}

        out = proc.stdout.strip() or proc.stderr.strip()
        if SEP in out:
            parts = out.split(SEP)
            return {
                "message": re.sub(r'&[0-9a-fk-or]', '', parts[0].strip()),
                "brand": parts[1].strip() if len(parts) > 1 else "",
                "plugin_channels": parts[2].strip() if len(parts) > 2 else ""
            }
        return {"message": out or "No response"}

    # === 3) exécution du scan nmap + ping ===
    def run(self, args):
        if len(args) < 1:
            print(f"Usage: {self.usage}")
            return

        host      = args[0]
        ports_arg = args[1] if len(args) > 1 else "1-65535"

        base    = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        bot_js  = os.path.join(base, "bungee", "bot.js")
        ping_js = os.path.join(base, "bungee", "ping.js")
        for path in (bot_js, ping_js):
            if not os.path.isfile(path):
                print(f"❌ {os.path.basename(path)} introuvable ({path})")
                return

        # scan ports ouverts
        nmap_cmd = [
            "nmap", "-p", ports_arg,
            "-n", "-T5", "-Pn", "-vvv", "-sS",
            "--open", host
        ]
        try:
            proc = subprocess.Popen(
                nmap_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                encoding="utf-8",
                errors="ignore",
                bufsize=1
            )
        except FileNotFoundError:
            print("❌ nmap non trouvé dans le PATH.")
            return

        port_re = re.compile(r"^(\d+)/tcp\s+open")
        try:
            for line in proc.stdout:
                line = line.rstrip()
                m = port_re.search(line)
                if not m:
                    continue
                port = m.group(1)
                print(f"[scan] → {host}:{port} ouvert, ping.json en cours…")
                status = self.do_status_ping(ping_js, host, port)
                if status.get("success"):
                    motd  = status.get("motd", "—")
                    ver   = status.get("version", "—")
                    pls   = status.get("players", {})
                    online = pls.get("online", "?")
                    maxp   = pls.get("max", "?")
                    print(f"       → MOTD: {motd}")
                    print(f"       → Version: {ver}")
                    print(f"       → Joueurs: {online}/{maxp}")
                else:
                    err = status.get("error", status.get("raw", "Unknown"))
                    print(f"       ping.json failed: {err}")

                # si ping.json KO, fallback handshake complet
                if not status.get("success"):
                    print(f"[scan] → fallback handshake pour {host}:{port}…")
                    self.do_ping(bot_js, host, port)

        except KeyboardInterrupt:
            print("\n[scan] → Interruption reçue, arrêt du scan…")
            proc.terminate()
            proc.wait()
            return

        proc.wait()
        print("[scan] → terminé.")
