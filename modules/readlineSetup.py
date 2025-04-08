import readline

def setup_completer(commands):
    def completer(text, state):
        options = [cmd for cmd in commands if cmd.startswith(text)]
        return options[state] if state < len(options) else None

    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
