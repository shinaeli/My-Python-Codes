# Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦
# in
# 15◦
# increments. Each result should be rounded to 4 decimal places. Sample output is shown
# below:
# 0 --- 0.0 1.0
# 15 --- 0.2588 0.9659
# 30 --- 0.5 0.866
# ...
# 345 --- -0.2588 0.9659
import math
from math import sin, cos
for item in range(0, 346, 15):
    print(f'{item} --- {round(sin(math.radians(item)), 4)} {round(cos(math.radians(item)), 4)}')

# 0 --- 0.0 1.0
# 15 --- 0.2588 0.9659
# 30 --- 0.5 0.866
# 45 --- 0.7071 0.7071
# 60 --- 0.866 0.5
# 75 --- 0.9659 0.2588
# 90 --- 1.0 0.0
# 105 --- 0.9659 -0.2588
# 120 --- 0.866 -0.5
# 135 --- 0.7071 -0.7071
# 150 --- 0.5 -0.866
# 165 --- 0.2588 -0.9659
# 180 --- 0.0 -1.0
# 195 --- -0.2588 -0.9659
# 210 --- -0.5 -0.866
# 225 --- -0.7071 -0.7071
# 240 --- -0.866 -0.5
# 255 --- -0.9659 -0.2588
# 270 --- -1.0 -0.0
# 285 --- -0.9659 0.2588
# 300 --- -0.866 0.5
# 315 --- -0.7071 0.7071
# 330 --- -0.5 0.866
# 345 --- -0.2588 0.9659
