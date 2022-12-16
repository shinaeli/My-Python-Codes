# Write a program that asks the user to enter a string, then prints out each letter of the string
# doubled and on a separate line. For instance, if the user entered HEY, the output would be
# HH
# EE
# YY

user_input = input('Enter a word of your choice: ')

for word in user_input:
    print(2 * word)


# Enter a word of your choice: hey
# hh
# ee
# yy