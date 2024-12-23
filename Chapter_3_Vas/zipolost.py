import random

def zip_list():
    list1 = [random.randint(0,9) for i in range(10)]
    list2 = [random.randint(0, 9) for i in range(10)]
    print(list2, list1)
    zipolist = []

    for i in range(len(list1)):
        zipolist.append(list2[i])
        zipolist.append(list1[i])

    return zipolist


if __name__ == "__main__":
    print(zip_list())