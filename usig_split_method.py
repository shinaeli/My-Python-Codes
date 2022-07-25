sample_string = 'Today is a good day.'

print(sample_string.split(' '))
# ['Today', 'is', 'a', 'good', 'day.']

sample_string2 = 'Joy, Amaka, 54, False, 9, 26, Deji'

print(sample_string2.split(', '))
# ['Joy', 'Amaka', '54', 'False', '9', '26', 'Deji']

print(sample_string2.split(',', 2))
# ['Joy', ' Amaka', ' 54, False, 9, 26, Deji']
# ['Joy', ' Amaka', ' 54, False, 9, 26, Deji']


