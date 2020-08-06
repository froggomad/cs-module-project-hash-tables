def word_count(s):
    d = {}
    phrase = ""

    chars_to_ignore = '":;,.-+=/\\|[]{}()*^&'
    # add characters to phrase
    for char in s:
        if char not in chars_to_ignore:
            phrase += char
    # split phrase into words
    words = phrase.lower().split()

    # count each word
    for word in words:        
        if word not in d:            
            d[word] = 1
        else:
            d[word] += 1

    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello   hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))