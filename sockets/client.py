import socket
from .server_info import HEADER, PORT, SERVER, ADDR, FORMAT, DISCONNECT_MESSAGE

class ClientClass:
    def __init__(self):
        pass

    def send(self, msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        print(client.recv(2048).decode(FORMAT))