# core/debug.py

import traceback
import logging
from config import Config
from core.colors import YELLOW, NEON_ORANGE, RESET, GRAY

DEBUG_MODE = Config.DEBUG

def setup_debug():
    """Configure logging en fonction du DEBUG_MODE."""
    if DEBUG_MODE:
        logging.basicConfig(
            filename='debug.log',
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    else:
        logging.basicConfig(level=logging.CRITICAL)

def debug_print(msg):
    if DEBUG_MODE:
        print(f"{GRAY}[{YELLOW}DEBUG{GRAY}]{RESET} {msg}")
        logging.debug(msg)

def handle_exception(e):
    print(f"\n{GRAY}[{NEON_ORANGE}ERROR{GRAY}]{RESET} {e}{RESET}")
    if DEBUG_MODE:
        traceback.print_exc()
        logging.exception("Exception interceptée")
