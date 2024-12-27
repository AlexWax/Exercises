from socket import *
from concurrent import futures as cf

TCP_Port = 8000
TCP_ID = 'localhost'


class TCP_Client_Mes:
    def __init__(self, idi, port):
        self.server_id = (idi, port)
        self.client()

    def client(self):
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect(self.server_id)
            print(f'CLIENT || Connect to {self.server_id}')
            while True:
                msg_for_server = input("CLIENT || Write your message for server: ")
                if not msg_for_server: break
                sock.sendall(msg_for_server.encode('utf-8'))
                response_from_server = sock.recv(1024)
                print(f'CLIENT || Get from server: {response_from_server.decode("utf-8")}')


class TCP_Server_Mes:
    def __init__(self, ide, port):
        self.server_id = (ide, port)
        self.server()

    def handle(self, new_sock, address):
        print('SERVER || Get connection')
        while True:
            msg_from_client = new_sock.recv(1024)
            print(f'SERVER || Get from client: {msg_from_client.decode("utf-8")}')
            msg_to_client = input("SERVER || Write your message for client: ")
            if not msg_to_client: break
            new_sock.sendall(msg_to_client.encode('utf-8'))
        new_sock.close()

    def server(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(self.server_id)
        sock.listen(5)
        print(f'Start server: {sock.getsockname()}')
        with cf.ThreadPoolExecutor(1) as clients:
            try:
                while True:
                    new_sock, address = sock.accept()
                    clients.submit(self.handle, new_sock, address)
            except KeyboardInterrupt: pass
            finally:
                sock.close()


if __name__ == '__main__':
    from multiprocessing import Process
    from threading import Thread

    client = Thread(target=TCP_Client_Mes, args=(TCP_ID, TCP_Port))
    server = Thread(target=TCP_Server_Mes, args=(TCP_ID, TCP_Port))
    server.start()
    client.start()
    client.join()
