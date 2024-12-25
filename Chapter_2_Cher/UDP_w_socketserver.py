from socketserver import UDPServer, BaseRequestHandler
from socket import *

UDP_IP = '127.0.0.8'
UDP_Port = 8883


class Client:
    def __init__(self, ip, port):
        self.msg = 'Mamam mila Ranu'
        self.server = (ip, port)
        self.client()

    def client(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        for word in self.msg.split(' '):
            sock.sendto(word.encode('utf-8'), self.server)
            data, address = sock.recvfrom(1024)
            print(f'CLIENT || Get: {data.decode("utf-8")} from {address}')


class EchoUDP(BaseRequestHandler):
    def handle(self):
        data, sock = self.request
        sock.sendto(data, self.client_address)


if __name__ == '__main__':
    from multiprocessing import *

    server = UDPServer((UDP_IP, UDP_Port), EchoUDP)
    client = Process(target=Client, args=(UDP_IP, UDP_Port))

    client.start()
    server.serve_forever()