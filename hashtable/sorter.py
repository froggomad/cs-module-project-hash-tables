d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

def sorter(e):
    return e[1]

items = list(d.items())
#sort by key
#items.sort()
#sort by value
#items.sort(key=sorter)
#with a lambda
items.sort(key=lambda e: e[1])
print(items)