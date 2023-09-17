from Controllers.ArchivesController import Archives
from Controllers.TerminalController import Terminal
from Controllers.NetworkController import Network
from Controllers.MemoryController import Memory
from rich import print
from time import sleep 

class OS:
    def __init__(self, MemorySize = 32) -> None:
        self.terminal = Terminal()
        self.network = Network()
        self.archives = Archives()
        self.memory = Memory(MemorySize)
        self.commands = {
            '$clear': self.terminal.clearScreen,
            '$exit': self.exitOS,
            '$setDB': self.archives.setDatabase,
            '$save': self.memory.saveMemoryState,
            '$memory': self.showMemoryWrapper,
            '$load': self.memory.loadMemory,
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
    
    def showMemoryWrapper(self, *args):
        self.terminal.showMemory(self.memory.memory, *args)
    
    def exitOS(self):
        return exit(0)
    
    def boot(self):
        return self.runKernel()
    
    def runKernel(self):
        self.terminal.clearScreen()
        self.terminal.showBootLogo(freeMemory=len(self.memory.memory))
        while True:
            commandUser = self.terminal.getCommand()
            self.process_command(command_line=commandUser)
        
if __name__ == '__main__':
    operationalSystem = OS()
    operationalSystem.boot()