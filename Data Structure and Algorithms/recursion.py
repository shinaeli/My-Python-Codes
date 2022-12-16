def factorial(x):
    if x == 1 or 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(1500))
print(factorial(14))
print(factorial(1))
print(factorial(285))
print(factorial(0))
