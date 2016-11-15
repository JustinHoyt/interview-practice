'''
Created on Nov 14, 2016

@author: justinhoyt
'''

from random import randrange

def rand5():
    return randrange(1,6)


def rand7():
    while True:
        random = (rand5() - 1) * 5 + (rand5() - 1) + 1
        if random < 22:
            return random % 7 + 1

mydict = {}

for _ in range(1000000):
    rand = rand7()
    if rand in mydict:
        mydict[rand] += 1
    else:
        mydict[rand] = 1

for key in mydict.keys():
    print(str(key) +  ": " + str(mydict[key]))