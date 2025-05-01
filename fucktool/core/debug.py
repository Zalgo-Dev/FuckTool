# core/debug.py

import traceback
import logging
from config import Config
from core.colors import YELLOW, RED, RESET

DEBUG_MODE = Config.DEBUG

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
        print(f"{YELLOW}[DEBUG]{RESET} {msg}")
        logging.debug(msg)


def handle_exception(e):
    print(f"\n{RED}Error: {e}{RESET}")
    if DEBUG_MODE:
        traceback.print_exc()
        logging.exception("Exception interceptée")
