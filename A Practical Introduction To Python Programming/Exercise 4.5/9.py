# Write a program that asks the user to enter a number and prints out all the divisors of that number.

user_input = int(input('Provide a whole number: '))
for item in range(1, user_input+1):
    if user_input % item == 0:
        print(item)

# Provide a whole number: 24
# 1
# 2
# 3
# 4
# 6
# 8
# 12
# 24
# Provide a whole number: 39
# 1
# 3
# 13
# 39