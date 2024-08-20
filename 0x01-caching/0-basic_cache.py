#!/usr/bin/env python3
"""BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item value for the key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
