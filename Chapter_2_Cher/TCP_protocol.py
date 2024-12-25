from socket import *
import time
from concurrent import futures as cf

TCP_IP = 'localhost'
TCP_PORT = 8883


def run_client(ip, port):
    message = 'Mama mila ramu?'
    server = (ip, port)

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(server)
        print(f'CLIENT || Connect to {server}')
        for word in message.split(' '):
            sock.sendall(word.encode('utf-8'))
            print(f'CLIENT || Send: {word}')
            response = sock.recv(1024)
            print(f"CLIENT || Get: {response.decode('utf-8')}")
    print(f'CLIENT || Connection to {server} closed')


def run_server(ip, port):
    def handle(new_sock, address):
        print(f'SERVER || Connection started')
        while True:
            data = new_sock.recv(1024)
            if not data: break
            print(f"SERVER || Get: {data.decode('utf-8')} from {address}")
            new_sock.sendall(data)
            print(f"SERVER || Send: {data} to {address}")
        new_sock.close()
        print(f'SERVER || Connection closed')

    servsock = socket(AF_INET, SOCK_STREAM)
    server = (ip, port)
    servsock.bind(server)
    servsock.listen(5)
    print(f'SERVER || Start server {servsock.getsockname()}')

    with cf.ThreadPoolExecutor(20) as client_pool:
        try:
            while True:
                new_sock, address = servsock.accept()
                client_pool.submit(handle, new_sock, address)
        except KeyboardInterrupt: pass
        finally: servsock.close()


if __name__ == '__main__':
    from multiprocessing import Process

    client = Process(target=run_client, args=(TCP_IP, TCP_PORT,))
    server = Process(target=run_server, args=(TCP_IP, TCP_PORT,))
    server.start()
    client.start()
    client.join()
    server.terminate()