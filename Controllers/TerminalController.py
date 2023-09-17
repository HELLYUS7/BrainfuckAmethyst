from rich.console import Console
from rich import print
from time import sleep
from Controllers.NetworkController import Network
from Utils.Constants import BF_CHARACTERS
from Info.CurrentVersion import CURRENT_VERSION
import socket
import os

class Terminal:
    def __init__(self) -> None:
        self.network = Network()
        self.console = Console()
        self.width = self.console.width
        self.height = self.console.height
    
    def clearScreen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def showStandardLogo(self) -> None:
        self.console.print(f'\n[bold magenta]- BrainfuckAmethyst v{CURRENT_VERSION} -\n[underline yellow]Design by Gabriel P.[/underline yellow][/bold magenta]\n', justify='center')
    
    def showBootLogo(self, freeMemory) -> None:
        self.showStandardLogo()
        print(f'[bold yellow]You have [magenta]{freeMemory} bytes[/magenta] of RAM...[/bold yellow]\n')
    
    def showMemory(self, memory, rowSize = 4, *args) -> None:
        for index, memoryCell in enumerate(memory):
            if index > 0 and index % int(rowSize) == 0:
                print('')
            cellCaractere = chr(memory[index])
            cellValue = str.center(cellCaractere, 4, ' ')
            print(f'[bold magenta]{str.rjust(str(index),3,"0")}[/bold magenta]|{str.rjust(str(int(memoryCell)),3,"0")}|{f"[bold red]{cellValue}[/bold red]" if cellCaractere in BF_CHARACTERS else "[bold green]Null[/bold green]"}| ', end='')
        print('')
    
    def showInfo(self) -> None:
        print(f'''
[bold magenta]BrainfuckAmethyst v{CURRENT_VERSION}\n[underline yellow]Design by Gabriel P.[/underline yellow][/bold magenta]
Pre alpha version\n
Your name: "{self.network.currentNetworkName}"
Your IP: "{self.network.ip}"
''')
    
    def showText(self, text, align='left'):
        self.console.print(text, justify=align)
    
    def showError(self, err):
        self.showText(f'[bold red]{err}[/bold red]')
    
    def getCommand(self, color='magenta', content='') -> str:
        command = self.console.input(f'[bold {color}]{content}> [/bold {color}]')
        return command