# Maximum value

ListN = list(eval(input("Type your list: ")))  # Use comma to make a list
Number = int(input("Input number of max: "))


def MaxNum(ListN, Number):

    for k in range(Number - 1):
        Max = max(ListN)
        for i in range(len(ListN)):
            if ListN[i] == Max:
                ListN[i] = min(ListN)

    return max(ListN)


print(MaxNum(ListN, Number))
