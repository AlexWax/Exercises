import random

def intersection_dict(text1, text2):
    num1 = set()
    num2 = set()
    while len(num1) < len(list(text1)):
        num1.add(random.randint(0,20))
    while len(num2) < len(list(text2)):
        num2.add(random.randint(0,20))

    dict1 = dict(zip(num1,text1))
    dict2 = dict(zip(num2,text2))
    print(dict1,dict2)

    set1 = set(num1)
    set2 = set(num2)
    int_set = set2.intersection(set1)

    int_dict = {}
    for key in int_set:
        int_dict.update({key:[dict1.get(key), dict2.get(key)]})

    return int_dict


dict1 = input('')
dict2 = input('')

print(intersection_dict(dict1, dict2))