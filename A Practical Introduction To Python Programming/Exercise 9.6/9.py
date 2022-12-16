# A 4000-year old method to compute the square root of 5 is as follows: Start with an initial
# guess, say 1. Then compute
# 1 +
# 5
# 1
# 2
# = 3.
# Next, take that 3 and replace the 1’s in the previous formula with 3’s . This gives
# 3 +
# 5
# 3
# 2
# = 7/3 ≈ 2.33.
# Next replace the 3 in the previous formula with 7/3. This gives
# 7/3 +
# 5
# 7/3
# 2
# =
# 47
# 21
# ≈ 2.24.
# If you keep doing this process of computing the formula, getting a result, and plugging it back
# in, the values will eventually get closer and closer to p
# 5. This method works for numbers
# other than 5. Write a program that asks the user for a number and uses this method to estimate
# the square root of the number correct to within 10−10. The estimate will be correct to within
# 10−10 when the absolute value of the difference between consecutive values is less than 10−10
# .

user_num = int(input('enter a number: '))
div = 1
while True:
    result = (div + (user_num / div)) / 2
    if abs(div - result) <= 1e-10:
        print(result)
        break
    div = result

# enter a number: 14
# 3.7416573867739413
# enter a number: 99
# 9.9498743710662
# enter a number: 38
# 6.164414002968977
# enter a number: 5
# 2.23606797749979






