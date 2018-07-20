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

    def exists(self, data):
        if self.data is None:
            return False
        if self.data == data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.exists(data)
        elif data > self.data:
            if self.right:
                return self.right.exists(data)
            else:
                return False



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
num1 = 10
num2 = 14

# print(lca(root, num1, num2).data)
print(root.exists(10))
print(root.exists(123))
