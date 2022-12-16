# Write a program that generates a random number, x, between 1 and 50, a random number y
# between 2 and 5, and computes x^y.

from random import randint

base = randint(1, 50)
power = randint(2, 5)

print(base ** power)
