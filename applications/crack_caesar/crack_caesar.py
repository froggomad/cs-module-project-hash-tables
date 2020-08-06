# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

#Working Cipher:

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

def decode(s, with_dict):
    r = ""
    for char in s:
        r += with_dict[char]
    return r



# Your code here

#from wikipedia
frequency = {
    "A": 8.497,
    "B": 1.492,
    "C": 2.202,    
    "D": 4.253,    
    "E": 11.162,
    "F": 2.228,    
    "G": 2.015,    
    "H": 6.094,    
    "I": 7.546,    
    "J": 0.153,    
    "K": 1.292,    
    "L": 4.025,    
    "M": 2.406,    
    "N": 6.749,    
    "O": 7.507,    
    "P": 1.929,    
    "Q": 0.095,    
    "R": 7.587,    
    "S": 6.327,    
    "T": 9.356,
    "U": 2.758,    
    "V": 0.978,    
    "W": 2.560,    
    "X": 0.150,    
    "Y": 1.994,    
    "Z": 0.077
}
items = list(frequency.items())
items.sort(key=lambda e: e[1], reverse=True)
letters_by_frequency = ''.join([item[0] for item in items])

print(f"letters by freq: {letters_by_frequency}")

lamb = encode("Mary had a Little lamb whos fleece was white as snow everywhere that mary went the lamb was sure to go".upper())

letterCount = {}
#init letterCount dictionary
for letter in letters_by_frequency:
    letterCount[letter] = 0
#get letter counts
for letter in lamb.upper():
    if letter in letters_by_frequency:
        letterCount[letter] += 1

count_list = letterCount
#replace letters in letterCount according to precedence in letters by frequency
translated_dict = {}
letter_count_by_frequency = list(letterCount.items())
letter_count_by_frequency.sort(key=lambda e: e[1], reverse=True)
for i, letter in enumerate(letter_count_by_frequency):
    key = letters_by_frequency[i]
    translated_dict[letter[0]] = key

translated_dict[' '] = ' '
print(f"encoded: {lamb}")
print(f"cipher: {translated_dict}")
decoded = decode(lamb.upper(), translated_dict)
print(f"decoded: {decoded}")

# print(mary.capitalize())

# print(letterCount)