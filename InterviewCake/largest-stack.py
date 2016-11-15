'''
Created on Nov 15, 2016

@author: justinhoyt
'''
import queue
class Max_Stack:
    def __init__(self):
        self.max_stack = []
        self.stack = []

    def insert(self, num):
        if len(self.stack) == 0:
            self.max_stack.append(num)
        elif num >= self.max_stack[-1]:
            self.max_stack.append(num)
        self.stack.append(num)            
        
    def get_max(self):
        try:
            return self.max_stack[-1]
        except IndexError:
            print("nothing to get!")

    def pop(self):
        try:
            if self.stack[-1] == self.max_stack[-1]:
                self.stack.pop()
                self.max_stack.pop()
            else:
                self.stack.pop()
        except IndexError:
            print("index error!")
            
stack = Max_Stack()

stack.insert(5)
stack.insert(10)
stack.insert(11)
stack.insert(12)
stack.insert(6)

print(stack.get_max())

stack.pop()
stack.pop()
print(stack.get_max())

stack.pop()
print(stack.get_max())

stack.pop()
print(stack.get_max())

stack.pop()
print(stack.get_max())