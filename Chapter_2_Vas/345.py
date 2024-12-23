import numpy as np

try:

    List1 = eval(input("Input number: "))
    List2 = eval(input('Input second list: '))
    MaxNum = int(input('Max number for sum: '))


    def CompList(List1, List2):
        print('Match!') if len(List1) == len(List2) and List1 == List2 else print('Not match!')


    def sumlist(listt,max_num):
        summ = 0
        for i in range(max_num):
            if i not in listt:
                summ += i
        print(summ)


    CompList(List1,List2)
    sumlist(List1, MaxNum)
    sumlist(List2, MaxNum)
except ValueError:
    print("ValueError: valuation problem")
except ZeroDivisionError:
    print("ZeroDivisionError:")
except TypeError:
    print("TypeError: incorrect operation")
except IndexError:
    print("IndexError: wrong element index")
except SyntaxError:
    print("SyntaxError: unable to calculate")
except NameError:
    print("NameError: incorrect identify index")