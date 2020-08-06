"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
q = set(range(1, 200))
#q = (1, 3, 4, 7, 12)


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
    additions = {}
    subtractions = {}
    # TODO: Efficiency
    # get the index and value of each node in q and add/subtract, storing in separate dictionaries with keys as tuples of keys and value as value
    for key, value in enumerate(l):
        for next_key, next_value in enumerate(l):
            if (key, next_key) not in additions.keys():
                additions[(key, next_key)] = value + next_value
            
            if (next_key, key) not in subtractions.keys():
                sub_val = next_value - value
                subtractions[(next_key, key)] = sub_val

    #what I find really interesting here is what I expect to be the value at each position is actually the key. If I do k, v in d, I get the index and key where I would expect the key and value
    for v in additions:
        for v2 in subtractions:
            if additions[v] == subtractions[v2]:
                result.append((v, v2))
    return result

print(find_matches(q))

"""
f(0) + f(0) = f(4) - f(3)    10 + 10 = 54 - 34
f(0) + f(2) = f(4) - f(2)    10 + 22 = 54 - 22

f(2) + f(0) = f(4) - f(2)    22 + 10 = 54 - 22

f(0) + f(3) = f(4) - f(0)    10 + 34 = 54 - 10
f(2) + f(2) = f(4) - f(0)    22 + 22 = 54 - 10

f(3) + f(0) = f(4) - f(0)    34 + 10 = 54 - 10

f(1) + f(1) = f(4) - f(3)    18 + 18 = 54 - 18
"""