def char() -> list:
    """Create a list of str following each other in ACSII-table.
    We did it to get letters for converting in systems > 10"""
    val = 'A'
    list_of_lat = ['' for i in range(58)]

    for j in range(58):
        list_of_lat[j] = val
        val = chr(ord(val)+1)   # ord - conv. to ascii; chr - opposite

    return list_of_lat


class NumSysConverter:
    """Convert any number from any_in to any_out"""
    def __init__(self, num_sys_in: int, num_sys_out: int, number: any):
        self.num_sys_in = num_sys_in
        self.num_sys_out = num_sys_out
        self.number = number

        self.chars = char()

        number_in_dec = self.system_change_2dec(num_sys_in, number)
        self.new_number = self.system_change_dec2(num_sys_out, number_in_dec)

    def system_change_2dec(self, num_sys: int, number: int) -> int:
        """convert any number from any to dec"""
        sam = 0
        number = list(reversed(str(number)))    # We opposite _num
        for i, num in enumerate(number):
            if num in self.chars:  # for letters mean nums > 10
                num = 10 + number.index(num)

            sam += int(num)*num_sys**i  # Multiply to correct _num = _num of system ^ digit
        return sam

    def system_change_dec2(self, num_conv: int, number: int) -> list[str]:
        """convert any number from dec to any"""
        strs = ''
        while number//num_conv >= 1:
            deriv = number % num_conv
            if deriv//10 >= 1 and deriv%10 >= 0:    # for letters mean nums > 10
                deriv = self.chars[deriv - 10]

            strs += str(deriv)  # Divide _num and remember remains
            number = number//num_conv

        if number//10 >= 1 and number%10 >= 0:  # for letters mean nums > 10
            number = self.chars[number - 10]
        return list(reversed(strs + str(number)))

    def __str__(self) -> str:
        str_out = ''
        for elem in self.new_number:
            str_out += str(elem)
        return str_out


if __name__ == '__main__':
    print(NumSysConverter(10, 2, 0))
