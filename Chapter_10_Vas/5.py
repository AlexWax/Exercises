class MyError(Exception):
    def __init__(self):
        self.value = []

    def __add__(self, other):
        self.value.append(chr(other+64))
        return self


def rec_er(num: int):
    try:
        if num <= 1:
            raise MyError
        rec_er(num-1)
    except MyError as error:
        raise error+num


def error_list(num: int):
    try:
        rec_er(num)
    except MyError as error:
        return error.value


A = error_list(17)
print(A)