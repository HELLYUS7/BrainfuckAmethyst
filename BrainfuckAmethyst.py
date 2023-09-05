from Controllers.ArchivesController import Archives
from Controllers.TerminalController import Terminal
from Controllers.NetworkController import Network
from rich import print
from time import sleep 

class OS:
    def __init__(self, ROMsize = 2048, RAMsize = 32) -> None:
        self.terminal = Terminal()
        self.network = Network()
        self.archives = Archives()
        self.databaseDir = '/Database/'
        self.ROMmemory = [0 for i in range(ROMsize)]
        self.RAMmemory = [0 for i in range(RAMsize)]
        self.commands = {
            '$clear': self.terminal.clearScreen,
            '$exit': self.exitOS,
            '$setDB': self.setDatabase,
            '$memory': self.showMemoryWrapper,
            '$load': self.loadMemory,
            '$info': self.terminal.showInfo,
            }
    
    def process_command(self, command_line):
        parts = command_line.split()
        if parts:
            command = str(parts[0])
            args = parts[1:]
            
            if command.isnumeric():
                self.currentAdressPointer = int(command)
            elif command in self.commands:
                self.commands[command](*args)
            else:
                print(f'Unknown command "{command}"')
        else:
            print(f'Type a command...')
    
    def setDatabase(self, dbDir=''):
        if dbDir != '':
            self.databaseDir = dbDir
            self.terminal.showText(f'[bold green]Database directory changed!\n{self.databaseDir}[/bold green]')
        else:
            self.terminal.showText('[bold red]The directory entered is empty[/bold red]')
    
    def loadMemory(self):
        self.RAMmemory = self.archives.getLocalMemory()
    
    def showMemoryWrapper(self, *args):
        self.terminal.showMemory(self.RAMmemory, *args)
    
    def exitOS(self):
        return exit(0)
    
    def boot(self):
        return self.runKernel()
    
    def runKernel(self):
        self.terminal.clearScreen()
        self.terminal.showBootLogo(freeROM=len(self.ROMmemory), freeRAM=len(self.RAMmemory))
        while True:
            commandUser = self.terminal.getCommand()
            self.process_command(command_line=commandUser)
        
if __name__ == '__main__':
    operationalSystem = OS()
    operationalSystem.boot()