'''
Created on Nov 12, 2016

@author: justinhoyt
'''
from copy import deepcopy
class test():
    def __init__(self):
        self.value1 = 1
        self.value2 = 2
        self.array = [1,2,3]

test = test()

test2 = deepcopy(test)

test2.array[0] = 13224

print(test.array)
print(test2.array)
