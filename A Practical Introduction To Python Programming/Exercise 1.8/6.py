# Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
# and 5x, each separated by three dashes, like below.
# Enter a number: 7
# 7---14---21---28---35

user_input = int(input('Enter a number: '))
output = ''
for i in range(1, 6):
    if i == 1:
        output += (f'{i * user_input}')
    else:
        output += ('---'+f'{i * user_input}')
print(output)

# Enter a number: 7
# 7---14---21---28---35
# Enter a number: 5
# 5---10---15---20---25
# Enter a number: 19
# 19---38---57---76---95
# Enter a number: 43
# 43---86---129---172---215
