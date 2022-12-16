# The following is useful in implementing computer players in a number of different games.
# Write a program that creates a 5 × 5 list consisting of zeroes and ones. Your program should
# then pick a random location in the list that contains a zero and change it to a one. If all the
# entries are one, the program should say so. [Hint: one way to do this is to create a new list
# whose items are the coordinates of all the ones in the list and use the choice method to
# randomly select one. Use a two-element list to represent a set of coordinates.]

arr = []
for outer in range(5):
    new_arr = []
    arr.append(new_arr)
    for inner in range(5):
        if (inner + outer + 1) % 2 == 0:
            new_arr.append(1)
        else:
            new_arr.append(0)

user_row = int(input('Enter a number from 1 to 5: '))
user_column = int(input('Enter a number from 1 to 5: '))

if arr[user_row - 1][user_column - 1] == 0:
    arr[user_row - 1][user_column - 1] = 1
    print(True)
else:
    print(False)

print(arr)