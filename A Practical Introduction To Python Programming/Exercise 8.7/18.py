# Write a program that creates a 10×10 list of random integers between 1 and 100. Then do the
# following:
# (a) Print the list.
# (b) Find the largest value in the third row.
# (c) Find the smallest value in the sixth column
from random import randint

arr = []
for outer in range(10):
    inner = []
    arr.append(inner)
    for item in range(10):
        new_number = randint(1, 100)
        inner.append(new_number)
print(arr)
print(max(arr[2]))
checker_arr = []
for out in range(len(arr)):
    checker_arr.append(arr[out][5])
print(min(checker_arr))

# [
# [62, 9, 81, 100, 28, 11, 53, 42, 34, 17],
# [69, 66, 70, 69, 12, 31, 73, 56, 86, 53],
# [44, 22, 8, 2, 33, 11, 16, 59, 86, 97],
# [3, 73, 38, 36, 83, 12, 67, 93, 16, 74],
# [98, 30, 4, 7, 36, 46, 100, 14, 99, 48],
# [95, 62, 19, 60, 64, 100, 79, 60, 21, 32],
# [12, 79, 34, 62, 76, 53, 89, 24, 70, 32],
# [75, 57, 81, 85, 48, 54, 60, 72, 25, 2],
# [54, 55, 52, 54, 39, 15, 63, 19, 25, 84],
# [21, 45, 76, 18, 5, 25, 62, 13, 91, 86]
# ]
# 97
# 11