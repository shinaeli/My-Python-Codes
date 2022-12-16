# Write a program that asks the user for a number and then prints out the sine, cosine, and
# tangent of that number.
import math
from math import sin, cos, tan
user_input = int(input('Enter a whole number: '))
# 'math.radians()' method is used to convert an angle from degrees to radians
print(sin(math.radians(user_input)))
print(cos(math.radians(user_input)))
print(tan(math.radians(user_input)))

# Enter a whole number: 30
# 0.49999999999999994
# 0.8660254037844387
# 0.5773502691896257