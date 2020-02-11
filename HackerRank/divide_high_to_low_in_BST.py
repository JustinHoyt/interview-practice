class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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



divide_tree = Node(4)
divide_tree.left = Node(2)
divide_tree.right = Node(128)
divide_tree.right.left = Node(8)
print(divide_elements_highest_to_lowest(divide_tree))


