class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def get_Kth_node_from_end(root, distance):
    curr = root
    count = 0

    while curr:
        curr = curr.next
        count += 1

    curr = root
    for _ in range(count-distance):
        curr = curr.next

    return curr.value


root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
print(get_Kth_node_from_end(root, 4))
