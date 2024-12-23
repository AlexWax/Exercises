from threading import *
from time import *


def suma():
    global num
    k = 1
    """If we want use this, we need set flag before running flow"""
    while myevent.is_set():
        num += k**2
        k += 1
        print(num)
        print(current_thread().name)
        sleep(0.3)


num = 0
myevent = Event()
t = Thread(target=suma)
"""SET flag"""
myevent.set()
"""Start thread"""
t.start()
sleep(2)
myevent.clear()


