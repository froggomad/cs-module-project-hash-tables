def word_count(s):
    d = {}
    phrase = ""

    chars_to_ignore = '":;,.-+=/\\|[]{}()*^&'
    
    for char in s:
        if char not in chars_to_ignore:
            phrase += char

    words = phrase.lower().split()

    # count each word
    for i in range(len(words)):        
        if words[i] not in d:            
            d[words[i]] = 0
        else:
            d[words[i]] += 1

    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))