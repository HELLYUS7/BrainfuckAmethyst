from Controllers.ArchivesController import Archives

class Memory:
    def __init__(self, size) -> None:
        self.archives = Archives()
        self.memory = [0 for i in range(size)]
    
    def saveMemoryState(self):
        self.archives.saveMemoryState(self.memory)
    
    def loadMemory(self):
        self.memory = self.archives.loadMemoryState()