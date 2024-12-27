from socketserver import (BaseRequestHandler, TCPServer)
from multiprocessing import Process
from socket import *

TCP_IP = 'localhost'
TCP_PORT = 8000


class Client:
    def __init__(self, ip, port):
        self.msg = 'MAMA mila RaMu'
        self.server = (ip, port)

        self.client()

    def client(self):
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect(self.server)
            for word in self.msg.split(' '):
                sock.sendall(word.encode('utf-8'))
                response = sock.recv(1024)
                print(f'CLIENT || Get: {response.decode("utf-8")}')


class EchoTCP(BaseRequestHandler):
    def handle(self):
        print(f'SERVER || Connection with {self.client_address} started')
        while True:
            msg = self.request.recv(1024)
            if not msg: break
            print(f'SERVER || Get: {msg} from {self.client_address}')
            self.request.send(msg)


if __name__ == '__main__':
    server = TCPServer((TCP_IP, TCP_PORT), EchoTCP)
    client = Process(target=Client, args=(TCP_IP, TCP_PORT,))
    client.start()
    server.serve_forever()
