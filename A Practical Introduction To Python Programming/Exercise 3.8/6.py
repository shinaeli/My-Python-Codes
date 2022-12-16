# Write a program that asks the user to enter two numbers, x and y, and computes |x-y|/x+y.

x = int(input('Enter X: '))
y = int(input('Enter y: '))

absolute_value = abs(x-y)
sum = x + y
result = absolute_value / sum

print(result)
