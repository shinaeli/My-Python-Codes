# Write a program to determine how many of the numbers between 1 and 10000 contain the
# digit 3.

for num in range(1, 10001):
    if '3' in str(num):
        print(num)