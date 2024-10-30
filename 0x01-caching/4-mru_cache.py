#!/usr/bin/env python3
""" Most Recently Used Caching Implementation.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A MRU cache (most recently used)

    Args:
        BaseCaching: base caching class
    """
    def __init__(self):
        """Initializaiton of cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        if len(self.cache_data) >= self.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
