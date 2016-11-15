'''
Created on Nov 3, 2016

@author: justinhoyt
'''

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None
        
    def insert(head, data):
        if head is None:
            head = Node(data)
        else:
            current = head
            while current.next:
                current = current.next
            current.next = LinkedListNode(data)
    
    def print_linked_list(self):
        current = self
        while current:
            print(current.value, end=" ")
            if current:
                current = current.next
            else:
                break
        print()
        
def reverse_linked_list(current):
    previous = None
    next = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
        
    return previous
        
        


list = LinkedListNode(0)
for i in range(1, 4):
    list.insert(i)

list.print_linked_list()
list2 = reverse_linked_list(list)
list2.print_linked_list()
