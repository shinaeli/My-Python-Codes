# Write a program that asks the user for an integer and creates a list that consists of the factors
# of that integer.

user_input = input('Provide an integer: ')
query = int(user_input)
output_list = []

for num in range(1, query + 1):
    if query % num == 0:
        output_list.append(num)

print(output_list)

# Provide an integer: 6
# [1, 2, 3, 6]
# Provide an integer: 13
# [1, 13]
