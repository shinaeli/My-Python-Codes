# Write a program that asks the user to enter a string. The program should then print the
# following:
# (a) The total number of characters in the string
# (b) The string repeated 10 times
# (c) The first character of the string (remember that string indices start at 0)
# (d) The first three characters of the string
# (e) The last three characters of the string
# (f) The string backwards
# (g) The seventh character of the string if the string is long enough and a message otherwise
# (h) The string with its first and last characters removed
# (i) The string in all caps
# (j) The string with every a replaced with an e

user_input = input('Enter a string: ')
print(len(user_input))
print(user_input * 10)
print(user_input[0])
print(user_input[0:3])
print(user_input[-3:])
output = user_input[::-1]
print(output)
if len(user_input) > 7:
    print(user_input[7])
else:
    print('The string is less than 7 in length.')
output1 = user_input.replace(user_input[0], '')
output2 = output1.replace(user_input[-1], '')
print(output2)
print(user_input.upper())