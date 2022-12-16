#  Write a program that asks the user for an hour between 1 and 12 and for how many hours in
# the future they want to go. Print out what the hour will be that many hours into the future.
# An example is shown below.
# Enter hour: 8
# How many hours ahead? 5
# New hour: 1 o'clock

user_hour = int(input('Enter hour: '))
user_hour_ahead = int(input('How many hours ahead?: '))
output = (user_hour + user_hour_ahead) % 12

print(f"New hour: {output} o'clock")

# Enter hour: 6
# How many hours ahead?: 9
# New hour: 3 o'clock
# Enter hour: 8
# How many hours ahead?: 5
# New hour: 1 o'clock
