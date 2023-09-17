import socket

class Network:
    def __init__(self) -> None:
        self.currentNetworkName = socket.gethostname()
        self.ip = socket.gethostbyname(self.currentNetworkName)
    