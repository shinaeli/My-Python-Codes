# Write a program that generates 100 random integers that are either 0 or 1. Then find the
# longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
# zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

from random import randint

output_list = []

for count in range(100):
    output_list.append(randint(0, 1))

print(output_list)
