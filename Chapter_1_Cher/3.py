from threading import *
from multiprocessing import Process, Manager
path_1 = "C:\\Users\\Админ\\Documents\\Python\\Projects\\Study\\Chapter_1_Cher\\text_1.txt"
path_2 = "C:\\Users\\Админ\\Documents\\Python\\Projects\\Study\\Chapter_1_Cher\\text_2.txt"


def read(namespace):
    global a
    with open(path_1, 'r') as text:
        namespace.a = text.readlines()


def write(namespace):
    with open(path_2, 'w') as b:
        b.write(str(namespace.a))


if __name__ == '__main__':
    a = ''
    mgr = Manager()
    namespace = mgr.Namespace()
    namespace.a = mgr.Value('a', a)
    rd = Process(target=read, args=(namespace,))
    wr = Process(target=write, args=(namespace,))

    rd.start()
    wr.start()

    rd.join()
    wr.join()