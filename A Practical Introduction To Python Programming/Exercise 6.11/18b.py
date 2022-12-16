# (b) Without using the count method, write a program that asks the user for a string and a
# letter and counts how many occurrences there are of the letter in the string.

user_input = input('Provide a word: ').lower()
letter_to_be_checked = input('Provide the alphabet to be checked: ').lower()
counter = 0

for letter in user_input:
    if letter == letter_to_be_checked:
        counter += 1
    else:
        counter += 0

print(f"'{letter_to_be_checked}' has {counter} occurrences in '{user_input}'.")

# Provide a word: YESTeRday
# Provide the alphabet to be checked: e
# 'e' has 2 occurrences in 'yesterday'.
# Provide a word: chrisTOPHEr
# Provide the alphabet to be checked: y
# 'y' has 0 occurrences in 'christopher'.
# Provide a word: chrisTOPHEr
# Provide the alphabet to be checked: C
# 'c' has 1 occurrences in 'christopher'.