import os
import readline
import atexit

def setup_history(history_file):
    try:
        readline.read_history_file(history_file)
    except FileNotFoundError:
        open(history_file, 'wb').close()
    atexit.register(readline.write_history_file, history_file)
