# Without using the index method, write a program that asks the user for a string and
# a letter and prints out the index of the first occurrence of the letter in the string. If the
# letter is not in the string, the program should say so.

user_input = input('Provide a word: ').lower()
letter_to_be_checked = input('Provide the alphabet to be checked: ').lower()
counter, output = 0, 0

for letter in user_input:
    counter += 1
    if letter == letter_to_be_checked:
        output = counter - 1
        break

if output >= 0:
    print(f"The index of '{letter_to_be_checked}' in '{user_input}' is {output}.")
else:
    print(f"{letter_to_be_checked} does not exist in {user_input}.")


# Provide a word: letter
# Provide the alphabet to be checked: t
# The index of 't' in 'letter' is 2.
# Provide a word: letter
# Provide the alphabet to be checked: R
# The index of 'r' in 'letter' is 5.
# Provide a word: letter
# Provide the alphabet to be checked: L
# The index of 'l' in 'letter' is 0.
