#!/usr/bin/env python3
"""FIFOCache"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """init"""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        if key is not None and item is not None:
            self.keys_order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.keys_order[0]
                del self.cache_data[first_key]
                self.keys_order.pop(0)
                print(f'DISCARD: {first_key}')

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
