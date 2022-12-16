# Write a program that generates a list of 20 random numbers between 1 and 100.
# (a) Print the list.
# (b) Print the average of the elements in the list.
# (c) Print the largest and smallest values in the list.
# (d) Print the second largest and second smallest entries in the list
# (e) Print how many even numbers are in the list.

from random import randint
outputArr = []

for count in range(20):
    outputArr.append(randint(1, 100))
    # outputArr[count] = randint(1, 100)
    # outputArr.insert(count, randint(1, 100))

average = sum(outputArr) / len(outputArr)
print(f'The average is {average}.')

print(f'The largest is {max(outputArr)}.')
print(f'The smallest is {min(outputArr)}.')

outputArr.sort()
print(f'The second smallest number is {outputArr[1]}.')
print(f'The second largest number is {outputArr[len(outputArr) - 2]}.')

counter = 0
for item in outputArr:
    if item % 2 == 0:
        counter += 1
    else:
        counter += 0

print(f'There are {counter} even numbers in the list.')

# The average is 38.4.
# The largest is 93
# The smallest is 4
# The second smallest number is 8.
# The second largest number is 89.
# There are 8 even numbers in the list.
