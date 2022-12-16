# (a) One way to find out the last digit of a number is to mod the number by 10. Write a
# program that asks the user to enter a power. Then find the last digit of 2 raised to that
# power.
user_power = int(input('Enter a power: '))
calc_index = 2 ** user_power
last_digit = calc_index % 10
print(last_digit)

# (b) One way to find out the last two digits of a number is to mod the number by 100. Write
# a program that asks the user to enter a power. Then find the last two digits of 2 raised to
# that power.
user_power = int(input('Enter a power: '))
calc_index = 2 ** user_power
last_digit = calc_index % 100
print(last_digit)

# (c) Write a program that asks the user to enter a power and how many digits they want.
# Find the last that many digits of 2 raised to the power the user entered.
user_power = int(input('Enter a power: '))
no_of_digits = int(input('Enter the number of digit: '))
calc_index = 2 ** user_power
power_of_ten = 10 ** no_of_digits
last_digit = calc_index % power_of_ten
print(last_digit)




