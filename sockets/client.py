import socket
import json

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = {"code": 1, "message": "Im going to disconnect myself."}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

class ClientClass:
    def __init__(self):
        pass

    def send(self, msg):
        message_string = json.dumps(DISCONNECT_MESSAGE).encode(FORMAT)
        client.send(message_string)
        # message = msg.encode(FORMAT)
        # msg_length = len(message)
        # send_length = str(msg_length).encode(FORMAT)
        # send_length += b' ' * (HEADER - len(send_length))
        # client.send(send_length)
        # client.send(message)
        # print(client.recv(2048).decode(FORMAT))

if __name__ == "__main__":
    client_instance = ClientClass()
    client_instance.send(DISCONNECT_MESSAGE)
