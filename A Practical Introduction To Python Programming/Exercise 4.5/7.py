# Write a program that asks the user for two numbers and prints Close if the numbers are
# within .001 of each other and Not close otherwise.

number_1 = float(input('Provide the first number: '))
number_2 = float(input('Provide the second number: '))

if (number_1 - number_2 <= 0.001) or (number_2 - number_1 <= 0.001):
    print('Close')
else:
    print('Not Close')

# Provide the first number: 3
# Provide the second number: 3.2991213
# Close
