# A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
# determine how many leap years there have been between 1600 and that year.

user_input = int(input('Enter a year of your choice: '))
count = 0
for year in range(1600, user_input+1):
    if year % 4 == 0:
        count += 1
    elif year % 100 == 0 and year % 400 == 0:
        count += 1
print(count)

# Enter a year of your choice: 2022
# 106
# Enter a year of your choice: 2200
# 151
# Enter a year of your choice: 1923
# 81







