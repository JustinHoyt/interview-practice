class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


best = 0

def find_mode(node):
    global best
    if not node:
        return 0
    so_far = find_mode(node.left)

    if node.left and node.left.value == node.value:
        return find_mode(node.right) + so_far + 1
    else:
        best = max(best, so_far)
        return find_mode(node.right) + 1


root = Node(30)
root.left = Node(10)
root.right = Node(60)
root.left.left = Node(5)
root.right.left = Node(40)
root.right.left.left = Node(40)
root.right.left.left.left = Node(40)
root.right.left.left.left.left = Node(40)

find_mode(root)
print(best)
