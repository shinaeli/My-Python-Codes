# (a) Write a program that uses a while loop (not a for loop) to read through a string and print
# the characters of the string one-by-one on separate lines.
# (b) Modify the program above to print out every second character of the string.

user_input = input('enter a string: ')
i = 0
while i < len(user_input):
    print(user_input[i])
    i+=1

user_input = input('enter a string: ')
i = 0
while i < len(user_input):
    print(user_input[i])
    i+=2
