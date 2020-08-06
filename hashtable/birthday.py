import hashlib
import random

def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff

def how_many_before_collision(slots, loops=1):
    for i in range(loops):
        tries = 0
        tried = set()
    
        while True:
            random_key = random.random()
            index = hash_function(random_key) % slots

            if index not in tried:
                tried.add(index)
                tries += 1

            else:
                break

        print(f"{slots} slots, {tries} hashes before collision. ({tries / slots * 100:.1f})")

#128 slots, 10 times

how_many_before_collision(128, 10)