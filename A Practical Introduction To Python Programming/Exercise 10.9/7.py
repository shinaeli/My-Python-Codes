# Write a program that creates the list [1,11,111,1111,...,111...1], where the entries
# have an ever increasing number of ones, with the last entry having 100 ones.

print(list(int('1' * num) for num in range(1, 101)))

# [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111, 11111111111, 111111111111, 1111111111111,
#  11111111111111, 111111111111111, 1111111111111111, 11111111111111111, 111111111111111111, 1111111111111111111,
#  11111111111111111111, 111111111111111111111, 1111111111111111111111, 11111111111111111111111,
#  111111111111111111111111, 1111111111111111111111111, 11111111111111111111111111, 111111111111111111111111111,
#  1111111111111111111111111111, 11111111111111111111111111111, 111111111111111111111111111111,
#  1111111111111111111111111111111, 11111111111111111111111111111111, 111111111111111111111111111111111,
#  1111111111111111111111111111111111, 11111111111111111111111111111111111, 111111111111111111111111111111111111,
#  1111111111111111111111111111111111111, 11111111111111111111111111111111111111,
#  111111111111111111111111111111111111111, 1111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111, 111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111, 11111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111, 1111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111, 111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111, 11111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111, 1111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111, 111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111, 11111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
#  1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111]