#!/usr/bin/env python3
""" Least Recently Used Caching Implementation
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
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

        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.popitem(last=False)

    def get(self, key):
        """Retrieves from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
