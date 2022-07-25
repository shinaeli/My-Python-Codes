course = 'Python for Beginners'
# 'len' method is used to determine the total amount of characters in a string
print(len(course)) #20
# 'find' method is used to find the index of the first occurence of the passed argument
# if the argument passed to the 'find' method doesn't exist in the string, '-1' is returned
print(course.find('h')) #3
print(course.find('for')) #7
print(course.find('k')) #-1
#  'upper' method converts all the characters present in the string to uppercase
print(course.upper()) #PYTHON FOR BEGINNERS
#  'lower' method converts all the characters present in the string to lowercase
print(course.lower()) #python for beginners
print(course) #Python for Beginners
# 'replace' is used to replace a character in a string with another character
print(course.replace('Beginners', 'Absolute Beginners')) #Python for Absolute Beginners
print(course) #Python for Beginners
# 'in' is used to check if a given character exists in a string
# 'in' returns a boolean
print('JavaScript' in course) #False
print('Python' in course) #True

