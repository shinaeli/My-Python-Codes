def count_4s(user_list):
    counter = 0

    for item in range(len(user_list)):
        if user_list[item] == 4:
            counter += 1
        else:
            continue

    return counter


call1 = count_4s([12, 4, 5, 8, 4, 3, 9, 4, 17, 35, 88, 4, 26])
print(call1) #4
call2 = count_4s([12, 5, 8, 3, 9, 17, 35, 88, 26])
print(call2) #0