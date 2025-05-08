# core/honeysdk.py
"""
Module Python pour intégrer et piloter Honeygain SDK sous Windows.
Les DLL doivent se trouver dans : 
    <projet>/fucktool/resources/hgsdk/x86/bin/hgsdk.dll 
    <projet>/fucktool/resources/hgsdk/x64/bin/hgsdk.dll
"""
import os
import platform
import atexit
from ctypes import CDLL, c_int32, c_char_p, byref, POINTER

# Détection de l'architecture
ARCH, _ = platform.architecture()
ARCH_FOLDER = 'x64' if ARCH == '64bit' else 'x86'

# Chemin vers le dossier resources/hgsdk dans le même package
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SDK_RESOURCES = os.path.join(BASE_DIR, 'resources', 'hgsdk')

# Construction du chemin vers la DLL
DLL_PATH = os.path.join(SDK_RESOURCES, ARCH_FOLDER, 'bin', 'hgsdk.dll')
if not os.path.isfile(DLL_PATH):
    raise FileNotFoundError(f"Honeygain SDK DLL introuvable: {DLL_PATH}")

# Chargement de la bibliothèque
_sdk = CDLL(DLL_PATH)

# Définition des prototypes de fonctions
_sdk.hgsdk_start.argtypes       = [c_char_p, POINTER(c_int32)]
_sdk.hgsdk_start.restype        = c_int32

_sdk.hgsdk_stop.argtypes        = []
_sdk.hgsdk_stop.restype         = c_int32

_sdk.hgsdk_is_running.argtypes  = [POINTER(c_int32)]
_sdk.hgsdk_is_running.restype   = c_int32

_sdk.hgsdk_opt_in.argtypes      = []
_sdk.hgsdk_opt_in.restype       = c_int32

_sdk.hgsdk_opt_out.argtypes     = []
_sdk.hgsdk_opt_out.restype      = c_int32

_sdk.hgsdk_is_opted_in.argtypes = [POINTER(c_int32)]
_sdk.hgsdk_is_opted_in.restype  = c_int32

_sdk.hgsdk_request_consent.argtypes = [POINTER(c_int32)]
_sdk.hgsdk_request_consent.restype  = c_int32

_sdk.hgsdk_log.argtypes         = [c_char_p]
_sdk.hgsdk_log.restype          = c_int32

_sdk.hgsdk_mute.argtypes        = []
_sdk.hgsdk_mute.restype         = c_int32

# Wrappers Python

def start(api_key: str) -> bool:
    """
    Démarre le service SDK. Retourne True si le consentement a été donné.
    """
    key = api_key.encode('utf-8')
    state = c_int32()
    res = _sdk.hgsdk_start(c_char_p(key), byref(state))
    if res < 0:
        raise RuntimeError('Échec du démarrage de Honeygain SDK')
    return bool(state.value)


def stop() -> None:
    """Arrête le service SDK."""
    res = _sdk.hgsdk_stop()
    if res < 0:
        raise RuntimeError('Échec de l\'arrêt de Honeygain SDK')


def is_running() -> bool:
    """Vérifie si le service SDK est en cours d'exécution."""
    state = c_int32()
    res = _sdk.hgsdk_is_running(byref(state))
    if res < 0:
        raise RuntimeError('Échec de la vérification du statut')
    return bool(state.value)


def opt_in() -> None:
    """Enregistre le consentement utilisateur et autorise le démarrage."""
    res = _sdk.hgsdk_opt_in()
    if res < 0:
        raise RuntimeError('Échec de l\'opt-in')


def opt_out() -> None:
    """Révoque le consentement utilisateur et arrête si en cours."""
    res = _sdk.hgsdk_opt_out()
    if res < 0:
        raise RuntimeError('Échec de l\'opt-out')


def is_opted_in() -> bool:
    """Retourne l'état du consentement utilisateur."""
    state = c_int32()
    res = _sdk.hgsdk_is_opted_in(byref(state))
    if res < 0:
        raise RuntimeError('Échec de la vérification du consentement')
    return bool(state.value)


def request_consent() -> bool:
    """Affiche la fenêtre de consentement à l'utilisateur (bloquant)."""
    state = c_int32()
    res = _sdk.hgsdk_request_consent(byref(state))
    if res < 0:
        raise RuntimeError('Échec de la requête de consentement')
    return bool(state.value)


def log(directory: str = None) -> None:
    """Active le logging dans le répertoire spécifié."""
    path = directory or os.getcwd()
    res = _sdk.hgsdk_log(c_char_p(path.encode('utf-8')))
    if res < 0:
        raise RuntimeError('Échec de l\'activation du logging')


def mute() -> None:
    """Désactive le logging."""
    res = _sdk.hgsdk_mute()
    if res < 0:
        raise RuntimeError('Échec de la désactivation du logging')

# Arrêt automatique à la fermeture
atexit.register(stop)
