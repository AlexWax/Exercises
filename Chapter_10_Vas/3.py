import numpy as np
def eq_solve(A: any, B: any) -> str:
    try:
        x = np.sin(A)/(A*(A-1))
    except ZeroDivisionError:
        x = 'ZeroDev'
    except TypeError:
        x = 'Non cor type'
    return str(x)


print(eq_solve(15, 'text'))