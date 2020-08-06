#convert letters in the string
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S',
    ' ': ' '
}

decode_table = {}

for k, v in encode_table.items():
    decode_table[v] = k

def encode(s):
    r = ""
    for char in s:
        r += encode_table[char]
    return r

def decode(s):
    r = ""
    for char in s:
        r += decode_table[char]
    return r

lamb = encode("Mary had a Little lamb".upper())

mary = decode(lamb)

print(mary.capitalize())
