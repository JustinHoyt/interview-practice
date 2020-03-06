class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def insert(self, val):
        if val <= self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)


    def contains(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left:
                return self.left.contains(val)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(val)
            else:
                return False


    @staticmethod
    def initialize(vals):
        node = Node(vals[0])
        for i in range(1, len(vals)):
            node.insert(vals[i])
        return node


def in_order_print(root):
    if root is None:
        return
    in_order_print(root.left)
    print(root.val)
    in_order_print(root.right)


def pre_order_print(root):
    if root is None:
        return
    print(root.val)
    pre_order_print(root.left)
    pre_order_print(root.right)


# def divide_elements_highest_to_lowest(root):
#     if root.right:
#         result = divide_elements_highest_to_lowest(root.right) / root.val
#     else:
#         result = root.val
#     if root.left:
#         return result / divide_elements_highest_to_lowest(root.left)
#     else:
#         return result

def divide_elements_highest_to_lowest(root):

    result = None
    def divide_rec(root):
        nonlocal result
        if root is None:
            return

        divide_rec(root.right)

        # if at the highest value, set it as the result
        if root.right is None and result is None:
            result = root.val
        else:
            result /= root.val

        divide_rec(root.left)

    divide_rec(root)
    return result



root = Node(5)
root.insert(6)
root.insert(2)
root.insert(15)
assert root.right.val == 6
assert not root.contains(14)
assert root.contains(15)


# divide_tree = Node(10)
# divide_tree.insert(40)
# divide_tree.insert(2)
divide_tree = Node(4)
divide_tree.left = Node(2)
divide_tree.right = Node(128)
divide_tree.right.left = Node(8)
# in_order_print(divide_tree)
print(divide_elements_highest_to_lowest(divide_tree))


# initialized_tree = Node.initialize([50,26,20,24,10,30,100,2,70])
# in_order_print(initialized_tree)
