from threading import *
from time import *


def lstk(*pos: iter):
    global lst
    print(pos)
    for i in range(len(pos)):
        mylock.acquire()
        if pos[i]%2 == 1:
            lst[pos[i]] = i
        else:
            lst[pos[i]] = chr(i+65)
        mylock.release()


lst = ['*' for i in range(10)]
mylock = Semaphore(2)
a = Thread(target=lstk, args=[i for i in range(10) if i % 2 == 1])
b = Thread(target=lstk, args=[i for i in range(10) if i % 2 == 0])
a.start()
b.start()
a.join()
b.join()
print(lst)
