num1 = input('Provide first number: ')
num2 = input('Provide second number: ')

try:
    output = int(num1) + int(num2)
except ValueError:
    print('Please, provide a valid number.')
else:
    print(output)




