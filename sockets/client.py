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
        # message = msg.encode(FORMAT)
        # msg_length = len(message)
        # send_length = str(msg_length).encode(FORMAT)
        # send_length += b' ' * (HEADER - len(send_length))
        # client.send(send_length)
        # client.send(message)
        # print(client.recv(2048).decode(FORMAT))

if __name__ == "__main__":
    client_instance = ClientClass()
    client_instance.send(server_info.LOGIN_MESSAGE)
    client_instance.send(server_info.DISCONNECT_MESSAGE)
