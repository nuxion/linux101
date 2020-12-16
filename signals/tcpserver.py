import socket
import logging
import threading
import datetime

logger = logging.getLogger(__name__)
_ENCODING = 'utf-8'

class TCPServer:

    def __init__(self, port=6999):
        self.srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.conn = None

    def recv(self):
        while True:
            data = self.srv.recv(1024)

    def listen(self):
        self.srv.bind(('127.0.0.1', self.port))
        self.srv.listen(2)
        print(f'Listening on: {self.port}')
        self.conn, addr = self.srv.accept()
        print(f"{datetime.datetime.now()} - DEBUG - conntected from {addr}")
        while True:
            data = self.conn.recv(1024)
            deco_data = data.decode(_ENCODING)
            print(f"{datetime.datetime.now()} - INFO - {deco_data}")

if __name__ == '__main__':
    import sys
    try:
        custom_port = int(sys.argv[1])
    except IndexError:
        custom_port = 6999

    srv = TCPServer(port=custom_port)
    srv.listen()

