class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


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
root.insert(8)
root.insert(22)
root.insert(4)
root.insert(12)
root.insert(10)
root.insert(14)
n1 = 10
n2 = 14

print(lca(root, n1, n2).data)
