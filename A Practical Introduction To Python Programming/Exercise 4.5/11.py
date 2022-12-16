# Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
# and asks them how many hours into the future they want to go. Print out what the hour will
# be that many hours into the future, printing am or pm as appropriate. An example is shown
# below.
# Enter hour: 8
# am (1) or pm (2)? 1
# How many hours ahead? 5
# New hour: 1 pm

user_time = int(input('Enter hour: '))
am_pm = input('am or pm? ')
future_hours = int(input('How many hours ahead? '))

updated_hour = user_time + future_hours
new_current_hour = updated_hour % 12
if am_pm == 'am' and updated_hour >= 12:
    print(f'New hour: {new_current_hour} pm')
elif am_pm == 'am' and updated_hour < 12:
    print(f'New hour: {future_hours + user_time} am')
elif am_pm == 'pm' and updated_hour >= 12:
    print(f'New hour: {new_current_hour} am')
else:
    print(f'New hour: {future_hours + user_time} pm')

