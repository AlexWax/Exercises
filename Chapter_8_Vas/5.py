def class_conv(some_object: object) -> object:
    """..."""
    class NewClass:
        def __init__(self, som_object: object):
            for name, value in som_object.__class__.__dict__.items():
                if not name.startswith('_') and type(value) == int:
                    self.__dict__[name] = value

    return NewClass(some_object)


class SomeClass:
    a = 4


A = class_conv(SomeClass())
print(A.__dict__)