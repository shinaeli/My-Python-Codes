# Write a program that uses list and range to create the list [3,6, 9, . . . , 99].

print(list(num for num in range(3, 100, 3)))
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87,
# 90, 93, 96, 99]

# OR

arr = []
for num in range(3, 100, 3):
    arr.append(num)

print(arr)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87,
# 90, 93, 96, 99]

