while True:

    num1 = input('Provide first number: ')
    num2 = input('Provide second number: ')

    try:
        output = int(num1) + int(num2)
    except ValueError:
        # The code fails silently after the 'ValueError' exception object
        pass
    else:
        # The 'else' lock execute successfully only if the 'try' block executes successfully
        print(output)




