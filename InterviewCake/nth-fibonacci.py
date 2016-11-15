'''
Created on Nov 12, 2016

@author: justinhoyt
'''

def nth_fibonacci(n):
    prev = 1
    prev_prev = 0
    current = 1
    for _ in range(n):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    return current

for i in range(10):
    print(nth_fibonacci(i))