import socket
import threading
import datetime
import signal

_ENCODING = 'utf-8'

    

class TCPServer:

    def __init__(self, port=6999):
        self.srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.conn = None
        
        signal.signal(signal.SIGINT, self.keyboard)

    def __enter__(self):
        print(f'Listening on: {self.port}')
        self.srv.bind(('127.0.0.1', self.port))
        self.srv.listen(2)
        self.conn, addr = self.srv.accept()
        print(f"{datetime.datetime.now()} - DEBUG - Client connected from {addr}")
        return self.conn

    def __exit__(self, type, value, traceback):
        self._close()

    def _close(self):
        self.srv.close()
        exit(0)

    def keyboard(self, signal, frame):
        print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
        self._close()


if __name__ == '__main__':
    import sys
    try:
        custom_port = int(sys.argv[1])
    except IndexError:
        custom_port = 6999
    with TCPServer(port=custom_port) as conn:
        ok = True
        while ok:
            try:
                data = conn.recv(1024)
                if data:
                    print(f"{datetime.datetime.now()} - INFO - {data}")
                else:
                    print(f"{datetime.datetime.now()} - ERROR - Socket closed by the client")
                    ok = False

            except OSError:
                print(f"{datetime.datetime.now()} - ERROR - Socket closed by the client")
                ok = False
                exit(0)
                



