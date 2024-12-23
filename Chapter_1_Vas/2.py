# How old are you?

day = int(input("What`s day? "))
month = int(input("What`s month? "))
year = int(input("What`s year? "))
B_day = int(input("What`s day when you was born? "))
B_month = int(input("What`s month when you was born? "))
B_year = int(input("What`s year when you was born? "))

MonthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
# Month_Length = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', 31]
Month_Length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def Age(year, month, day, B_year, B_month, B_day):
    if (B_month > month) or ((B_month == month) and (B_day > day)):
        Y_Year = year - B_year - 1
    else:
        Y_Year = year - B_year

    if B_day > day:
        Y_Month = (12 - B_month + month - 1) % 12
    else:
        Y_Month = (12 - B_month + month) % 12

    Y_Day = (Month_Length[month - 2] - B_day + day) % Month_Length[month - 2]

    return Y_Year, Y_Month, Y_Day


def LastForB(month, day, B_month, B_day):
    if B_day < day:
        Y_Month = (12 - month + B_month - 1) % 12
    else:
        Y_Month = (12 - month + B_month) % 12

    Y_Day = (Month_Length[month - 1] - day + B_day) % Month_Length[month - 1]

    return Y_Month, Y_Day


print("Your are", Age(year, month, day, B_year, B_month, B_day)[0], "years, ",
      Age(year, month, day, B_year, B_month, B_day)[1], "month, ",
      Age(year, month, day, B_year, B_month, B_day)[2], "days old")

print("For your birthday", LastForB(month, day, B_month, B_day)[0], "month and ",
      LastForB(month, day, B_month, B_day)[1], "days")
