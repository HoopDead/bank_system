import socket
import json
import server_info

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_info.ADDR)

"""
client.py
=====================
Handle ClientClass, that have to provide correct way to treat client in sockets
"""

class ClientClass:
    """
    Handle functions to keep client alive and communicate with server

    Arg:
    Null
    """
    def __init__(self):
        pass

    def send(self, msg):
        """
        Send function to send message to server

        :param msg (dict): Takes dictionary with code, message and optionaly arguments to send to server
        """
        message_string = json.dumps(msg).encode(server_info.FORMAT)
        client.send(message_string)
        print(client.recv(2048).decode(server_info.FORMAT))

if __name__ == "__main__":
    # client_instance = ClientClass()
    # client_instance.send(server_info.LOGIN_MESSAGE)
    # client_instance.send(server_info.DISCONNECT_MESSAGE)
