"""def sum() -> int:
    '''№1'''
    a = input()
    if not a.isnumeric():
        return suum
    return suum + int(a) + sum()

global suum
suum = 0
print(sum())"""


def evklid(num1: int, num2: int) -> int:
    """The largest common divider or not"""
    if num1 == 0:
        return num2
    else:
        return evklid(num2 % num1, num2)


def been(num: int) -> str:
    """Convert num to bin(num)"""
    global bin_num_rev
    if num in [0, 1]:
        bin_num_rev += str(num)
    else:
        bin_num_rev += str(num%2)
        return been(num//2)


def romula_numbers(num: str) -> int:
    """Convert romula numbers to humans"""
    global human_num
    global dict_romula
    dict_romula = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(num) == 1:
        human_num += dict_romula[num[0]]
        return 0
    if dict_romula[num[0]] < dict_romula[num[1]]:
        human_num -= dict_romula[num[0]]
    else: human_num += dict_romula[num[0]]

    return romula_numbers(num[1:])


def polindrom(num: str) -> bool:
    """Polindrom check"""
    if num == '':
        return True
    if num[0] == num[-1]:
        return polindrom(num[1:-1])
    else:
        return False


def sqrt(num: int, guess: float = 1) -> float:
    """Sqrt"""
    if abs(guess**2-num) < 1e-10:
        return guess
    else:
        guess += num/guess
        return sqrt(num, guess/2)


def money(num: int, max_num) -> bool:
    """Money money moneeey"""
    global a
    if a > max_num:
        return False
    if num == 0 and a <= max_num:
        print(a)
        return True
    for i in [10, 5, 1]:
        if num - i >= 0:
            a += 1
            return money(num-i, max_num)


def list_eq(lst: list, b: list = []) -> list:
    """Дist alignment"""
    if lst != []:
        if type(lst[0]) == int:
            b.append(lst[0])
            return list_eq(lst[1:], b)

        list_eq(lst[0], b)
        return list_eq(lst[1:], b)
    else:
        return b


def decod(lst: list) -> list:
    global new_lst
    global count
    if len(lst) == 1:
        new_lst.extend([lst[0], count])
        return new_lst
    if lst[0] == lst[1]:
        count += 1
    else:
        new_lst.extend([lst[0], count])
        count = 1
    return decod(lst[1:])


count = 1
new_lst = []
print(decod(["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A",
             "A", "B"]))
