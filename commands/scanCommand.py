import socket
import json
import struct
import itertools
import argparse
from concurrent.futures import ThreadPoolExecutor
from modules.colorsModule import COLOR

def get_minecraft_version(host, port=25565, timeout=2):
    """ Récupère la version d'un serveur Minecraft si en ligne. """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((host, port))

            host_bytes = host.encode('utf-8')
            handshake_packet = (
                b"\x00" + b"\x47" + struct.pack(">B", len(host_bytes)) + host_bytes + struct.pack(">H", port) + b"\x01"
            )

            sock.send(struct.pack(">B", len(handshake_packet)) + handshake_packet)
            sock.send(b"\x01\x00")

            data_length = sock.recv(1)
            if not data_length:
                return None

            data_length = struct.unpack(">B", data_length)[0]
            data = sock.recv(data_length)

            json_data = data[3:].decode('utf-8')
            status = json.loads(json_data)
            return status.get("version", {}).get("name", "Unknown Version")

    except:
        return None  # Hors ligne ou non Minecraft

def expand_ip_range(ip_range):
    """ Génère toutes les combinaisons possibles à partir d'un format d'IP personnalisé. """
    segments = ip_range.split(".")
    ranges = []

    for seg in segments:
        if "-" in seg:
            start, end = map(int, seg.split("-"))
            ranges.append(range(start, end + 1))
        elif seg == "*":
            ranges.append(range(0, 256))
        else:
            ranges.append([int(seg)])

    return [".".join(map(str, ip)) for ip in itertools.product(*ranges)]

def parse_port_range(port_range):
    """ Convertit un port ou un range en liste de ports. """
    if "-" in port_range:
        start_port, end_port = map(int, port_range.split("-"))
        return list(range(start_port, end_port + 1))
    return [int(port_range)]

def scan_server(ip, port):
    """ Scanne un serveur Minecraft sur un port spécifique. """
    version = get_minecraft_version(ip, port)
    if version:
        print(f"  {COLOR.GREEN}[✔] {COLOR.BOLD}{ip}:{port} - Serveur en ligne (Version: {COLOR.YELLOW}{version}{COLOR.GREEN}){COLOR.RESET}")
    else:
        print(f"  {COLOR.RED}[✘] {COLOR.BOLD}{ip}:{port} - Hors ligne ou non Minecraft{COLOR.RESET}")

def handle_scan(args):
    """ Fonction principale pour le scan. """
    if len(args) != 2:
        print(f"\n  {COLOR.RED}[{COLOR.LIGHT_ORANGE}Error{COLOR.RED}] {COLOR.YELLOW}Usage: scan <ip-range> <port-range>{COLOR.RESET}\n")
        return

    ip_range = args[0].strip()
    port_range = args[1].strip()

    ip_list = expand_ip_range(ip_range)
    port_list = parse_port_range(port_range)

    print(f"\n  {COLOR.GRAY}[{COLOR.RED}#{COLOR.GRAY}] {COLOR.WHITE}Lancement du scan sur {COLOR.NEON_GREEN}{len(ip_list)} IPs {COLOR.RESET} et {COLOR.NEON_GREEN}{len(port_list)} ports{COLOR.RESET}...\n")

    with ThreadPoolExecutor(max_workers=20) as executor:
        for ip in ip_list:
            for port in port_list:
                executor.submit(scan_server, ip, port)
