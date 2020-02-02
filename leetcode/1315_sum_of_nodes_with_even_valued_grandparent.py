class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_even_valued_grandparents(node):
    def sum_rec(node, parent=None, grandparent=None):
        if node is None:
            return 0

        curr_val = 0
        if grandparent and grandparent.value % 2 == 0:
            curr_val = node.value

        return (curr_val
                + sum_rec(node.left, node, parent)
                + sum_rec(node.right, node, parent))

    return sum_rec(node)

root = Node(6)
root.left = Node(7)
root.left.left = Node(2)
root.left.left.left = Node(9)
root.left.right = Node(7)
root.left.right.left = Node(1)
root.left.right.right = Node(4)
root.right = Node(8)
root.right.left = Node(1)
root.right.right = Node(3)
root.right.right.right = Node(5)

print(sum_of_even_valued_grandparents(root))
