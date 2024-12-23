def generator(lst1: list, lst2: list):
    """Return list elements"""
    j = 0
    a = []
    for i in range(len(lst1)):
        if i == j:
            j -= len(lst2)
        a.append(lst1[i] * lst2[j])
        j += 1
    return a


def list_mlp(list1: list, list2: list) -> list:
    """Make list of list1[i]*list2[i]"""

    if list1 >= list2:
        return generator(list1, list2)
    if list2 > list1:
        return generator(list2, list1)


list1, list2 = [1, 2, 4], [2, 3, 4, 5]
print(list_mlp(list1, list2))
