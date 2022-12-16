# Write a program that asks the user to enter an angle in degrees and prints out the sine of that
# angle.

import math
from math import sin
user_input = int(input('Enter an angle in degrees: '))
print(sin(math.radians(user_input)))

# Enter an angle in degrees: 45
# 0.7071067811865476
# Enter an angle in degrees: 26
# 0.4383711467890774

