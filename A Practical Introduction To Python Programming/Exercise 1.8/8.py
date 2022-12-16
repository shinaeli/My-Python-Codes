# Write a program that asks the user to enter three numbers (use three separate input statements).
# Create variables called total and average that hold the sum and average of the
# three numbers and print out the values of total and average.

user_input1 = int(input('Provide the first number: '))
user_input2 = int(input('Provide the second number: '))
user_input3 = int(input('Provide the third number: '))

total = user_input1 + user_input2 + user_input3
average = total / 3

print(f'The sum of {user_input1}, {user_input2} and {user_input3} is {total} while their average is {average}.')


# Provide the first number: 71
# Provide the second number: 29
# Provide the third number: 35
# The sum of 71, 29 and 35 is 135 while their average is 45.0.
# Provide the first number: 21
# Provide the second number: 48
# Provide the third number: 76
# The sum of 21, 48 and 76 is 145 while their average is 48.333333333333336.
