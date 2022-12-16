# Write a program that creates and prints an 8 × 8 list whose entries alternate between 1 and 2
# in a checkerboard pattern, starting with 1 in the upper left corner

arr = []
for outer in range(8):
    new_arr = []
    arr.append(new_arr)
    for inner in range(8):
        if (inner + outer + 1) % 2 == 0:
            new_arr.append(2)
        else:
            new_arr.append(1)
print(arr)
# [
#     [1, 2, 1, 2, 1, 2, 1, 2],
#     [2, 1, 2, 1, 2, 1, 2, 1],
#     [1, 2, 1, 2, 1, 2, 1, 2],
#     [2, 1, 2, 1, 2, 1, 2, 1],
#     [1, 2, 1, 2, 1, 2, 1, 2],
#     [2, 1, 2, 1, 2, 1, 2, 1],
#     [1, 2, 1, 2, 1, 2, 1, 2],
#     [2, 1, 2, 1, 2, 1, 2, 1]
# ]