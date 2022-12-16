# Write a program to determine how many zeroes 1000! ends with.

import math

counter = 0
output = str(math.factorial(1000))
for i in range(len(output) - 1, -1, -1):
    if output[i] == '0':
        counter += 1
    else:
        break

print(f'"1000!" ends with {counter} zeroes.')

#"1000!" ends with 249 zeroes.


