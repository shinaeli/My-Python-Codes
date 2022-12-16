# The GCD (greatest common divisor) of two numbers is the largest number that both are divisible by. For instance,
# gcd(18, 42) is 6 because the largest number that both 18 and 42 are
# divisible by is 6. Write a program that asks the user for two numbers and computes their gcd.
# Shown below is a way to compute the GCD, called Euclid’s Algorithm.
# • First compute the remainder of dividing the larger number by the smaller number
# • Next, replace the larger number with the smaller number and the smaller number with
# the remainder.
# • Repeat this process until the smaller number is 0. The GCD is the last value of the larger
# number.

import math

num1 = int(input('provide first number: '))
num2 = int(input('provide second number: '))

print(f'The GCD of {num1} and {num2} is {math.gcd(num1, num2)}.')

# provide first number: 18
# provide second number: 42
# The GCD of 18 and 42 is 6.
