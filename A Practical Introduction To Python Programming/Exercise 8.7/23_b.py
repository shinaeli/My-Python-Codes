# This exercise is useful in creating a Memory game. Randomly generate a 6 × 6 list of assorted
# characters such that there are exactly two of each character. An example is shown below.
# @ 5 # A A !
# 5 0 b @ $ z
# $ N x ! N z
# 0 - + # b :
# - : + c c x

from random import choice

item_arr = ['@', 5, '#', 'A', 'b', 'c', 'x', ':', '+', '-', 0, '$', 'N', '!', 'z']
arr = []
for outer in range(6):
    new_arr = []
    arr.append(new_arr)
    for inner in range(6):
        item = choice(item_arr)
        if item not in new_arr:
            new_arr.append(item)
        else:
            other_item = choice(item_arr)
            if (other_item != item) and (other_item not in new_arr):
                new_arr.append(other_item)

print(arr)

# [
# [0, 'A', '$', 'N', 'x', '@'],
# [5, 'N', ':', 'c', '$', 0],
# ['A', ':', 'b', 'x', '@', 0],
# ['!', 'z', 'x', '+', ':'],
# ['A', 'N', '-', '!', 5, '#'],
# ['!', 5, 0, '$', '#', 'N']
# ]