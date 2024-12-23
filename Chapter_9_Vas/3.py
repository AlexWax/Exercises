from random import *

class ListAdd:
    def __init__(self, list_len: int):
        self.lst_len = list_len
        self.lst = [randint(0, 10) for i in range(list_len)]

    def __add__(self, obj: object) -> object:
        if obj.lst == None:
            list_len = self.lst_len
        else:
            list_len = self.lst_len + obj.lst_len
        return ListAdd(list_len)

    def show(self):
        print(self.lst)


A = ListAdd(10)
A.show()
B = ListAdd(5)
B.show()
C = A + B
C.show()