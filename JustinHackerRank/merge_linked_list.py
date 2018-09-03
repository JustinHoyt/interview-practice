'''
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_merge(first, second):
    temp_first = first
    temp_second = second
    while temp_first:
        while temp_second:
            if temp_first is temp_second:
                return temp_first.value
            temp_second = temp_second.next
        temp_second = second
        temp_first = temp_first.next
    return -1


first = Node(3)
first.next = Node(4)
first.next.next = Node(5)
second = Node(1)
second.next = first.next.next
print(find_merge(first, second))
