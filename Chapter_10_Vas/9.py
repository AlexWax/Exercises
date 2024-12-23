from threading import *

def a(n: int, N: int):
    global lst_lst
    global k
    # mylock.acquire()
    print(current_thread().name)
    l = 1
    for j in range(N):
        l *= k+1
        lst_lst[n][j] = l
        k += 1
    # mylock.release()


def b(n: int, N: int):
    global lst_lst
    global k
    # mylock.acquire()
    print(current_thread().name)
    l = 1
    for j in range(N):
        l *= k+2
        lst_lst[n][j] = l
        k += 1
    # mylock.release()


def c(n: int, N: int):
    global lst_lst
    global k
    # mylock.acquire()
    print(current_thread().name)
    for j in range(N):
        lst_lst[n][j] = k
        k += 1
    # mylock.release()


mylock = Lock()
k = 0
lst_lst = [[1 for i in range(5)] for j in range(4)]
threads = [a, b, c]
t = [Thread(target=threads[i], args=[i, 5], name=str(threads[i])) for i in range(len(threads))]
print(lst_lst)
for thread in t:
    thread.start()
for thread in t:
    thread.join()
print(lst_lst)