class Iter:
    def __init__(self, max_num: int):
        self.max_number = max_num
        lst = []
        for j in range(self.max_number-2):
            lst.append(self.fibo(j))
        self.list_out = lst
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.position < self.max_number-2:
            return self.list_out[self.position]
        else:
            raise StopIteration

    def fibo(self, num: int) -> int:
        global cash
        cash = {0: 1, 1: 1}
        if num not in cash:
            cash[num] = self.fibo(num - 1) + self.fibo(num - 2)
        return cash[num]



A = Iter(20)
try:
    while True:
        print(next(A))
except BaseException as error:
    print(error.__doc__)
    print('Please stop')
A.position = 1
try:
    while True:
        print(next(A))
except StopIteration:
    print('Please stop')
