
def print_string(word):

    return word

def count_vowels(word):
    vowels = "аеёиоуыэюя"
    return sum(1 for letter in word if letter in vowels)