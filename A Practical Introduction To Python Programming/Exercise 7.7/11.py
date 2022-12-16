# Using a for loop, create the list below, which consists of ones separated by increasingly many
# zeroes. The last two ones in the list should be separated by ten zeroes.
# [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]
sample_list = [1]

for diff in range(11):
    for zeros in range(diff):
        sample_list.append(0)
    sample_list.append(1)

print(sample_list)

# [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
# 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

