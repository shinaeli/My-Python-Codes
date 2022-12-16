# Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.

output = ''
for num in range(8, 92, 3):
    if num == 89:
        output += f'{num}.'
    else:
        output += f'{num}, '
print(output)

# 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89.