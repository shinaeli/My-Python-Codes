# Write a program that asks the user for a number of seconds and prints out how many minutes
# and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
# operator to get minutes and the % operator to get seconds.]

user_input = int(input('Enter the number of seconds: '))
minutes = user_input // 60
seconds_left = user_input % 60
output = f'{minutes} minutes and {seconds_left} seconds.'

print(output)

# Enter the number of seconds: 837
# 13 minutes and 57 seconds.
# Enter the number of seconds: 200
# 3 minutes and 20 seconds.
# Enter the number of seconds: 450
# 7 minutes and 30 seconds.