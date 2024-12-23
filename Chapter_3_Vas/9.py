import random

def long_list():

    lis = [random.randint(0,9) for i in range(10)]
    print(lis)
    lisk = lis[:]

    for i in range(1, len(lis)):
        lisk[i*2-1:i*2-1] = [lis[i] + lis[i-1]]

    return lisk


if __name__ == '__main__':
    print(long_list())
