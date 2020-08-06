"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

"""
for n in q:
    sum each pair, store in dict (ie 1+3 = 4 == d[(0,1)] = 4)

for n in q:
    diff each pair, return if match, or return None
"""
def find_matches(l):
    result = []
    d = {}
    e = {}
    # TODO: Efficiency
    # get the index and value of each node in q and add/subtract, storing in separate dictionaries with keys as tuples of keys and value as value
    for key, value in enumerate(l):
        for next_key, next_value in enumerate(l):            
            # subtract no matter what
            e[(key, next_key)] = value - next_value
            # addition will have the same result with inverse keys, so avoid extra work
            if (next_key, key) not in d.keys():
                d[(key, next_key)] = value + next_value

    #what I find really interesting here is what I expect to be the value at each position is actually the key. If I do k, v in d, I get the index and key where I would expect the key and value
    for v in d:
        for v2 in e:
            if d[v] == e[v2]:
                #print(f"match\nkey1: {v}\nkey2: {v2}")
                #print(f"value1: {d[v]}\nvalue2: {e[v2]}\n")
                result.append((v, v2))
    return result

print(find_matches(q))