a = """maMa Hello Worldmila * ramu""".lower()
newtext = ''
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
last_chr = ord('z')
prelast_chr = ord('y')
first_chr = ord('a')
second_chr = ord('b')

for let in a:
    if ord(let) == ord(' '):
        newtext += let
    if let in vowel:
        if ord(let) == ord(vowel[-1]):
            newtext += vowel[1]
        else:
            newtext += vowel[vowel.index(let)+1]
    else:
        newtext += let


print(newtext, sep='\n')