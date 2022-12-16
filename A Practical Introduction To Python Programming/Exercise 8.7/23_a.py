# This exercise is useful in creating a Memory game. Randomly generate a 6 × 6 list of assorted
# characters such that there are exactly two of each character. An example is shown below.
# @ 5 # A A !
# 5 0 b @ $ z
# $ N x ! N z
# 0 - + # b :
# - : + c c x

from random import sample

item_arr = ['@', 5, '#', 'A', 'b', 'c', 'x', ':', '+', '-', 0, '$', 'N', '!', 'z']
arr = []
for outer in range(6):
    random_items = sample(item_arr, 6)
    arr.append(random_items)

print(arr)

# [
# ['N', '+', 'x', '!', '@', '$'],
# [5, 'b', '#', 'c', 'z', '+'],
# ['$', '#', '@', 'c', 'x', '-'],
# ['+', 'x', 5, 'c', ':', 'z'],
# ['@', '-', '+', 'z', 5, ':'],
# [5, '-', 'z', '@', '$', '#']
# ]



