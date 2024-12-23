class Int:
    def __init__(self, num):
        self.num = num

    def __add__(self, num):
        if type(num) == int:
            value = num + self.num
        else:
            value = self.num + num.num
        return Int(value)


A = Int(4)
B = Int(6)
print(B.num)
print(A + B)