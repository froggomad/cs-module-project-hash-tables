cache = {}

def fib(n):
    """return the nth fibonnaci number recursively"""
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

for i in range(20000):
    print(f"{i:3}: {fib(i)}")