def check_num(num):
    for count in range(100, 2100, 100):
        if count == num:
            return True
        else:
            return False


# print(check_num(50))
print(check_num(1300))