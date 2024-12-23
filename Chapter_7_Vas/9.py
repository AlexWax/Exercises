import sys

with open("C:\\Users\\Админ\\Documents\\Python\\Projects\\Study\\Chapter_7_Vas\\text.txt", 'rt') as a:

    path = "C:\\Users\\Админ\\Documents\\Python\\Projects\\Study\\Chapter_7_Vas\\Alise was"
    with open(path, 'wt') as b:
        text = a.read().replace('\n', ' ').split()
        length = 0
        for word in text:
            length += len(word) + 1
            if length > 50:
                b.write('\n')
                length = len(word) + 1
            b.write(word + ' ')

