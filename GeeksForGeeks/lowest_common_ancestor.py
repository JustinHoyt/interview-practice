class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(node, n1, n2):
    if node is None:
        return None
    print(node.data)
    if n1 < node.data and n2 < node.data:
        return lca(node.left, n1, n2)
    elif n1 > node.data and n2 > node.data:
        return lca(node.right, n1, n2)
    return node


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
n1 = 10
n2 = 14

print(lca(root, n1, n2).data)
