import collections
from random import randint

# I/O
# file = open("file.txt", mode="w")
sets = []
with open('file.txt', 'w') as file:
    file.write("[")
    for i in range(500):
        tempset = set()
        for j in range(500):
            tempset.add(randint(0, 100000))
        file.write("%s,\n" % tempset)
    file.write("]")
        # sets.append(tempset)
    # print(sets)

test_val = 5
print("my value =", test_val)
print()


# trees
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)

def is_bst_rec(curr, prev):
    if curr:
        if is_bst_rec(curr.left, prev) is False:
            return False
        if prev and prev.value >= curr.value:
            return False
        return is_bst_rec(curr.right, curr)
    else:
        return True

def is_bst(root):
    prev = None
    return is_bst_rec(root, prev)

root = TreeNode(25)
root.insert(10)
root.insert(15)
root.insert(13)
root.insert(30)
root.insert(90)
print(root.left.right.value)
print(root.right.value)
print(is_bst(root))
print()


# Linked List
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        temp = self
        while temp.next:
            temp = temp.next
        temp.next = LinkedListNode(value)


linked_list = LinkedListNode(14)
linked_list.insert(15)
linked_list.insert(16)
linked_list.insert(17)
linked_list.insert(18)
print(linked_list.next.next.value)
print()


# Stacks & Queues
stack = collections.deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print("--Stack--")
print(stack)
stack.pop()
stack.pop()
print(stack)

queue = collections.deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print("--Queue--")
print(queue)
queue.popleft()
queue.popleft()
print(queue)
