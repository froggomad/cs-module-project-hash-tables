def char_count(s):
    d = {}
    for char in s:
        if char.isspace():
            continue
        
        char = char.lower()
        if char not in d:
            d[char] = 0

        d[char] += 1
    return d

print(char_count("HELLO")["l"])

def sorted_letter_count(s):
    d = char_count(s)

    items = list(d.items())
    #sort by highest value
    items.sort(key=lambda e: e[1], reverse = True)

    for i in items:
        print(f"{i[0]}:{i[1]}")

print(sorted_letter_count("Sally sells seashells by the seashore"))