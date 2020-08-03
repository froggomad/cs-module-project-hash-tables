import sys
import re

class HashTableEntry:
    def __init__(self):
        pass

    def __str__(self):
        return ""

class HashTable:
    def __init__(self):
        pass

    def __str__(self):
        return ""

    def fnv1_64(self, string, seed=0):
        FNV_prime = 1469511628211
        offset_basis = 1469581039346656037

        hash = offset_basis + seed
        for char in string:
            hash = hash ^ ord(char)
            hash = hash * FNV_prime
        return hash

hashtbl = HashTable()
print(hashtbl.fnv1_64("dog"))