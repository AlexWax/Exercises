from socket import *
from concurrent import futures as cf

TCP_ID = 'localhost'
TCP_Port = 8000


class TSP_Client_File:
    def __init__(self, ide, port):
        self.server_id = (ide, port)
        self.file_name = 'C:\\Users\\Админ\\Documents\\Python\\Projects\\Study\\Chapter_2_Cher\\Text.txt'

        self.client()

    def client(self):
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect(self.server_id)
            print(f'CLIENT || Connect to {self.server_id}')
            while True:
                with open(self.file_name, 'r') as file:
                    data = file.read()
                    if not data: break
                    print(f'CLIENT || Send file, wait server response')
                    sock.sendall(data.encode('utf-8'))

                serv_ans = sock.recv(1024)
                print(f'CLIENT || Get response. Close connection')
                if serv_ans:
                    break


class TSP_Server_File:
    def __init__(self, ide, port):
        self.server_id = (ide, port)
        self.file_name = 'New_Text'
        self.server()

    def handle(self, new_socket, address):
        print('SERVER || Get connection')
        while True:
            data = new_socket.recv(1024)
            if not data: break
            print(f'SERVER || Get file, start writing')
            with open(self.file_name, 'w') as file:
                file.write(data.decode('utf-8'))

            print(f'SERVER || Write file, sent response')
            new_socket.sendall('True'.encode('utf-8'))
        new_socket.close()
        print('SERVER || Lose connection')

    def server(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(self.server_id)
        sock.listen(5)

        with cf.ThreadPoolExecutor(20) as clients:
            try:
                while True:
                    new_socket, address = sock.accept()
                    clients.submit(self.handle, new_socket, address)
            except KeyboardInterrupt: pass
            finally:
                sock.close()


if __name__ == '__main__':
    from multiprocessing import *
    from threading import *

    server = Process(target=TSP_Server_File, args=(TCP_ID, TCP_Port))
    client = Process(target=TSP_Client_File, args=(TCP_ID, TCP_Port))

    server.start()
    client.start()
    client.join()
    server.terminate()
