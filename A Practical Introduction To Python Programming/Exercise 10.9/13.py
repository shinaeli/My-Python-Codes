# The number 99 has the property that if we multiply its digits together and then add the sum
# of its digits to that, we get back to 99. That is, (9 × 9) + (9 + 9) = 99. Write a program to find
# all of the numbers less than 10000 with this property. (There are only nine of them.)

for i in range(1, 10001):
    str_num = str(i)
    times_end, sums_end = 1, 0
    if len(str_num) > 1:
        for item in str_num:
            times_end *= int(item)
            sums_end += int(item)
        grand_sum = times_end + sums_end
        if grand_sum == int(str_num):
            print(i)
        else:
            continue


# 19
# 29
# 39
# 49
# 59
# 69
# 79
# 89
# 99
