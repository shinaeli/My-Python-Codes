# Write a program that estimates the average number of drawings it takes before the user’s
# numbers are picked in a lottery that consists of correctly picking six different numbers that
# are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of
# user numbers and simulates drawings until the user’s numbers are drawn. Find the average
# number of drawings needed over the 1000 times the loop runs.

from random import sample

correct_nums = '2 6 5 1 9 3'
counter = 0
for count in range(1001):
    counter += 1
    num_list = [str(num + 1) for num in range(0, 9)]
    output_list = sample(num_list, 6)
    outcome = ' '.join(output_list)
    if outcome == correct_nums:
        print('You won!')
        print(f'Your average number of drawing is {counter}.')
        break
    else:
        print('Retry')


