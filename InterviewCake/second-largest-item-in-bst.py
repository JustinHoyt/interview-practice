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

# peworder till i hit a leaf node
# pre: SRL -> [10, 16, 20, 17, 18]

def second_largest_element(root, high = float('-inf'), second_high = float('-inf')):
    # go until leaf node, then return second highest
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        if node.value > high:
            second_high = high
            high = node.value
        elif node.value > second_high:
            second_high = node.value
        if node.right is None and node.left is None:
            return second_high

def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.value, end=" ")
    print_tree(root.right)

tree = BinaryTreeNode(10)
tree.insert_left(5)
tree.insert_right(16)
tree.right.insert_right(20)
tree.right.right.insert_left(17)
tree.right.right.left.insert_right(18)

print_tree(tree)
print()
print(second_largest_element(tree))