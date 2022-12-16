# Write a program that finds the average of all of the entries in a 4 × 4 list of integers

user_input = eval(input('Provide a 4x4 matrix: '))
count, total = 0, 0

for outer in range(len(user_input)):
    for inner in range(len(user_input[outer])):
        count += 1
        total += user_input[outer][inner]
print(f'The average of {user_input} is {total / count}.')

# Provide a 4x4 matrix: [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# The average of [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]] is 8.5.




