names = ['Fred', 'Oluwaseyi', 'Temitope', 'Sola', 'Ayodeji', 'Toyin', 'Dorcas']
for name in names:
    print(name)
# Fred
# Oluwaseyi
# Temitope
# Sola
# Ayodeji
# Toyin
# Dorcas
# 'len' is used to determine the total number of items in a list
print(len(names)) #7
# 'append' is used to add a new item to the list
names.append('Carolina') #['Fred', 'Oluwaseyi', 'Temitope', 'Sola', 'Ayodeji', 'Toyin', 'Dorcas', 'Carolina']
print(names) #['Fred', 'Oluwaseyi', 'Temitope', 'Sola', 'Ayodeji', 'Toyin', 'Dorcas', 'Carolina']
print(len(names)) #8
# 'insert' is used to add a new item to the list at a specified index
names.insert(3, 'Tomiwa')
print(names) #['Fred', 'Oluwaseyi', 'Temitope', 'Tomiwa', 'Sola', 'Ayodeji', 'Toyin', 'Dorcas', 'Carolina']
print(len(names)) #9
# 'in' is used to check if an item exists in a list
# 'in' returns a boolean value
print('Tayo' in names) #False
print('Oluwaseyi' in names) #True
names[len(names)-1] = 'Carol'
print(names) #['Fred', 'Oluwaseyi', 'Temitope', 'Tomiwa', 'Sola', 'Ayodeji', 'Toyin', 'Dorcas', 'Carol']
names[-3] = 'Wumi'
print(names)
names.insert(-4, 'Toyin')
print(names) #['Fred', 'Oluwaseyi', 'Temitope', 'Tomiwa', 'Sola', 'Toyin', 'Ayodeji', 'Wumi', 'Dorcas', 'Carol']
# Iterating through a section of the list 'names'
for title in names[2:6]:
    print(title)
# Temitope
# Tomiwa
# Sola
# Toyin
names.append('Temitope')
print(names) #['Fred', 'Oluwaseyi', 'Temitope', 'Tomiwa', 'Sola',
# 'Toyin', 'Ayodeji', 'Wumi', 'Dorcas', 'Carol', 'Temitope']
print(names.count('Temitope')) #2
# 'copy' is used to make a copy of a list
# the newly created copy doesn't get mutated if the original list gets mutated
student_names = names.copy()
print(student_names) #['Fred', 'Oluwaseyi', 'Temitope', 'Tomiwa', 'Sola',
# 'Toyin', 'Ayodeji', 'Wumi', 'Dorcas', 'Carol', 'Temitope']
names.append('Oluwafisayomi')
print(student_names) #['Fred', 'Oluwaseyi', 'Temitope', 'Tomiwa', 'Sola', 'Toyin',
# 'Ayodeji', 'Wumi', 'Dorcas', 'Carol', 'Temitope']
print(names) #['Fred', 'Oluwaseyi', 'Temitope', 'Tomiwa', 'Sola', 'Toyin',
# 'Ayodeji', 'Wumi', 'Dorcas', 'Carol', 'Temitope', 'Oluwafisayomi']



