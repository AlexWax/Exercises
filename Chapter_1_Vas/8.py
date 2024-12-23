# Fibonacci sequence

F_number = int(input("How much elements..?"))


def FibCal(F_number):
    Fibonacci3 = 0
    Fibonacci2 = 1
    Fibonacci1 = 1
    FibList = list(range(1, F_number + 1))

    for k in range(F_number - 1):
        Fibonacci1 = Fibonacci3
        Fibonacci3 = Fibonacci2
        Fibonacci2 = Fibonacci1 + Fibonacci3
        FibList[k+1] = Fibonacci2

    return FibList


print(FibCal(F_number))

def fib(n: int) -> int:
    global count
    global cash

    count += 1
    if n not in cash:
        cash[n] = fib(n - 1) + fib(n - 2)
    return cash[n]


cash = {0: 1, 1: 1}
count = 0
[print(fib(i), end='\t') for i in range(F_number)]
print('\n', count)
