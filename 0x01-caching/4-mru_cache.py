#!/usr/bin/env python3
"""Most Recently Used caching module.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """init"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_rused, _ = self.cache_data.popitem(last=True)
            print(f'DISCARD: {most_rused}')

        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data.pop(key)
        self.cache_data[key] = item

        return item
