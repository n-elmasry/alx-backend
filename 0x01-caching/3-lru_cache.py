#!/usr/bin/env python3
"""Least Recently Used caching module.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """init"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_used, _ = self.cache_data.popitem(last=False)
                print(f'DISCARD: {least_used}')

        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
