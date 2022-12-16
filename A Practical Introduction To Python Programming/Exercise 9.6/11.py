# Write a program that starts with an 5 × 5 list of zeroes and randomly changes exactly ten of
# those zeroes to ones.

from random import randint

out_arr = []
for count in range(5):
    in_arr = []
    for counter in range(5):
        in_arr.append(0)
    out_arr.append(in_arr)
print(out_arr) # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

looper = 1
while looper <= 10:
    out_index = randint(0, 4)
    in_index = randint(0, 4)
    out_arr[out_index][in_index] = 1
    looper += 1

print(out_arr)

# [[1, 1, 1, 0, 1], [1, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [1, 1, 0, 0, 0]]
# [[1, 0, 1, 1, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [1, 0, 1, 1, 0], [0, 0, 0, 1, 0]]
# [[0, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 1, 1], [0, 1, 0, 1, 0]]








