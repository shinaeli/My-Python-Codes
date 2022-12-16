# Write a program that removes any repeated items from a list so that each item appears at most
# once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

user_list = eval(input('Provide a list of your choice: '))

output_list = []

for item in user_list:
    if item in output_list:
        continue
    else:
        output_list.append(item)

print(output_list)

# Provide a list of your choice: ['mAry', 'fredrick', 'goke', 'mAry', 'mAry', 'goke', 'tobi', 'fredrick', 'mAry', 'george', 'tobi']
# ['mAry', 'fredrick', 'goke', 'tobi', 'george']

# Provide a list of your choice: [1,1,2,3,4,3,0,0]
# [1, 2, 3, 4, 0]

# Provide a list of your choice: [10, 25, 209, 150, 75]
# [10, 25, 209, 150, 75]




