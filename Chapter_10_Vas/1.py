def summa(*args: any) -> int:
    suma = 0
    for arg in args:
        try:
            if type(arg) == int:
                suma += arg
            else:
                raise ValueError
        except (ValueError, TypeError):
            print('We skip:', arg)
            continue
    return suma


def border(bord_min: any, bord_max: any) -> list:
    try:
        if type(bord_min) == int and type(bord_max) == int:
            if bord_min > bord_max:
                error_2 = Exception('Wrong order')
                raise error_2
            lst = []
            [lst.append(i) for i in range(bord_min, bord_max+1)]
            return lst
        else:
            error = ValueError('Bord nums must be integer')
            raise error
    except ValueError:
        return error
    except Exception:
        print(error_2)
        print('We change order')
        return border(bord_max, bord_min)


print(summa(1, 'b', 2, [1, 2, 3], 1.5))
print(border(1, -1))