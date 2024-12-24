class Num:
    """Num of class appearance"""
    num = 0

    def __init__(self):
        Num.num += 1


class Prop:
    def __init__(self):
        self.__mama_name = 'Mama'

    def name(self):
        return self.__mama_name


Num()
print(Num().num)

print(Prop().name)
print(Prop()._Prop__mama_name)