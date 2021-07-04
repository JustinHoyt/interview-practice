class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return ("key: " + self.key + " value " + self.value + " next " + self.next + " prev " + self.prev)


class LRUCache:
    '''
    [3,3] -> [2,2] -> None
    cache.get(2)
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list_head = None
        self.linked_list_tail = None
        self.dict = {}

    def __str__(self):
        result = ""
        node = self.linked_list_head
        while node:
            result += ("key: " + str(node.key) + " value " + str(node.value) + "\n")
            node = node.next

    def get(self, key: int) -> int:
        print("get", key)
        if key not in self.dict:
            return -1

        node = self.dict[key]

        # if node in the middle of linked list
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.linked_list_head
            self.linked_list_head = node

        # if node at the head, then you don't have to move it
        # if node at the tail
        elif node.prev:
            self.linked_list_tail = node.prev
            node.prev.next = None
            node.next = self.linked_list_head
            self.linked_list_head = node

        print("hello")
        return self.dict[key].value

    def put(self, key: int, value: int) -> None:
        '''
        [3,3] -> [1,1] -> None
        cache.get(2)
        '''
        print("put", key, value)
        new_node = LinkedListNode(key, value)

        if len(self.dict) == 0:
            self.linked_list_tail = new_node
            self.linked_list_head = new_node
        else:
            self.linked_list_head.prev = new_node
            new_node.next = self.linked_list_head
            self.linked_list_head = new_node
            self.dict[key] = new_node

            if len(self.dict) > self.capacity:
                del self.dict[self.linked_list_tail.key]
                self.linked_list_tail = self.linked_list_tail.prev
                self.linked_list_tail.next = None


cache = LRUCache(2)

cache.put(1, 1)
# print(cache)
cache.put(2, 2)
print(cache.get(1))       # returns 1
cache.put(3, 3)    # evicts key 2
print(cache.get(2))       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4
