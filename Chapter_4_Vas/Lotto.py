import random

from Study.Chapter_4_Vas.play_cards import deck


def lotto():
    let = ['L', 'O', 'T', 't', 'o']
    c = [[random.randint(1+i*15, 15+i*15) if random.choice([True, False]) else '' for j in range(5)] for i in range(len(let))]
    lotr = dict(zip(let,c))
    return lotr


def show_lotto(lotr):
    for key in lotr.keys():
        print(key, end='\t')
    print('\n')
    for i in range(5):
        for value in lotr.values():
            print(value[i], end='\t')
        print('\n')
    return


def play_lotto(lotr, num):
    num_let, num_val = num[0], num[1:]
    for key, value in lotr.items():
        if num_let == str(key) and int(num_val) in value:
            lotr[str(key)][value.index(int(num_val))] = '*'

    c = [value for value in lotr.values()]

    zero_count = [0 for o in range(2+len(c)+len(c[0]))]

    for i in range(len(c)):
        for j in range(len(c[i])):
            if type(c[i][j]) == int:
                zero_count[i] += c[i][j]
                zero_count[j+len(c)] += c[i][j]
                if i == j: zero_count[0+len(c)+len(c[0])] += c[i][j]
                if i + j == len(c) - 1: zero_count[1+len(c)+len(c[0])] += c[i][j]

    if 0 in zero_count:
        return True


if __name__ == '__main__':

    miditr = 0
    for i in range(1000):

        if i%10 == 0:
            #print(f"*{'-'*18}*")
            print(f"|{'>'*(i//100): <9} {(i+10)/10:3.1f}% {'<'*(i//100): >9}|")
            #print(f"*{'-'*18}*")

        lotto_nums = deck(suit=['L', 'O', 'T', 't', 'o'], min_num=1, max_num=75, suit_num_order='sn',
                          add_let_to_num=False, shuffle=True)
        lotto_card = lotto()

        for itr, num in enumerate(lotto_nums):
            stop_flag = play_lotto(lotto_card,num)
            if stop_flag:
                #print(f'Stop iter: {itr}')
                miditr += itr / 1000
                #show_lotto(lotto_card)
                break

    #print("%4.2f" % miditr)