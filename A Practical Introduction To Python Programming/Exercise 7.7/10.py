# Write a program that rotates the elements of a list so that the element at the first index moves
# to the second index, the element in the second index moves to the third index, etc., and the
# element in the last index moves to the first index.

user_list = eval(input('Provide a list: '))
output_list = []

for num in range(len(user_list)):
    if num == len(user_list) - 1:
        output_list.insert(0, user_list[num])
    else:
        output_list.insert(num + 1, user_list[num])

print(output_list)

# Provide a list: ['olu', 'tope', 'MARYKAY', 419]
# [419, 'olu', 'tope', 'MARYKAY']
# Provide a list: [5, 3, 10, 46, 29]
# [29, 5, 3, 10, 46]