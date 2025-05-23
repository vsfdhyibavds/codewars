# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    words = s.split()
    min_length = len(words[0])
    for word in words:
        if len(word) < min_length:
            min_length = len(word)
    return min_length