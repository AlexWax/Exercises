class Name1:
    number = 10
    def __init__(self, num: int):
        pass
    def show(self):
        print(self.number)


class Name2(Name1):
    def __init__(self, lst: list, num):
        super().__init__(num)
        self.lst = lst
    def sum(self, lst: list):
        self.summ = lst[0] + lst[1]
        return self.summ


class Name3(Name2):
    def __init__(self, lst: list, num: int, stri: str):
        super().__init__(num = self.sum(lst), lst=super().sum(lst))
        self.stri = stri
        self.number = self.number + num
    def show(self):
        super().show()
        print(self.stri)
        print(self.number)


A = Name1(10)
A.show()
B = Name2([1, 2], 2)
B.show()
C = Name3([1, 2, 3], 3, 'C')
C.show()

for clas in Name3.__mro__:
    print(clas.__name__)
