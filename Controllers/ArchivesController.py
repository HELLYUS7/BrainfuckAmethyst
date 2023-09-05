from Controllers.TerminalController import Terminal
import json
import os

class Archives:
    def __init__(self) -> None:
        self.terminal = Terminal()
    
    def getLocalMemory(self):
        self.terminal.showText('[bold green]Local do arquivo:[/bold green]')
        a = self.terminal.getCommand()
        self.terminal.showText(f'[bold green]Batman: "{a}"[/bold green]')