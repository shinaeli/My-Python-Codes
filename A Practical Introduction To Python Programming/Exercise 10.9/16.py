# Write a program that converts a decimal height in feet into feet and inches. For instance, an
# input of 4.75 feet should become 4 feet, 9 inches.

user_input = input('provide a length in feet(must be a decimal): ')
dot_index = user_input.index('.')
first_integer = user_input[0:dot_index]
# print(first_integer)
decimals = float(user_input) - int(first_integer)
# print(decimals)
inched = decimals * 12
print(f'{int(first_integer)} feet, {int(inched)} inches')

# provide a length in feet(must be a decimal): 4.75
# 4 feet, 9 inches
# provide a length in feet(must be a decimal): 361.592
# 361 feet, 7 inches
# provide a length in feet(must be a decimal): 18.048
# 18 feet, 0 inches