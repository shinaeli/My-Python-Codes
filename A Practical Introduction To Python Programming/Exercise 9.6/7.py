# Recall that, given a string s, s.index('x') returns the index of the first x in s and an error
# if there is no x.
# (a) Write a program that asks the user for a string and a letter. Using a while loop, the
# program should print the index of the first occurrence of that letter and a message if the
# string does not contain the letter.
# (b) Write the above program using a for/break loop instead of a while loop.

position = 0
user_string = input('Provide a string: ').lower()
user_letter = input('Provide a letter to search for: ').lower()
while position < len(user_string):
    if user_string[position] == user_letter:
        print(f'The index of the first occurrence of "{user_letter}" in "{user_string}" is {position}.')
        break
    position += 1
# This is a special 'else' block that comes into action only when the entire loop(be it while or for loop)
# runs completely without a break
else:
    print('It never exist in the string.')



