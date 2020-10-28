import hashlib
from collections import deque


class HashTable:

    def __init__(self, size):
        self.__items = [deque() for _ in range(size)]
        self.__size = size

    def add(self, key):
        hashed_key = int(hashlib.sha1(str(key).encode('utf-8')).hexdigest(), 16) % (10 ** 8)
        if self.contains(key):
            return self.get_position(key)
        self.__items[hashed_key].append(key)
        return self.get_position(key)

    def contains(self, key):
        hashed_key = int(hashlib.sha1(str(key).encode('utf-8')).hexdigest(), 16) % (10 ** 8)
        return key in self.__items[hashed_key]

    def remove(self, key):
        hashed_key = int(hashlib.sha1(str(key).encode('utf-8')).hexdigest(), 16) % (10 ** 8)
        self.__items[hashed_key].remove(key)

    def get(self, key):
        hashed_key = int(hashlib.sha1(str(key).encode('utf-8')).hexdigest(), 16) % (10 ** 8)
        return self.__items[hashed_key]

    def get_position(self, key):
        hashed_key = int(hashlib.sha1(str(key).encode('utf-8')).hexdigest(), 16) % (10 ** 8)
        index = 0

        for item in self.__items[hashed_key]:
            if item != key:
                index += 1
            else:
                break

        return hashed_key, index

    def items(self):
        return self.__items

    def __str__(self) -> str:
        result = 'Symbol Table\n'
        for i in range(self.__size):
            result += str(i) + '->' + str(self.__items[i]) + '\n'
        return result
