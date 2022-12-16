# Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
# entries in the list that are greater than 10 with 10.

user_list = eval(input('Provide a list of 1 to 12: '))

for num in range(len(user_list)):
    if user_list[num] > 10:
        user_list[num] = 10

print(user_list)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]



