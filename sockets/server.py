import socket 
import threading
import sockets.server_info as server_info
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_info.ADDR)

class ServerClass:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr


    def handle_client(self):
        print(f"[NEW CONNECTION {self.addr} connected.")

        connected = True
        while connected:
            tmp = self.conn.recv(1024)
            message_string = b''
            message_string += tmp
            message_string = message_string.decode("utf-8")
            msg = json.loads(message_string)
            if msg["code"] == 1:
                connected = False
            if msg["code"] == 2:
                print("[%s] Login: %s, Password: %s" % (self.addr, msg["login"], msg["password"]))

            print("[%s] %s" % (self.addr, msg["message"]))
            self.conn.send("[Server.py - Client.py] Message recived successfully".encode(server_info.FORMAT))

        self.conn.close()

    def start(self):
        server.listen()
        print(f"[Server.py] Server is on and listening on {server_info.SERVER}")
        while True:
            self.conn, self.addr = server.accept()
            thread = threading.Thread(target=self.handle_client, args=())
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

