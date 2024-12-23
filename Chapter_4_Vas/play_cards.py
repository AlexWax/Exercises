import random


def deck(suit, min_num, max_num, suit_num_order, add_let_to_num=True,  shuffle=True):
    num = {i for i in range(min_num, max_num)}
    if add_let_to_num: num.update({'J', 'Q', 'K', 'A'})

    deckk = []

    for suits in suit:
        for nums in num:
            if suit_num_order == 'ns':
                deckk.append(str(nums) + suits)
            elif suit_num_order == 'sn':
                deckk.append(suits + str(nums))

    if shuffle:
        len_deck = len(deckk)
        newdeck = []
        while len(newdeck) < len_deck:
            rand = random.randint(0, len(deckk) - 1)
            newdeck.append(deckk[rand])
            deckk.remove(deckk[rand])
        return newdeck

    else: return deckk

def draw(num_players, num_cards):
    suit = {'s', 'd', 'c', 'h'}
    deckk = deck(suit, 2, 14, suit_num_order='ns', shuffle=True)
    need_card = num_cards*num_players
    if need_card > len(deckk):
        return print('Not enough cards')

    hand = [[0 for j in range(num_cards)] for i in range(num_players)]
    for i in range(num_cards):
        for j in range(num_players):
            hand[j][i] = deckk.pop(random.randint(0, need_card))

    for i in range(num_players):
        print(hand[:][i])

    return deckk
