from threading import *

class List:
    def __init__(self):
        self.list_1 = ['' for i in range(10)]
        self.list_2 = [0 for i in range(10)]

def lst1():
    i = 0
    while True:
        if i<10:
            A.list_1[i] = chr(i+64)
            i+=1
            print(A.list_1)
        else:
            break

def lst2():
    i = 0
    while True:
        if i<10:
            A.list_2[i] = i
            i+=1
            print(A.list_2)
        else:
            break


A = List()
mylock = Lock()
l1 = Thread(target=lst1)
l2 = Thread(target=lst2)
l1.start()
l2.start()
l1.join()
l2.join()
print(A.list_1, A.list_2)