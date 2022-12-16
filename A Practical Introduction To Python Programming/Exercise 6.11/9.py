# Ask the user for a number and then print the following, where the pattern ends at the number
# that the user enters.
#  1
#   2
#    3
#     4

user_input = int(input('Provide a number of your choice: '))

spacer = 0
for count in range(user_input):
    spacer += 1
    count += 1
    print((' ' * spacer)+str(count))



# Provide a number of your choice: 10
#  1
#   2
#    3
#     4
#      5
#       6
#        7
#         8
#          9
#           10



