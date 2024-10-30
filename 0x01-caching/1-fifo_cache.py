#!/usr/bin/env python3
""" FIFO Caching Implementation
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO (queue) Cache

    Args:
        BaseCaching: base cache class
    """
    def __init__(self):
        """Initialization with ordered dictionary
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds to the cache

        Args:
            key: key to add
            item: corresponding value to add
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_in_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD:{first_in_key}")

    def get(self, key):
        """Retrieves dta from the cache

        Args:
            key: key to data

        Returns:
            corresponding value to the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
