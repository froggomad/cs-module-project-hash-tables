import sys
import re

class HashTableEntry:
    def __init__(self):
        pass

    def __str__(self):
        return ""

class HashTable:
    def __init__(self, data_size=3):
        self.__hash_data = [None] * data_size

    def __str__(self):
        return f"size: {self.len}"

    def len(self):
        return len(self.__hash_data)

    def hash(self, string, seed=0):
        """fnv1_64 hash function"""
        FNV_prime = 1469511628211
        offset_basis = 1469581039346656037

        hash = offset_basis + seed
        for char in string:
            hash = hash ^ ord(char)
            hash = hash * FNV_prime
        return hash

    def get_index(self, s):
        hash_value = hash(s)        
        return hash_value % self.len()

    def get(self, key):
        index = self.get_index(key)
        return self.__hash_data[index]

    def put(self, key, value):
        index = self.get_index(key)
        self.__hash_data[index] = value

    def delete(self, key):
        index = self.get_index(key)
        self.__hash_data[index] = None