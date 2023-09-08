from Controllers.TerminalController import Terminal
from datetime import datetime
import fnmatch
import json
import os

class Archives:
    def __init__(self) -> None:
        self.databaseDir = 'Database/'
        self.stateSaveDirs = []
        self.terminal = Terminal()
    
    def verifyDir(self):
        if not os.path.exists(self.databaseDir):
            os.makedirs(self.databaseDir)
    
    def setDatabase(self):
        #Função que muda o diretório padrão do banco de dados
        
        self.terminal.showText('[bold magenta]Default database location:[/bold magenta]')
        dbDir = self.terminal.getCommand()
        if os.path.exists(dbDir):
            self.databaseDir = dbDir
            self.terminal.showText(f'[bold green]Database directory changed!\n{self.databaseDir}[/bold green]')
        else:
            self.terminal.showText('[bold red]Directory is invalid or does not exist![/bold red]')
    
    
    def saveMemoryState(self, memoryState):
        #Função que salva um estado de memória no diretório do banco de dados
        
        #self.verifyDir()
        self.terminal.showText('[bold magenta]Name of this memory state:[/bold magenta]')
        memoryStateName = self.terminal.getCommand()
        pathDir = os.path.join(self.databaseDir, memoryStateName + '.json')
        try:
            with open(pathDir, 'w') as archive:
                json.dump([[memoryStateName, datetime.now().strftime(f'%d/%m/%Y, %H:%M:%S')], memoryState], archive)
                print(memoryState)
            self.terminal.showText(f'[bold green]Saved sucesfully!\n{pathDir}[/bold green]')
        except Exception as err:
            self.terminal.showError(err)
    
    
    def loadMemoryState(self):
        #Função para retornar um estado de memória salvo
        
        try:
            option = 0
            self.stateSaveDirs = []
            for root, dirs, files in os.walk(self.databaseDir):
                for currentArchive in files:
                    if fnmatch.fnmatch(currentArchive, '*.json'):
                        pathDir = os.path.join(root, currentArchive)
                        self.stateSaveDirs.append(pathDir)
            for index, file in enumerate(self.stateSaveDirs):
                self.terminal.showText(f'[bold magenta]State {index}[/bold magenta]')
                with open(file, 'r') as openFile:
                    data = json.load(openFile)
                    self.terminal.showText(f'Name: [bold green]{data[0][0]}[/bold green]\nLast change on: [bold green]{data[0][1]}[/bold green]\n')
            while True:
                option = int(self.terminal.getCommand(color='yellow', content='Index '))
                if option <= len(self.stateSaveDirs)-1 and option >= 0:
                    with open(self.stateSaveDirs[option], 'r') as chosenFileOpened:
                        data = json.load(chosenFileOpened)
                        return data[1]
                else:
                    self.terminal.showError('Enter a corresponding value in the range shown')
            
        except Exception as err:
            self.terminal.showError(err)