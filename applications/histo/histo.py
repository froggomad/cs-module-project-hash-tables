# Your code here

# strip punctuation from string
def strip_word(s):
    r = ""
    chars_to_ignore = '"?:;,.-+=/\\|[]{}()*^&'
    for char in s:
        if char not in chars_to_ignore:
            r += char
    return r

word_counts = {}

# Open file (read-only)
fp = open('robin.txt', 'r')
# Store whole file in string
text = fp.read()
# Split string into array of strings
for word in text.split():
    # Remove punctuation
    strip_word(word)
    # Add count
    if word in word_counts:
        word_counts[word] += "#"
    else:
        word_counts[word] = "#"
# Close file 
fp.close()

print(word_counts)