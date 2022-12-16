# The following is useful as part of a program to play Battleship. Suppose you have a 5 × 5 list
# that consists of zeroes and ones. Ask the user to enter a row and a column. If the entry in the
# list at that row and column is a one, the program should print Hit and otherwise it should
# print Miss.

arr = []
for outer in range(5):
    new_arr = []
    arr.append(new_arr)
    for inner in range(5):
        if (inner + outer + 1) % 2 == 0:
            new_arr.append(1)
        else:
            new_arr.append(0)

user_row = int(input('Enter a row(from 1 to 5): '))
user_column = int(input('Enter a column(from 1 to 5): '))

if arr[user_row - 1][user_column - 1] == 1:
    print('Hit')
else:
    print('Miss')

# Enter a row(from 1 to 5): 3
# Enter a column(from 1 to 5): 2
# Hit

# Enter a row(from 1 to 5): 5
# Enter a column(from 1 to 5): 3
# Miss
