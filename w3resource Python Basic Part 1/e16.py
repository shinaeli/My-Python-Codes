def absolute_difference(num):
    if num < 17:
        return 17 - num
    else:
        return 2 * abs(17 - num)


print(absolute_difference(35))
# 36
print(absolute_difference(3))
# 14