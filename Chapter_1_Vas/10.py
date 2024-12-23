# Odd sum

ListN = list(eval(input("Type your list: ")))  # Use comma to make a list
Number = int(input("Input number of odd values: "))


def OddSum(ListN, Number):

    Sum = 0
    k = 0

    for num in ListN:
        if num % 2 == 1 and k < Number:
            k += 1
            Sum += num

    return Sum


print(OddSum(ListN, Number))
