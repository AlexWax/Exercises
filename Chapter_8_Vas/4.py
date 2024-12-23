def obj_creation(name: str, atr: list) -> object:
    new_list = []
    [new_list.append(elem) for i, elem in enumerate(atr) if type(elem) == str]

    class Name:
        def __init__(self, atr: list):
            for i, elem in enumerate(atr):
                print(elem, i)
                self.__dict__[elem] = i

    Name.__name__ = name
    return Name(new_list)


A = obj_creation('Mama', [1, 4, 5, int(2), 3, 'p', 'ap', [1, 2, 3], 'a', 1])
print(A.__class__.__dict__)