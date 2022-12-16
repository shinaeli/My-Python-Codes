# Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in. Your program should convert the temperature to the other unit. The conversions
# are F =
# 9
# 5
# C + 32 and C =
# 5
# 9
# (F − 32).

user_input = int(input('Provide a temperature: '))
user_unit = input('C or F: ')
if user_unit == 'C' or user_unit == 'c':
    output = (1.8 * user_input) + 32
    print(f'{round(output, 2)} Fahrenheit')
elif user_unit == 'F' or user_unit == 'f':
    output = (5 * (user_input - 32)) / 9
    print(f'{round(output, 2)} Celsius')
else:
    print('Invalid unit!')


# Provide a temperature: 245
# C or F: F
# 118.33 Celsius
# Provide a temperature: 120
# C or F: c
# 248.0 Fahrenheit
# Provide a temperature: 150
# C or F: k
# Invalid unit!