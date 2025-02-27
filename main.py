
def print_string(word):

    return word

def count_vowels(word):
    vowels = "аеёиоуыэюя"
    return sum(1 for letter in word if letter in vowels)

def onefunc(word):
    return word[::-1]

def removeduplicates(word):
    unique_chars = ""
    for char in word:
        if char not in unique_chars:
            unique_chars += char