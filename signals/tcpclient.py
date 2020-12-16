import socket
import datetime

_ENCODING='utf-8'

class TCPClient:


    def __init__(self, port=6998):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost", port))
        print(f"{datetime.datetime.now()} - DEBUG - Connected to {port}")

    def send(self, msg, encode=_ENCODING):
        print(f"{datetime.datetime.now()} - INFO - Sent {msg}")
        self.sock.send(msg.encode(encode))


