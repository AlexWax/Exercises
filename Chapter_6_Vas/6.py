def rec(f, n: int, b):
    """№6 Return f(f(...) n times """
    global count
    if n == 0:
        return f
    else:
        count += 1
        print(count)
        return lambda x: f(rec(f, n-1, b))



count = 0
b = rec(lambda x: x**2, 3, 3)
print(b(x=2))
print(count)