# A program that prints the calendar of any given month
import calendar

while True:
    print('Enter "q" to quit.')
    y = input('Input the year: ')
    if y == 'q':
        break
    else:
        converted_year = int(y)
    print('Enter "q" to quit.')
    m = input('Input the month: ')
    if m == 'q':
        break
    else:
        converted_month = int(m)

    print(calendar.month(converted_year, converted_month))