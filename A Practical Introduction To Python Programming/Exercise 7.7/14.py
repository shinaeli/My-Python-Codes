# Write a program that asks the user to enter a length in feet. The program should then give
# the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
# meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
# enter a 2, then the program converts to yards, etc. While this can be done with if statements,
# it is much shorter with lists and it is also easier to add new conversions if you use lists.

question = float(input('Provide a length in feet: '))
user_option = int(input('Enter an option from 1 to 7: '))
options = ['inches', 'yards', 'miles', 'millimeters', 'centimeters', 'meters', 'kilometers']
result = 0
if 1 <= user_option <= 7:
    if options[user_option - 1] == 'inches':
        result = question * 12
    elif options[user_option - 1] == 'yards':
        result = question * 0.333
    elif options[user_option - 1] == 'miles':
        result = question * 0.000189
    elif options[user_option - 1] == 'millimeters':
        result = question * 304.8
    elif options[user_option - 1] == 'centimeters':
        result = question * 30.48
    elif options[user_option - 1] == 'meters':
        result = question * 0.30
    elif options[user_option - 1] == 'kilometers':
        result = question * 0.000305
    print(f'{question}feet is {result}{options[user_option - 1]}.')
else:
    print('Wrong Input!')

# Provide a length in feet: 15
# Enter an option from 1 to 7: 4
# 15feet is 4572.0millimeters.

# Provide a length in feet: 23.96
# Enter an option from 1 to 7: 2
# 23.96feet is 7.978680000000001yards.

# Provide a length in feet: 5.805
# Enter an option from 1 to 7: 8
# Wrong Input!



