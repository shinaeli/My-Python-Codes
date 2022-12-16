# A simple way to estimate the number of words in a string is to count the number of spaces
# in the string. Write a program that asks the user for a string and returns an estimate of how
# many words are in the string.

user_input = input('Enter a sentence(s): ')
count = 0
for each in user_input:
    if each == ' ':
        count += 1
    else:
        continue
if count == 0:
    print(f'There is only one word in "{user_input}".')
elif user_input[-1] == ' ':
    print(f'There are {count} words in "{user_input}".')
else:
    print(f'There are {count + 1} words in "{user_input}".')

