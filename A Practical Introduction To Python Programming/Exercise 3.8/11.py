# Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound.

user_weight = int(input('Enter weight in kilograms: '))
pound_weight = user_weight * 2.205
print(round(pound_weight, -1))

# Enter weight in kilograms: 39
# 90.0
# Enter weight in kilograms: 71
# 160.0
