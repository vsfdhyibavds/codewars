# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    # Create a list of tuples containing the word and its number
    word_number_pairs = []
    for word in words:
        number = int(next(c for c in word if c.isdigit()))
        word_number_pairs.append((number, word))
    # Sort the list based on the number
    word_number_pairs.sort()
    # Extract the words in order
    sorted_words = [word for number, word in word_number_pairs]
    return ' '.join(sorted_words)