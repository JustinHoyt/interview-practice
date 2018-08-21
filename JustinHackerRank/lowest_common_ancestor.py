class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)


    def lca(self, v1, v2):
        right = max(v1, v2)
        left = min(v1, v2)
        if self.value <= right and self.value >= left:
            print("found it")
            return self.value
        elif self.value < left:
            print("going right")
            if self.right is not None:
                return self.right.lca(v1, v2)
        elif self.value > right:
            print("going left")
            if self.left is not None:
                return self.left.lca(v1, v2)


    def find(self, value):
        if self.value == value:
            return True
        if value < self.value:
            print("here")
            if self.left is not None:
                return self.left.find(value)
            else:
                return False
        if value > self.value:
            print("here")
            if self.right is not None:
                return self.right.find(value)
            else:
                return False


root = Node(4)
root.insert(2)
root.insert(7)
root.insert(1)
root.insert(3)
root.insert(6)

print(root.lca(2, 7))
print(root.find(6))
