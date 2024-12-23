from random import *


class ListComparing:
    def __init__(self, list_len: int):
        self.list_len = list_len
        self.lst = [randint(0,10) for i in range(list_len)]

    def compare(self, self_list, other_list: list) -> (list, list):
        other_list.extend([0 for i in range(len(self_list) - len(other_list))]) if len(self_list) > len(other_list) \
            else other_list.extend([0 for i in range(len(other_list) - len(self_list))])
        return self_list, other_list

    def __eq__(self, other):
        list1, list2 = self.compare(self.lst, other.lst)
        return list1[0] == list2[0]
    def __lt__(self, other):
        list1, list2 = self.compare(self.lst, other.lst)
        return list1[1] > list2[1]
    def __gt__(self, other):
        list1, list2 = self.compare(self.lst, other.lst)
        return list1[2] < list2[2]
    def show(self):
        print(self.lst)

A = ListComparing(3)
A.show()
B = ListComparing(3)
B.show()

print(A > B)