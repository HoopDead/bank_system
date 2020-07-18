import socket 
import threading
from .server_info import HEADER, PORT, SERVER, ADDR, FORMAT, DISCONNECT_MESSAGE
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

class ServerClass:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr


    def handle_client(self):
        print(f"[NEW CONNECTION {self.addr} connected.")

        connected = True
        message_string = b''
        while connected:
            tmp = self.conn.recv(1024)
            message_string += tmp
            msg = json.loads(message_string.decode())
            if msg["code"] == 1:
                connected = False

            print("[%s] %s" % (self.addr, msg["message"]))
            self.conn.send("[!] Message recived successfully".encode(FORMAT))
            # if msg_length:
            #     msg = self.conn.recv(msg_length).decode(FORMAT)
            #     if msg["code"] == 1:
            #         connected = False

            #     print(f"[{self.addr}] {msg}")
            #     self.conn.send("[!] Message recived successfully".encode(FORMAT))

        self.conn.close()

    def start(self):
        server.listen()
        print(f"[Server.py] Server is on and listening on {SERVER}")
        while True:
            self.conn, self.addr = server.accept()
            thread = threading.Thread(target=self.handle_client, args=())
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

