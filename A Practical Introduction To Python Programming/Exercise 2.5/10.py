# Use a for loop to print a box like the one below. Allow the user to specify how wide and how
# high the box should be. [Hint: print('*'*10) prints ten asterisks.]

width = int(input('Provide a width: '))
height = int(input('Provide a height: '))

for count in range(height):
    print('*' * width)


# Provide a width: 20
# Provide a height: 10
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
# Provide a width: 5
# Provide a height: 5
# *****
# *****
# *****
# *****
# *****

