import datetime

# 'datetime' module supplies classes for manipulating dates and time in both simple and complex ways
now = datetime.datetime.now()
# 'datetime.now(tz=None)' returns the current local date and time
# If 'tz' is 'None' or not specified, this is like today.
print('Current date and time: ')
# 'date.strftime(format)' returns a string representing the date, controlled by an explicit format string
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Current date and time:
# 2022-07-21 20:14:21