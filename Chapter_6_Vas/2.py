
def now_generator(ldt: list) -> int:
    """№2"""
    for i in ldt:
        if i%2 == 1:
            yield i


def trvr(txt: str, *args: int) -> str:
    """№4"""
    stor = ''
    for i in args:
        stor += txt[i]
    return stor


def max_val(f: "function", min_r: int, max_r: int) -> (int, int):
    """№5"""
    a = []
    for val in range(min_r, max_r+1):
        a.append(f(val))
    return max(a), a.index(max(a))


def text(txt: str) -> str:
    """№7"""
    if len(txt) == 0:
        raise SystemExit
    print(txt[0])
    return text(txt[2:])

def sump(mlp: int, num: int) -> int:
    """№8"""
    global a
    if num == 1:
        return 1
    return a + sump(mlp, num-1)*mlp


def generator(num: int) -> (int, str):
    """№9, 10"""
    for i in range(num):
        yield 2**i
    for month in ['J', 'f', 'm']:
        yield month


a = 1
print(list(generator(5)))
print(sump(2, 4))
print(a)
print(text('mama mila'))


lst_odd = now_generator([i for i in range(10)])

print(list(lst_odd))
print(trvr('abracadabra', 1, 2, 3, 4))
print(max_val(lambda x: x**2 - x + 1, -4, 0))