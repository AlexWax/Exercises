class MyError(Exception):
    def __init__(self):
        self.list_out = []

    def __add__(self, other):
        self.list_out.append(other)
        return self


def recurs_error(num: int):
    try:
        if num <= 1:
            raise MyError
        recurs_error(num - 1)
    except MyError as error:
        raise error+num


def error_list(num: int):
    try:
        recurs_error(num)
    except MyError as error:
        return error.list_out


A = error_list(10)
print(A)