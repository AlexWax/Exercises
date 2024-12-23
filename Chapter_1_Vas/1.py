# What`s day today

day = input("What`s day? ")
month = input("What`s month? ")
# B_day = input("What`s day when you was born? ")
# B_month = int(input("What`s month when you was born? "))

MonthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']


def NinM(n):
    Flag_int = 0
    Flag_str = ''
    for k in range(len(MonthList)+1):
        if MonthList[k - 1] == n:
            Flag_int = k
            return Flag_int
        if str(k) == n:
            Flag_str = MonthList[eval(n) - 1]
            return Flag_str


print('Today: ', day, NinM(month))

