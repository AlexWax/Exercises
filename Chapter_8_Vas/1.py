class FieldClass:
    def __init__(self, a: any, b: any):
        self.field_1 = a
        self.field_2 = b

    def show(self):
        for name in self.__dict__:
            if name != 'name':
                print(self.__dict__[name])


A = FieldClass('text', 4)
B = FieldClass(123, [1, 2, 3])
A.show()
B.show()
FieldClass.show(FieldClass(1, 2))