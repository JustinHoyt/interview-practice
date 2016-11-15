'''
Created on Nov 13, 2016

@author: justinhoyt
'''
from random import randrange
def shuffle(list):
    for index in range(len(list)):
        rand_index = randrange(index, len(list))
        list[index], list[rand_index] = list[rand_index], list[index]
    return list


print(shuffle(list(range(10))))