from Controllers.TerminalController import Terminal
import json
import os

class Archives:
    def __init__(self) -> None:
        self.databaseDir = 'Database/'
        self.terminal = Terminal()
    
    def verifyDir(self):
        if not os.path.exists(self.databaseDir):
            os.makedirs(self.databaseDir)
    
    def setDatabase(self):
        self.terminal.showText('[bold magenta]Default database location:[/bold magenta]')
        dbDir = self.terminal.getCommand()
        if os.path.exists(dbDir):
            self.databaseDir = dbDir
            self.terminal.showText(f'[bold green]Database directory changed!\n{self.databaseDir}[/bold green]')
        else:
            self.terminal.showText('[bold red]Directory is invalid or does not exist![/bold red]')
    
    
    def saveMemoryState(self, memoryState):
        #self.verifyDir()
        self.terminal.showText('[bold magenta]Name of this memory state:[/bold magenta]')
        memoryStateName = self.terminal.getCommand()
        pathDir = os.path.join(self.databaseDir, memoryStateName + '.json')
        try:
            with open(pathDir, 'w') as archive:
                json.dump(memoryState, archive)
            self.terminal.showText(f'[bold green]Saved sucesfully!\n{pathDir}[/bold green]')
        except Exception as err:
            self.terminal.showText(f'[bold red]{err}[/bold red]')
    
    
    def loadMemoryState(self):
        pass