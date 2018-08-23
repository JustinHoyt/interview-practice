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


    def is_bst_rec(self, prev):
        if self is not None:
            if self.left is not None \
                    and self.left.is_bst_rec(prev) is False:
                return False
            if prev is not None \
                    and prev.value >= self.value:
                return False
            if self.right is not None:
                return self.right.is_bst_rec(self)
            else:
                return True
        else:
            return True


    def is_bst(self):
        prev = None
        return self.is_bst_rec(prev)


# def is_valid(current, parent):
#     if current is None:
#         return True
#     left = True
#     right = True
#     if current.left is not None:
#         if current.left.value > current.value:
#             left = False
#         if current.value > parent.value \
#                 and current.left.value <= parent.value:
#             left = False

#     if current.right is not None:
#         if current.right.value <= current.value:
#             right = False
#         if current.value <= parent.value \
#                 and current.left.value > parent.value:
#             right = False

#     if left == True:
#         left = is_valid(current.left, current)
#     if right == True:
#         right = is_valid(current.right, current)

#     return left and right


# def is_bst(root):
#     if root is None:
#         return True
#     else:
#         is_tree_valid = is_valid(root.left, root) \
#             and is_valid(root.right, root)
#         return is_tree_valid


def is_bst_rec(current, prev):
    if current is not None:
        if is_bst_rec(current.left, prev) is False:
            return False
        if prev is not None \
                and prev.value >= current.value:
            return False
        return is_bst_rec(current.right, current)
    else:
        return True


def is_bst(root):
    prev = None
    return root.is_bst_rec(prev)


root = Node(4)
root.insert(2)
root.insert(7)
root.insert(1)
root.insert(3)
root.insert(6)

invalid_bst = Node(3)
invalid_bst.left = Node(2)
invalid_bst.left.left = Node(1)
invalid_bst.right = Node(5)
invalid_bst.right.left = Node(2)
invalid_bst.right.right = Node(6)

# print(root.lca(2, 7))
# print(root.find(6))
# print(is_bst(root))
# print(is_bst(invalid_bst))
print(is_bst(root))
print(is_bst(invalid_bst))
