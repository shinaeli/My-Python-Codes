# Write a program to find all numbers between 1 and 1000 that are divisible by 7 and end in a
# 6.

# print(num if(num % 7 == 0 and str(num)[-1] == '6') for num in range(1, 1001))

for num in range(1, 1001):
    if num % 7 == 0 and str(num)[-1] == '6':
        print(num)

# 56
# 126
# 196
# 266
# 336
# 406
# 476
# 546
# 616
# 686
# 756
# 826
# 896
# 966
