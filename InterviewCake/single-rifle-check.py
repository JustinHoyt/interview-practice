'''
Created on Nov 13, 2016

@author: justinhoyt
'''

# find if the deck is only halved
def is_single_riffle(shuffled_deck, half1, half2):
    #walk through shuffled deck and compare with half1 until changes
    for card in shuffled_deck:
        if len(half1) != 0 and len(half2) != 0:
            if card == half1[0]:
                del(half1[0])
            elif card == half2[0]:
                del(half2[0])
            else:
                return False
        elif len(half1) != 0:
            if card == half1[0]:
                del(half1[0])
            else:
                return False
        elif len(half2) != 0:
            if card == half2[0]:
                del(half2[0])
            else:
                return False
    return True


shuffled_deck = [0,1,2,3,4,5,6,7,8,9,10]
half1 = [0,1,2,3,4]
half2 = [5,6,7,8,9,10]

print(is_single_riffle(shuffled_deck, half1, half2))