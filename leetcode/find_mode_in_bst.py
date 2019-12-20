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
    mode = 0
    value = node.value if node else None
    if not node:
        return mode, value

    mode, value = find_mode(node.left)

    if mode > best_mode:
        best_mode = mode
        best_value = value

    find_mode(node.right)

    if node.left and node.left.value == node.value:
        mode += 1
    else:
        mode = 1

    return mode, node.value


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
