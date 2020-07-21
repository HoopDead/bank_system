import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = {"code": 1, "message": "[!] Client is going to disconnect."}
LOGIN_MESSAGE = {"code": 2, "message": "[!] Client wants to log in.", "login": "", "password": ""}
