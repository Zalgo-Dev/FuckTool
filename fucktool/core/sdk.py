import os
import sys
import subprocess
import platform
from core.debug import debug_print
import atexit

# Configuration des chemins
SDK_BASE_PATH = os.path.abspath(r'resources')
SDK_PROCESS = None

def _get_arch_folder():
    """Détecte l'architecture du système et retourne le dossier correspondant"""
    machine = platform.machine().lower()
    is_64bit = sys.maxsize > 2**32
    
    if is_64bit or machine in ('x86_64', 'amd64'):
        return 'win64'
    elif machine in ('i386', 'x86'):
        return 'win32'
    else:
        debug_print(f"[SDK] Architecture not supported: {machine}")
        return None

def init_sdk(app_key: str) -> bool:
    """Démarre PacketSDK avec la bonne version architecturale"""
    global SDK_PROCESS
    
    arch_folder = _get_arch_folder()
    if not arch_folder:
        return False

    exe_path = os.path.join(SDK_BASE_PATH, arch_folder, 'packet_sdk.exe')
    
    if not os.path.exists(exe_path):
        debug_print(f"[SDK] File not found: {exe_path}")
        return False

    try:
        SDK_PROCESS = subprocess.Popen(
            [exe_path, f"-appkey={app_key}", "-logfile=enable"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        
        # Vérification du démarrage
        if SDK_PROCESS.poll() is not None:
            debug_print("[SDK] The process stopped immediately.")
            return False
            
        debug_print(f"[SDK] PacketSDK ({arch_folder}) start with PID {SDK_PROCESS.pid}")
        return True
        
    except Exception as e:
        debug_print(f"[SDK] Error on Startup: {str(e)}")
        return False

def shutdown_sdk():
    """Arrête proprement le processus SDK"""
    global SDK_PROCESS
    
    if SDK_PROCESS:
        try:
            # Essaye d'arrêter proprement
            SDK_PROCESS.terminate()
            try:
                SDK_PROCESS.wait(timeout=3)
            except subprocess.TimeoutExpired:
                # Force l'arrêt si nécessaire
                SDK_PROCESS.kill()
                
            debug_print("[SDK] PacketSDK process stopped.")
        except Exception as e:
            debug_print(f"[SDK] Stop error: {str(e)}")
        finally:
            SDK_PROCESS = None

# Arrêt automatique à la fin du programme
atexit.register(shutdown_sdk)