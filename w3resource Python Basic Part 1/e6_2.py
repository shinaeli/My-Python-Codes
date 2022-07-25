user_list = input('Provide a list of items: ')

# 'split' method is used to change a string into a list
# It returns a standard python list
# Its argument is used as a seperator marker i.e. what is used to mark-out each item to make the list
# It accepts another optional argument called 'max_split'
# 'max_split' indicates the maximum number of item that the list must contain
# The maximum number of items in the list is simply the sum of the 'max_split' plus one
splitted_user_list = user_list.split(", ")

print(tuple(splitted_user_list))
print(splitted_user_list)





# James, 15, Fredrick, 20, True, 48, 95, Ferrari