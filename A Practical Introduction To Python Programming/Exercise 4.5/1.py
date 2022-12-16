# Write a program that asks the user to enter a length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program
# should convert the length to inches and print out the result. There are 2.54 centimeters in an
# inch.

user_input = float(input('Enter a length in centimeters: '))
if user_input < 0:
    print('Invalid input!')
else:
    print(f'{round((user_input / 2.54), 2)} inch')


# Enter a length in centimeters: 14.5
# 5.71 inch