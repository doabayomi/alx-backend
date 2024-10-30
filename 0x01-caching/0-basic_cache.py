#!/usr/bin/env python3
""" BaseCaching module
"""
from collections import OrderedDict
from base_cache import BaseCaching


class BasicCache(BaseCaching):
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
