# Create a list of str following each other in ACSII-table. We did it to get letters for converting in systems > 10
def char():
    val = 'A'
    list_of_lat = ['' for i in range(58)]

    for j in range(58):
        list_of_lat[j] = val
        val = chr(ord(val)+1) # ord - conv. to ascii; chr - opposite

    return list_of_lat


def system_change_2dec(num_sys, number):    # convert any number from any to dec
    sam = 0
    dev = char()

    number = list(reversed(str(number)))    # We opposite num
    for i, num in enumerate(number):
        if num in dev:  # for letters mean nums > 10
            num = 10 + number.index(num)

        sam += int(num)*num_sys**i  # Multiply to correct num = num of system ^ digit
    return sam


def system_change_dec2(num_conv, number):    # convert any number from dec to any
    strs = ''
    dev = char()
    while number//num_conv >= 1:
        deriv = number % num_conv
        if deriv//10 >= 1 and deriv%10 >= 0:    # for letters mean nums > 10
            deriv = dev[deriv - 10]

        strs += str(deriv)  # Divide num and remember remains
        number = number//num_conv

    if number//10 >= 1 and number%10 >= 0:  # for letters mean nums > 10
        number = dev[number - 10]
    return list(reversed(strs + str(number)))


def system_change(num_sys, num_conv,number):  # I dont now how realise direct conversion, so we use this buffer function
    number_in_dec = system_change_2dec(num_sys, number)
    new_number = system_change_dec2(num_conv, number_in_dec)
    return new_number


print(system_change(8, 10, 441))