# Let L be a list of strings. Write list comprehensions that create new lists from L for each of the
# following.
# (a) A list that consists of the strings of s with their first characters removed
# (b) A list of the lengths of the strings of s
# (c) A list that consists of only those strings of s that are at least three characters long

L = eval(input('Provide a list of strings: '))
s = [x[1:] for x in L]
print(s)

# Provide a list of strings: ['goat', 'cow', 'mouse', 'factorial', 'politicians']
# ['oat', 'ow', 'ouse', 'actorial', 'oliticians']

lengths = [len(y) for y in L]
print(lengths)

# Provide a list of strings: ['goat', 'cow', 'mouse', 'factorial', 'politicians']
# [4, 3, 5, 9, 11]

lengthers = [p for p in L if len(p) >= 3]
print(lengthers)

# Provide a list of strings: ['goat', 'cow', 'mouse', 'factorial', 'politicians']
# ['goat', 'cow', 'mouse', 'factorial', 'politicians']