# Write a program to test if a number is within 100 of 1000 or 2000

def near_thousand(num):
    return ((abs(1000 - num) <= 1000) or (abs(2000 - num) <= 100))


print(near_thousand(1000))
# True
print(near_thousand(900))
# True
print(near_thousand(800))
# False
print(near_thousand(2200))
# False