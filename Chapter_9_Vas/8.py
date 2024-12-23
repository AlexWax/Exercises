class PolSum:
    def __init__(self, lst: list):
        self.lst = lst

    def __call__(self, args: int):
        sum_out = 0
        for i, elem in enumerate(self.lst):
            sum_out += elem*args**i
        return sum_out


A = PolSum([1, 2, 3])
print(A(4))