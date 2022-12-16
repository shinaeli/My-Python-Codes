# Write a program that asks the user to enter a word that contains the letter a. The program
# should then print the following two lines: On the first line should be the part of the string up
# to and including the first a, and on the second line should be the rest of the string. Sample
# output is shown below:
# Enter a word: buffalo
# buffa
# lo

user_input = input('Provide a word: ')

if 'a' in user_input:
    get_index = user_input.index('a')
    first_portion = user_input[0:get_index + 1]
    print(first_portion)
    last_portion = user_input[get_index+1:]
    print(last_portion)
