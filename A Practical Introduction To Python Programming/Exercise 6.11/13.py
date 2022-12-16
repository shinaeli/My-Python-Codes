# Write a program that asks the user to enter two strings of the same length. The program
# should then check to see if the strings are of the same length. If they are not, the program
# should print an appropriate message and exit. If they are of the same length, the program
# should alternate the characters of the two strings. For example, if the user enters abcde and
# ABCDE the program should print out AaBbCcDdEe.

user_input1 = input('Provide a word: ')
user_input2 = input('Provide another word of the same length: ')

if len(user_input1) != len(user_input2):
    print('You provided the wrong inputs.')
else:
    output = ''
    for count in range(len(user_input2)):
        output += user_input2[count]
        output += user_input1[count]
    print(output)

# Provide a word: abcde
# Provide another word of the same length: ABCDE
# AaBbCcDdEe
# Provide a word: board
# Provide another word of the same length: broad
# bbrooaardd

