from random import *


class NumList:
    def __init__(self, max_num: int):
        self.num_list = [randint(1, randint(1, max_num)) for i in range(randint(0, max_num))]


def list_search(some_object: object) -> list:
    for name, value in some_object.__dict__.items():
        if type(value) == list:
            return [name, value]


def list_adj(object_1: object, object_2: object) -> object:

    class NewObject:
        def __init__(self, obj1, obj2):
            [name, value1] = list_search(obj1)
            _, value2 = list_search(obj2)
            if len(value2) > len(value1):
                value1.extend([0 for i in range(len(value2)- len(value1))])
            else:
                value2.extend([0 for i in range(len(value1) - len(value2))])

            self.__dict__[name] = [value1[i] + value2[i] for i in range(len(value1))]

    return NewObject(object_1, object_2)


A = NumList(10)
B = NumList(5)
print(A.__dict__, B.__dict__, sep='\n')

C = list_adj(A, B)
print(C.__dict__)
