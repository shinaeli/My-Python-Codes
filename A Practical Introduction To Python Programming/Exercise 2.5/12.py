# Use a for loop to print a triangle like the one below. Allow the user to specify how high the
# triangle should be.

height = int(input('Provide a height: '))

for count in range(1, height+1):
    print('*' * count)


# Provide a height: 5
# *
# **
# ***
# ****
# *****
# Provide a height: 10
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********