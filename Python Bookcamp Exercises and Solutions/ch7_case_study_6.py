# Making a simple calculator

from calculator_operations import addition, subtraction, multiplication, division

while True:
    print('*' * 40)
    print('''
    This is a simple calculator.
    It supports the following operations:
    i.) Addition
    ii.) Subtraction
    iii.) Multiplication and
    iv.) Division
    ''')
    print('*' * 40)

    first_number = input('Enter the first number: ')
    second_number = input('Enter the second number: ')
    task = input('Enter an operator(+,-,*,/): ')

    tasks = {
        '+': addition.add(first_number, second_number),
        '-': subtraction.subtract(first_number, second_number),
        '*': multiplication.multiply(first_number, second_number),
        '/': division.divide(first_number, second_number)
    }

    if (task in tasks.keys()) == False:
        print('Invalid operator.')
    elif type(tasks[task]) == float:
        print(f'The final result is: {tasks[task]}.')
        break
    else:
        print(tasks[task])




# print(type(55.3) == float)
