import os
from collections import OrderedDict


# TODO: Use a Hashmap and a doubly linked list to locate cache entries in O(1) time and a doubly linked list to maintain usage order
# TODO: Research popitem(last=False)
# TODO: Create pytests and check for functionality
# TODO: Import clock and enforce cache expiration, each entry should have an expiry/duration time i.e TTL (time to live), per-key expiry
# TODO: Add a fixed size to the OrderedDict at creation by overriding a dunder method -> __setitem__
class LRUCache:

    def __init__(self, capacity: int = 3, duration: int = 5):
        """Initialize a LRU Cache with a fixed capacity and a duration for TTL in seconds"""
        self.dict: OrderedDict = OrderedDict()
        self.capacity = capacity
        self.duration = duration

    def get(self, key: str) -> int:
        """Return the value of a given key if it exists in the cache, otherwise return -1. The accessed item is marked as the MRU (most recently used)"""
        if self.dict[key]:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: str, value: int):
        """Insert a new key-value pair or updates an existing key, if the cache exceeds capacity then the LRU (least recently used) item is removed"""
        if (self.capacity + 1 > len(self.dict)):
            pass
            # self.dict.pop()

        if (len(self.dict) + 1 > self.capacity):
            pass
        
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
cache = LRUCache(capacity = 3, duration = 10)
cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)

cache.get("A")

cache.put("D", 4)
cache.get("B")

print(cache)