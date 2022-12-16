# Use a for loop to print an upside down triangle like the one below. Allow the user to specify
# how high the triangle should be.

height = int(input('Provide a height: '))

for count in range(height, 0, -1):
    print('*' * count)


# Provide a height: 5
# *****
# ****
# ***
# **
# *
# Provide a height: 11
# ***********
# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *
