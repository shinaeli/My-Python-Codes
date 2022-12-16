# Write a program that finds all pairs of six-digit palindromic numbers that are less than 20
# apart. One such pair is 199991 and 200002


new_num = 0
for num in range(100000, 300000):
    if str(num) == str(num)[::-1]:
        if num - new_num < 20:
            print(num, new_num)
            break
        else:
            new_num = num

# 200002 199991

