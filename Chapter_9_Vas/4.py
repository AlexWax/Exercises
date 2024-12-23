class Math:
    def __init__(self, field):
        self.field = field

    def __add__(self, obj: object):
        if type(obj.field) == str and type(self.field) == str:
            new_field = self.field + "+" + obj.field
        if type(obj.field) == int and type(self.field) == int:
            new_field = self.field - obj.field

        return Math(new_field)

    def __sub__(self, other: object):
        if type(other) == int:
            return Math(self.field - other)
        if type(other.field) == str and type(self.field) == str:
            new_field = [self.field.pop(elem) for elem in other.field if elem in self.field]
        if type(other.field) == int and type(self.field) == int:
            new_field = self.field/other.field

        return Math(new_field)

    def __rsub__(self, other: object):
        if type(other) == int:
            return other - self.field
        if type(other.field) == str and type(self.field) == str:
            new_field = [other.field.pop(elem) for elem in self.field if elem in other.field]
        if type(other.field) == int and type(self.field) == int:
            new_field = other.field + self.field

        return Math(new_field)

    def show(self):
        print(self.field)
        print(type(self.field))


A = Math(4)
A.show()
B = Math(5)
B.show()
C = B - A
C.show()
D = C - 1
D.show()
E = 1 - C
print(E, type(E))