# Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
output_list, squares_list, words_list = [], [], []

for count in range(50):
    output_list.append(count)

print(output_list)

for num in range(1, 51):
    squares_list.append(num ** 2)

print(squares_list)

for num in range(len(letters_list)):
    words_list.append(letters_list[num] * (num + 1))

print(words_list)


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
# 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676,
# 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116,
# 2209, 2304, 2401, 2500]
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg', 'hhhhhhhh', 'iiiiiiiii', 'jjjjjjjjjj', 'kkkkkkkkkkk',
#  'llllllllllll', 'mmmmmmmmmmmmm', 'nnnnnnnnnnnnnn', 'ooooooooooooooo', 'pppppppppppppppp', 'qqqqqqqqqqqqqqqqq',
#  'rrrrrrrrrrrrrrrrrr', 'sssssssssssssssssss', 'tttttttttttttttttttt', 'uuuuuuuuuuuuuuuuuuuuu',
#  'vvvvvvvvvvvvvvvvvvvvvv', 'wwwwwwwwwwwwwwwwwwwwwww', 'xxxxxxxxxxxxxxxxxxxxxxxx',
#  'yyyyyyyyyyyyyyyyyyyyyyyyy', 'zzzzzzzzzzzzzzzzzzzzzzzzzz']