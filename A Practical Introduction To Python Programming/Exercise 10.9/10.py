# Adding certain numbers to their reversals sometimes produces a palindromic number. For
# instance, 241 + 142 = 383. Sometimes, we have to repeat the process. For instance, 84 + 48 =
# 132 and 132 + 231 = 363. Write a program that finds both two-digit numbers for which this
# process must be repeated more than 20 times to obtain a palindromic number.

for i in range(11, 100):
    num = i
    for count in range(1000):
        num = num + int(str(num)[::-1])
        if str(num) == str(num[::-1]):
            if count > 20:
                print(num, count)
            break

