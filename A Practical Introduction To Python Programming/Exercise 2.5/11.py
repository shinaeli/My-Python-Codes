# Use a for loop to print a box like the one below. Allow the user to specify how wide and how
# high the box should be.


width = int(input('Provide a width: '))
height = int(input('Provide a height: '))

for count in range(1, height + 1):
    spacer = ' ' * (width-2)
    if count == 1 or count == height:
        print('*' * width)
    else:
        print(f"*{spacer}*")


# Provide a width: 20
# Provide a height: 4
# ********************
# *                  *
# *                  *
# ********************

