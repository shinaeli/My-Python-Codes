def find_max(num_list):
    if len(num_list) == 1:
        return num_list[0]
    elif len(num_list) == 0:
        return 'Invalid Input'
    else:
        maximum_num = num_list[0]
        for num in num_list:
            if num > maximum_num:
                maximum_num = num
        return maximum_num


print(find_max([18, 4])) #18
print(find_max([9, 26])) #26
print(find_max([6])) #6
print(find_max([])) #Invalid Input