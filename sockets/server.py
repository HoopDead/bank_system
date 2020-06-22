import socket 
import threading
from .server_info import HEADER, PORT, SERVER, ADDR, FORMAT, DISCONNECT_MESSAGE

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

class ServerClass:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr


    def handle_client(self):
        print(f"[NEW CONNECTION {self.addr} connected.")

        connected = True
        while connected:
            msg_length = self.conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{self.addr}] {msg}")
                self.conn.send("[!] Message recived successfully".encode(FORMAT))

        self.conn.close()

    def start(self):
        server.listen()
        print(f"[LISTENING] Server is listening on {SERVER}")
        while True:
            self.conn, self.addr = server.accept()
            thread = threading.Thread(target=self.handle_client, args=())
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

