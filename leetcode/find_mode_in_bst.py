class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

'''
           4
          / \
         2   5
        / \   \
       2   3   6
      /   /
     2   3
    /
   1
'''


best_mode = 0
best_value = 0

def find_mode(node):
    global best_mode
    global best_value
    if not node:
        return 0, None

    left_mode, left_value = find_mode(node.left)

    if left_mode > best_mode:
        best_mode = left_mode
        best_value = left_value

    find_mode(node.right)

    if node.left and node.left.value == node.value:
        return left_mode + 1, node.value
    else:
        return 1, node.value


root = Node(4)
root.right = Node(5)
root.right.right = Node(6)
root.left = Node(2)
root.left.left = Node(2)
root.left.left.left = Node(2)
root.left.left.left.left = Node(1)
root.left.right = Node(3)
root.left.right.left = Node(3)
# root.left.right.left.left = Node(3)

# LSR: 5, 10, 30, 40, 40, 40, 40, 60
# [5, 10, 30, 40, 40, 40, 40, 60]


#                      30
#                 10                            60
#             5                            40
#                                     40
#                                40
#                           40




find_mode(root)
print("value:", best_value)
print("mode", best_mode)

# in_order(root)
