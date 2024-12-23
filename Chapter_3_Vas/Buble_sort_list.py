import random
def buble_sort_list():

    lis = [random.randint(0, 9) for i in range(10)]
    print(lis)

    for k in range(len(lis)//2):
        for i in range(len(lis)-1)[1::2]:
            if lis[i] > lis[i+2]:
                lis[i], lis[i+2] = lis[i+2], lis[i]
        for i in range(len(lis)-2)[::2]:
            if lis[i] < lis[i + 2]:
                lis[i], lis[i + 2] = lis[i + 2], lis[i]

    return lis


if __name__ == "__main__":
    #lis = list(eval(input('List: ')))
    print(buble_sort_list(), sep='\n', end='\n')

