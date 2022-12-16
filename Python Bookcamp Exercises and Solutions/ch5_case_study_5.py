# Making a simple calculator
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
        '+': float(first_number) + float(second_number),
        '-': float(first_number) - float(second_number),
        '*': float(first_number) * float(second_number),
        '/': float(first_number) / float(second_number)
    }

    if (task in tasks.keys()) == False:
        print('Cannot compute the result')
    else:
        print(f'The final result is: {tasks[task]}.')
        break



# print(float('5.55'))

