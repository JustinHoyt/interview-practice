'''
Created on Oct 31, 2016

@author: justinhoyt
'''

def reverse_string(str):
    letters = list(str)
    for index in range(int(len(letters) / 2)):
        letters[index], letters[-index - 1] = letters[-index - 1], letters[index]  
    return ''.join(letters)

print(reverse_string("hello world"));