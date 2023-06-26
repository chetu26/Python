def find_short_words(string):
    words = string.split()  # Split the string into a list of words
    short_words = [word for word in words if len(word) < 4]
    return short_words

input_string = input('enter string:')
result = find_short_words(input_string)
print(result)
