class IndexSum:
    def __init__(self, list1: list, list2: list):
        self.list_1, self.list_2 = self.list_equal(list1, list2)

    def __getitem__(self, index):
        if index <= len(self.list_1)-1:
            if type(self.list_1[index]) == type(self.list_2[index]):
                out_value = self.list_1[index] + self.list_2[index]
            else:
                out_value = self.list_1[index]*self.list_2[index]
        else:
            out_value = None
        return out_value

    def list_equal(self, lst1, lst2):
        lst1.extend([0 for i in range(len(lst2) - len(lst1))]) if len(lst2) > len(lst1) \
            else lst2.extend([0 for i in range(len(lst1) - len(lst2))])
        return lst1, lst2


A = IndexSum([1, 2, 3], [1, 'b', 4])
print(A[0])
