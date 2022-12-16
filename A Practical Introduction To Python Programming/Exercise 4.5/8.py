# A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Write a program that asks the user for a year and prints
# out whether it is a leap year or not

user_input = float(input('Please, provide a year: '))
if user_input % 4 == 0:
    print(f'{int(user_input)} is a leap year.')
elif user_input % 100 == 0:
    if user_input % 400 == 0:
        print(f'{int(user_input)} is a lep year.')
else:
    print(f'{int(user_input)} is not a leap year.')

# Please, provide a year: 1998
# 1998 is not a leap year.
# Please, provide a year: 2000
# 2000 is a leap year.
