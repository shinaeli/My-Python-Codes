# Write a program that repeatedly asks the user to enter a birthday in the format month/day
# (like 12/25 or 2/14). The user indicates they are done entering birthdays by entering done.
# The program should return a count of how many of those birthdays are in February and how
# many are on the 25th of some month (any month).

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
month_list, day_list = [], []

while True:
    user_input = input('provide a date in the format("mm/dy"): ')
    if user_input == 'done':
        break
    else:
        get_index = user_input.index('/')
        get_month = user_input[0:get_index]
        get_day = user_input[get_index + 1:]
        month_list.append(int(get_month))
        day_list.append(int(get_day))

print(f'{month_list.count(months.index("feb") + 1)} of the provided birthdays are in February.')
print(f'{day_list.count(25)} of the provided birthdays are on the 25th.')

# provide a date in the format("mm/dy"): 1/6
# provide a date in the format("mm/dy"): 2/25
# provide a date in the format("mm/dy"): 9/17
# provide a date in the format("mm/dy"): 6/26
# provide a date in the format("mm/dy"): 8/2
# provide a date in the format("mm/dy"): 2/15
# provide a date in the format("mm/dy"): 3/25
# provide a date in the format("mm/dy"): 2/9
# provide a date in the format("mm/dy"): 7/30
# provide a date in the format("mm/dy"): 8/25
# provide a date in the format("mm/dy"): 2/10
# provide a date in the format("mm/dy"): 10/25
# provide a date in the format("mm/dy"): 2/2
# provide a date in the format("mm/dy"): done
# 5 of the provided birthdays are in February.
# 4 of the provided birthdays are on the 25th.
