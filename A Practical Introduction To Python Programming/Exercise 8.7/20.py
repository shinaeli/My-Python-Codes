# Write a program that checks to see if a 4 × 4 list is a magic square. In a magic square, every
# row, column, and the two diagonals add up to the same value.

user_arr = eval(input('Provide a 4x4 matrix: '))
sum_column1, sum_column2, sum_column3, sum_column4 = 0, 0, 0, 0
sum_diagonal1, sum_diagonal2 = 0, 0
row_sum_arr_checker, output_arr = [], []
for outer in user_arr:
    sum_column1 += outer[0]
    sum_column2 += outer[1]
    sum_column3 += outer[2]
    sum_column4 += outer[3]
if sum_column1 == sum_column2 == sum_column3 == sum_column4:
    output_arr.append(True)
else:
    output_arr.append(False)
for outer in range(len(user_arr)):
    sum_row = 0
    for inner in range(len(user_arr[outer])):
        sum_row += user_arr[outer][inner]
    row_sum_arr_checker.append(sum_row)
for item in row_sum_arr_checker:
    if item != row_sum_arr_checker[0]:
        output_arr.append(False)
    else:
        output_arr.append(True)
for outer in range(len(user_arr)):
    for inner in range(len(user_arr[outer])):
        if outer == inner:
            sum_diagonal1 += user_arr[outer][inner]
        elif outer + inner == 3:
            sum_diagonal2 += user_arr[outer][inner]
if sum_diagonal1 == sum_diagonal2:
    output_arr.append(True)
else:
    output_arr.append(False)
# print(output_arr, row_sum_arr_checker)
if False in output_arr:
    print('The list provided is not a magic square.')
else:
    print('The list provided is a magic square.')


# Provide a 4x4 matrix: [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# The list provided is not a magic square.
# Provide a 4x4 matrix: [[1,15,14,4], [10,11,8,5], [7,6,9,12], [16,2,3,13]]
# The list provided is a magic square.
# Provide a 4x4 matrix: [[2,2,2,2], [2,2,2,2], [2,2,2,2], [2,2,2,2]]
# The list provided is a magic square.







