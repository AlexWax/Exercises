from socket import *
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 8883


def run_client(ip, port):
    message = 'Mama mila ramu?'
    print(f'CLIENT || Send: {message}')
    print('------------')
    mes_out = ''
    sock = socket(AF_INET, SOCK_DGRAM)
    server = (ip, port)
    for word in message.split(' '):
        data = word.encode('utf-8')
        sock.sendto(data, server)
        print(f'CLIENT || Send: {repr(data)} to {server}')
        response, address = sock.recvfrom(1024)
        mes_out += response.decode('utf-8') + ' '
        print(f"CLIENT || Get: {response.decode('utf-8')} from {address}")
    print('------------')
    print(f"CLIENT || Get {mes_out}")

def run_server(ip, port):
    sock = socket(AF_INET, SOCK_DGRAM)
    server = (ip, port)
    sock.bind(server)
    mes = 'Net ne mila!'
    i = 0
    while True:
        data, address = sock.recvfrom(1024)
        print(f"SERVER || Get: {data.decode('utf-8')} from {address}")
        new_data = f'{mes.split(" ")[i]}'
        sock.sendto(new_data.encode('utf-8'), address)
        print(f"SERVER || Send: {new_data} to {address}")
        i += 1


if __name__ == '__main__':
    from multiprocessing import Process

    client = Process(target=run_client, args=(UDP_IP, UDP_PORT,))
    server = Process(target=run_server, args=(UDP_IP, UDP_PORT,))
    server.start()
    client.start()
    client.join()
    server.terminate()