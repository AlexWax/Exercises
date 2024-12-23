class F:
    def __init__(self, num: int, strip: str, fl: float):
        self.number = num
        self.strip = strip
        self.flt = fl

    def __int__(self):
        return self.number + 1
    def __float__(self):
        return self.flt * 10
    def __str__(self):
        return self.strip + "_Ogo"


print(F(10, 'Go', 1.0))
print(float(F(10, 'Go', 1.0)))
print(int(F(10, 'Go', 1.0)) - 1)