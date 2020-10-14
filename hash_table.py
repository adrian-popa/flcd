import hashlib

from collections import deque


class HashTable:

    def __init__(self, size):
        self.__items = [deque() for _ in range(size)]

    def add(self, key, value):
        hashed_key = int(hashlib.sha1(key).hexdigest(), 16) % (10 ** 8)
        if hashed_key in self.__items:
            self.__items[hashed_key] = value
        else:
            self.__items[hashed_key].append(value)
