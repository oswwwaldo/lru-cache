from collections import OrderedDict
from collections.abc import Callable
from functools import wraps
from typing import Final, Literal

# In the future implement a full cache system...
# TODO: Leat Frequently Used
# TODO: First-In, First-Out
# TODO: Last-In, First-Out
# TODO: Most Recently Used
# TODO: Time-To-Live
# TODO: Random / 2-Random

# TODO: Adaptive Replacement Cache
# TODO: Segmented LRU & Click / CAR
# TODO: SIEVE 
# A great docstring acts like a user manual for anyone calling the function —
# We don't need to know how it's done, just what it does unless there are side effects

# `with` works on any object with the two dunder methods: `__enter__` & `__exit__`
# TODO: Implement `with` functionality with `LRUCache`
# TODO: Use a Hashmap and a doubly linked list to locate cache entries in O(1) time and a doubly linked list to maintain usage order
# TODO: Research popitem(last=False)
# TODO: Create pytests and check for functionality
# TODO: Import clock and enforce cache expiration, each entry should have an expiry/duration time i.e TTL (time to live), per-key expiry
# TODO: Add a fixed size to the OrderedDict at creation by overriding a dunder method -> __setitem__
class LRUCache:

    def __init__(self, capacity: int = 3, duration: int = 5):
        """Initialize a LRU Cache with a fixed capacity and a duration for TTL in seconds"""
        self.dict: OrderedDict[str, str] = OrderedDict()
        self.capacity = capacity
        self.duration = duration

    # Check if capacity has been reached before updating
    def __setitem__(self, key: str, value: int) -> None:
        if (len(self.dict) >= self.capacity and key not in self.dict):
            print("Too large")
        else:
            super().__setitem__(key, value)

    # Update, then remove the oldest item if capacity exceeds   
    # def __setitem__(self, key, value):
    #     super().__setitem__(key, value)

    #     if len(self) > self.capacity:
    #         self.dict.popitem(last=False)

    def show(self, func: Callable) -> Callable:
        if DEBUG_MODE is True:
            print(list(self.dict.items()))
            return func
        else:
            return func

    @staticmethod
    def debug(func: Callable):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if DEBUG_MODE:
                print(f"{func.__name__}{args} -> result: {list(self.dict.items())}")
            return result
        return wrapper

    @debug
    def get(self, key: str) -> str | Literal[-1]:
        """Return the value of a given key if it exists in the cache, otherwise return -1. The accessed item is marked as the MRU (most recently used)"""
        if self.dict[key]:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    @debug
    def put(self, key: str, value: int):
        """Insert a new key-value pair or updates an existing key, if the cache exceeds capacity then the LRU (least recently used) item is removed"""
        if (self.capacity + 1 > len(self.dict)):
            pass
            # self.dict.pop()

        if (len(self.dict) + 1 > self.capacity):
            pass
        else:
            self.dict[key] = str(value)
