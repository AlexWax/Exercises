import numpy as np

try:

    Value = list(input("Input number: "))

    def numnum(Value):
        n = np.zeros(10)
        for i in range(1,10):
            for num in Value:
                if num == str(i):
                    n[i] += 1
            print(f'There are: {int(n[i])} of', i)

    def AntuNum(Value):
        NewValue = ''
        for num in Value:
            num1 = 9 - int(num)
            NewValue += str(num1)
        return NewValue

    numnum(Value)
    print(AntuNum(Value))

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