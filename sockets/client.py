import socket
import json
import server_info

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_info.ADDR)

class ClientClass:
    def __init__(self):
        pass

    def send(self, msg):
        message_string = json.dumps(msg).encode(server_info.FORMAT)
        client.send(message_string)
        print(client.recv(2048).decode(server_info.FORMAT))

if __name__ == "__main__":
    # client_instance = ClientClass()
    # client_instance.send(server_info.LOGIN_MESSAGE)
    # client_instance.send(server_info.DISCONNECT_MESSAGE)
