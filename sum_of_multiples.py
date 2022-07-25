def sum_of_multiples(limit):
    output = []
    total = 0
    for count in range(1, limit+1):
        if (count % 3 == 0 and count % 5 == 0) or count % 3 == 0 or count % 5 == 0:
            output.append(count)
    print(output)
    for item in output:
        total += item
    print(total)


sum_of_multiples(20)
# [3, 5, 6, 9, 10, 12, 15, 18, 20]
# 98
sum_of_multiples(49)
# [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48]
# 543