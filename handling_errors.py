# 'try-except' are used in handling programme errors in python
# 'try' signifies that we are trying to run a programme
try:
    user_age = int(input('Age: '))
    income_per_day = 20000
    number_of_hours = int(input('Provide number of working hours: '))
    print(user_age)
    income_per_hour = income_per_day / number_of_hours
    print(income_per_hour)
# 'except' tells python to run the indented code block if the specified type of error is encountered
except ZeroDivisionError:
    print('Number of working hours must not be 0')
except ValueError:
    print('Invalid Input')
# 'exit code 0' signifies that our programme ran successfully while 'exit code 1' signifies that our programme crashed

