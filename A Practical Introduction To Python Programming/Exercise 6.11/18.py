# The goal of this exercise is to see if you can mimic the behavior of the in operator and the
# count and index methods using only variables, for loops, and if statements.
# (a) Without using the in operator, write a program that asks the user for a string and a letter
# and prints out whether or not the letter appears in the string.
# (b) Without using the count method, write a program that asks the user for a string and a
# letter and counts how many occurrences there are of the letter in the string.
# (c) Without using the index method, write a program that asks the user for a string and
# a letter and prints out the index of the first occurrence of the letter in the string. If the
# letter is not in the string, the program should say so.

user_input = input('Provide a word: ').lower()
letter_to_be_checked = input('Provide the alphabet to be checked: ').lower()
checker_array = []

for letter in user_input:
    if letter == letter_to_be_checked:
        checker_array.append('true')
        break
    else:
        continue

if 'true' in checker_array:
    print(f"'{letter_to_be_checked}' exists in '{user_input}'.")
else:
    print(f"'{letter_to_be_checked}' does not exist in '{user_input}'.")

# Provide a word: come
# Provide the alphabet to be checked: d
# 'd' does not exist in 'come'.
# Provide a word: GOAL
# Provide the alphabet to be checked: l
# 'l' exists in 'goal'.





