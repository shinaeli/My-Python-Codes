# Randomly generate a 9 × 9 list where the entries are integers between 1 and 9 with no repeat
# entries in any row or in any column.

from random import shuffle, randint

# arr = []
#
# for out in range(9):
#     in_arr = []
#     for inner in range(9):
#         picked = randint(1, 9)
#         if inner == 0:
#             in_arr.append(picked)
#         elif inner > 0 and picked not in in_arr:
#             in_arr.append(picked)
#         else:
#             re_picked = randint(1, 9)
#             if re_picked not in in_arr:
#                 in_arr.append(re_picked)
#     arr.append(in_arr)
#
# print(arr)

arr = []

for out in range(9):
    in_arr = []
    for inner in range(1,10):
        in_arr.append(inner)
    arr.append(in_arr)

i = 0
while i < len(arr):
    shuffle(arr[i])
    i += 1

print(arr)

