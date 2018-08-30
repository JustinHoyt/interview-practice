from queue import Queue

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


    def lowest_common_ancestor(self, v1, v2):
        right = max(v1, v2)
        left = min(v1, v2)
        if self.value <= right and self.value >= left:
            print("found it")
            return self.value
        elif self.value < left:
            print("going right")
            if self.right is not None:
                return self.right.lowest_common_ancestor(v1, v2)
        elif self.value > right:
            print("going left")
            if self.left is not None:
                return self.left.lowest_common_ancestor(v1, v2)


    def find(self, value):
        if self.value == value:
            return True
        if value < self.value:
            print("here")
            if self.left:
                return self.left.find(value)
            else:
                return False
        if value > self.value:
            print("here")
            if self.right:
                return self.right.find(value)
            else:
                return False


    def is_bst_rec(self, prev):
        if self:
            if self.left and self.left.is_bst_rec(prev) is False:
                return False
            if prev and prev.value >= self.value:
                return False
            if self.right:
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
    if current:
        if is_bst_rec(current.left, prev) is False:
            return False
        if prev and prev.value >= current.value:
            return False
        return is_bst_rec(current.right, current)
    else:
        return True


def is_bst(root):
    prev = None
    return root.is_bst_rec(prev)

def longest_common_path_rec(root, best):
    if root is None:
        return 1,1
    left, _ = longest_common_path_rec(root.left, best)
    right, _ = longest_common_path_rec(root.right, best)
    if root.left and root.left.value - 1 == root.value:
        left += 1
    else:
        best = max(left, best)
        left = 1
    if root.right and root.right.value - 1 == root.value:
        right += 1
    else:
        best = max(right, best)
        right = 1

    so_far = max(left, right)
    best = max(so_far, best)
    return so_far, best


def longest_common_path(root):
    best = 0
    result = longest_common_path_rec(root, best)[1]
    return result


def breadth_first_find(root, value):
    next_to_visit = Queue()
    next_to_visit.put(root)
    while next_to_visit.empty() is False:
        print("here")
        current = next_to_visit.get(root)
        if current.value == value:
            return True

        if current.left:
            next_to_visit.put(current.left)
        if current.right:
            next_to_visit.put(current.right)

    return False


valid_bst = Node(4)
valid_bst.insert(2)
valid_bst.insert(7)
valid_bst.insert(1)
valid_bst.insert(3)
valid_bst.insert(6)

invalid_bst = Node(3)
invalid_bst.left = Node(2)
invalid_bst.left.left = Node(1)
invalid_bst.right = Node(5)
invalid_bst.right.left = Node(2)
invalid_bst.right.right = Node(6)

longest_common_path_tree = Node(1)
longest_common_path_tree.left = Node(2)
longest_common_path_tree.left.left = Node(3)
longest_common_path_tree.right = Node(4)
longest_common_path_tree.right.left = Node(5)
longest_common_path_tree.right.right = Node(6)
longest_common_path_tree.right.right.left = Node(7)

# print(valid_bst.lowest_common_ancestor(2, 7))
# print(valid_bst.find(6))
# print(is_bst(valid_bst))
# print(is_bst(invalid_bst))
# print(is_bst(valid_bst))
# print(is_bst(invalid_bst))
print(longest_common_path(longest_common_path_tree))
# print(breadth_first_find(valid_bst, 9))
