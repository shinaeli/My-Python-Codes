# Randomly generate a 6 × 6 list that has exactly 12 ones placed in random locations in the list.
# The rest of the entries should be zeroes.

from random import randint
# Create a 6x6 matrix of zeroes only
arr = []
for out in range(6):
    in_arr = []
    for inner in range(6):
        in_arr.insert(inner, 0)
    arr.append(in_arr)


counter = 1
while counter <= 12:
    # For each loop generate two random numbers from 0 to 5
    i, j = randint(0, 5), randint(0, 5)
    if arr[i][j] == 0:
        arr[i][j] = 1
        counter += 1
    else:
        continue

print(arr)

# [[0, 1, 1, 0, 1, 0],
# [0, 0, 1, 0, 1, 0],
# [0, 1, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0],
# [1, 0, 0, 1, 0, 1],
# [0, 0, 1, 0, 1, 0]]