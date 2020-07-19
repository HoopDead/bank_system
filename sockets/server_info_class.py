import socket

class ServerInfo:
    def __init__(self):
        self.header = 64
        self.port = 5050
        self.server = socket.gethostbyname(socket.gethostname())
        self.addr = (self.server, self.port)
        self.encoding_format = 'utf-8'
        self.disconnect_message = {"code": 1, "message": "Im going to disconnect myself."}