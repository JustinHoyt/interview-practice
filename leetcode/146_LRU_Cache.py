class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = None
        self.dict = {}

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        # remove least recently used if at capacity
        new_node = LinkedListNode(value)
        new_node.next = self.linked_list
        self.linked_list = new_node
        self.dict[key] = new_node

        if len(self.dict) >= self.capacity:



cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4
