#!/usr/bin/env python3
""" Basic Caching Implementation
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system inheriting from base caching

    Args:
        BaseCaching: A base class for caches
    """
    def __init__(self):
        """Initializaiton of cache
        """
        super().__init__()

    def put(self, key, item):
        """Adds to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
