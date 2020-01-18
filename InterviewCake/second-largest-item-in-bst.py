'''
Created on Nov 2, 2016

@author: justinhoyt
'''

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

#                 10
#         5               16
#     2       7       13            20
#                            17
#                                 18


def find_second_largest( head ):
    largest_parent, largest = find_largest(head)
    second_largest = None
    if largest.left:
        _, second_largest = find_largest(largest.left)
    else:
        second_largest = largest_parent

    return second_largest.value


def find_largest(head):
    current = head
    prev = None
    while current.right:
        prev = current
        current = current.right

    return prev, current

def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.value, end=" ")
    print_tree(root.right)

tree = BinaryTreeNode(200)
tree.left = BinaryTreeNode(100)
tree.left.right = BinaryTreeNode(150)
tree.left.right.right = BinaryTreeNode(170)
tree.left.left = BinaryTreeNode(90)
tree.left.left.left = BinaryTreeNode(80)
tree.left.left.left.left = BinaryTreeNode(70)

print_tree(tree)
print()
print(find_second_largest(tree))
