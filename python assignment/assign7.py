def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([char for char in string if char.lower() not in vowels])

input_string = input('ebter string:')
result = remove_vowels(input_string)
print(result)  
