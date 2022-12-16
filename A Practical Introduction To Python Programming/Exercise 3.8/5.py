# Write a program that generates 50 random numbers such that the first number is between 1
# and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
# 1 and 51.

from random import randint

for item in range(2, 51):
    print(randint(1, item))