from collections import OrderedDict
from datetime import datetime

class LRUCache(OrderedDict):

    def __init__(self, capacity, expiration_time):
        self.capacity = capacity
        # 5 minute expiration
        self.expiration_time = expiration_time

    def get(self, key):
        if key not in self:
            return -1

        self.move_to_end(key)

        if self[key][0] > datetime.now() + expiration_time:
            self.popitem(last = False)
            return -1

        return self[key][1]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = (datetime.now(), value)
        if len(self) > self.capacity:
            self.popitem(last = False)

    # some sort of async function that runs periodically
    def _garbage_collection(self):
        pass

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity, expiration_time)
# param_1 = obj.get(key)
# obj.put(key,value)
