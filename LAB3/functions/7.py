#Write a function word_frequency that takes a string as input and returns a dictionary where keys are unique words, and values are their frequencies.
def word_frequency(word):
    words = word.split()
    return {word: words.count(word) for word in set(words)}

string = str(input())
result = word_frequency(string)
print(result)