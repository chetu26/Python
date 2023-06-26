input_str = input("Enter the list of words: ")
words = input_str.split()
print(words)
word_lengths = {word: len(word) for word in words}
print(word_lengths)
