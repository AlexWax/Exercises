import sys
import datetime

try:
    def convert(num_sys: str, num: int) -> int:
        """Convert _num to nym_sys system"""
        dic = {'0b': bin, '0o': oct, '0x': hex}
        return dic[num_sys](num)


    def byt(num: int, num_bit: int) -> int:
        """Return value of num_bit"""
        return int(bin(num)[num_bit+1])


    def byt_sum(num: int) -> int:
        """Return sum of bits"""
        return sum([int(let) for let in bin(num)[2:]])


    def oct_trans(num: int) -> int:
        a = ''
        for let in reversed(oct(num)[2:]):
            a += let
        return int(a, 8)

    def day_dif(day1, day2) -> int:
        return (day2 - day1).days

    def time_dif(time1, time2) -> int:
        return (time2 - time1)


    print(time_dif(datetime.datetime.now(), datetime.datetime(2025,1,1,0,0,0)))
    print(day_dif(datetime.date(2024,12,9), datetime.date(2025,1, 1)))
    print(sum([1 + 2j, 2 + 3j]))
    print(oct_trans(100))
    print(byt_sum(40))
    print(byt(40, 1))
    print(f"{convert('0b', 40):_<10}")

except:
    print('No system!')
