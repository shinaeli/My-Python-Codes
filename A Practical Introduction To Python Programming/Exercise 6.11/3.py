# People often forget closing parentheses when entering formulas. Write a program that asks
# the user to enter a formula and prints out whether the formula has the same number of opening and closing parentheses

user_input = input('Provide a formula: ')
count_open, count_close = 0, 0
for each in user_input:
    if each == '(':
        count_open += 1
    elif each == ')':
        count_close += 1
if count_open == count_close:
    print('The formula has the same number of opening and closing parenthesis.')
else:
    print('The formula does not have equal number of opening and closing parenthesis.')