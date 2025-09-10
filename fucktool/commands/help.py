from core.command_manager import BaseCommand, register_command, get_command_metadata
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

@register_command
class HelpCommand(BaseCommand):
    name = "help"
    description = "Display all available commands."
    usage = "help"

    def run(self, args=None):
        console = Console()
        
        commands = get_command_metadata()
        commands_sorted = sorted(commands, key=lambda x: x["name"])
        
        command_styles = {
            "clear": {"icon": "🧹", "color": "cyan"},
            "dns": {"icon": "🌐", "color": "blue"},
            "fakeproxy": {"icon": "🎭", "color": "magenta"},
            "help": {"icon": "❓", "color": "yellow"},
            "info": {"icon": "📊", "color": "green"},
            "proxycheck": {"icon": "🔍", "color": "orange1"},
            "scan": {"icon": "📡", "color": "bright_green"},
            "stress": {"icon": "💥", "color": "red"}
        }
        
        table = Table(show_header=False, box=None, padding=(0, 1))
        table.add_column("Command", style="", width=20)
        table.add_column("Arrow", style="dim", width=3, justify="center")
        table.add_column("Description", style="white")
        
        for cmd in commands_sorted:
            cmd_name = cmd["name"]
            cmd_desc = cmd["description"]
            
            style = command_styles.get(cmd_name, {"icon": "⚡", "color": "white"})
            icon = style["icon"]
            color = style["color"]
            
            command_cell = f"{icon} [{color}][bold]{cmd_name}[/bold][/{color}]"
            arrow_cell = "[dim]→[/dim]"
            desc_cell = cmd_desc
            
            table.add_row(command_cell, arrow_cell, desc_cell)
        
        main_panel = Panel(
            table,
            title="🔧 [bold red]FuckTool - Commands[/bold red]",
            subtitle="Advanced Minecraft Penetration Testing Tool",
            border_style="red",
            padding=(1, 2),
        )
        
        info_text = Text()
        info_text.append("💡 ", style="yellow")
        info_text.append("Usage Tips: ", style="bold")
        info_text.append("Type '<command>' for usage info  •  Use 'exit' to quit the tool\n")
        
        info_text.append("🔗 ", style="blue")
        info_text.append("Author: ", style="bold")
        info_text.append("ZalgoDev  •  ")
        info_text.append("github.com/Zalgo-Dev/FuckTool", style="link https://github.com/Zalgo-Dev/FuckTool")
        
        info_panel = Panel(
            info_text,
            border_style="dim red",
            padding=(0, 2),
        )
        
        console.print()
        console.print(main_panel)
        console.print(info_panel)
        console.print()
