from threading import *
from time import *

def left():
    global first, last, j
    while True:
        if last > first:
            lst[last] = j
            last -= 1
            j += 1
            sleep(0.1)
        else:
            break



def right():
    global first, last, j
    while True:
        if last > first:
            lst[first] = chr(j+64)
            first += 1
            j += 1
            sleep(0.1)
        else:
            break



j = 0
first = 0
last = 10
lst = ['*' for i in range(11)]

Left = Thread(target=left)
Right = Thread(target=right)
Left.start()
Right.start()
Left.join()
Right.join()

print(lst)