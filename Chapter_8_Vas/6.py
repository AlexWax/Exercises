def class_list(num: int, some_object: object) -> list[object]:

    return [some_object(2*n + 1) for n in range(num)]

class SomeClass:
    def __init__(self, numer):
        self.intt = numer


print(class_list(4, SomeClass)[1].intt)