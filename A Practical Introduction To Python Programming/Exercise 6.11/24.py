# . In calculus, the derivative of x
# 4
# is 4x
# 3
# . The derivative of x
# 5
# is 5x
# 4
# . The derivative of x
# 6
# is
# 6x
# 5
# . This pattern continues. Write a program that asks the user for input like x^3 or x^25
# and prints the derivative. For example, if the user enters x^3, the program should print out
# 3x^2

user_input = input('Provide a polynomial: ')
first_product = 0

if '^' in user_input:
    get_index = user_input.index('^')
    get_power = user_input[get_index + 1:]
    if get_power == '0':
        print(0)
    else:
        if user_input[0] == 'x':
            first_product = int(get_power) * 1
        else:
            first_product = int(get_power) * int(user_input[0:user_input.index('x')])
        new_power = int(get_power) - 1
        print(f'{first_product}x^{new_power}')


# Provide a polynomial: 3x^-2
# -6x^-3
# Provide a polynomial: x^3
# 3x^2
# Provide a polynomial: 25x^20
# 500x^19
# Provide a polynomial: -5x^8
# -40x^7