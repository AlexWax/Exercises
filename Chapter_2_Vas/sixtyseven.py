import numpy as np

try:
    def triangle(num1, num2, num3):
        print('Yes') if num1+num2 > num3 and num1+num3 > num2 and num2+num3 > num1 else print('No')

    def consequence(num1, num2, num3):
        print('Yes') if num1-num2 == num2-num3 or num3-num1 == num2-num3 or num1-num2 > num3-num1 else print('No')

    def maxi(num1, num2):
        listt = [num1, num2]
        print(max(listt))

    if __name__ == "__main__":
        Num1 = int(input("Input number: "))
        Num2 = int(input('Input second number: '))
        Num3 = int(input('Input third number: '))

        triangle(Num3,Num2,Num1)

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