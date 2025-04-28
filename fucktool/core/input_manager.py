from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from pathlib import Path

# Définir un style pour le prompt
custom_style = Style.from_dict({
    'bracket': '#ff0000 bold',
    'arrow': '#ffffff bold',
})

def get_command_input(commands):
    """
    Affiche un prompt interactif stylisé avec autocomplétion et historique
    """
    # Configuration de l'historique
    history = FileHistory(str(Path(__file__).parent.parent / '.fucktool_history'))
    
    # Configuration de l'autocomplétion
    completer = WordCompleter(commands, ignore_case=True, sentence=True)

    # Prompt en HTML stylé
    prompt_text = HTML('<bracket>[</bracket><arrow>></arrow><bracket>]</bracket> ')

    user_input = prompt(
        prompt_text,
        completer=completer,
        style=custom_style,
        history=history  # Ajout de l'historique ici
    )
    return user_input