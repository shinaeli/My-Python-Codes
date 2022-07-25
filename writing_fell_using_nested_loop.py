nums_list = [[5,1,5,1,1], [5,1,5,1,5], [1,1,1,1,5], [1,1,1,1,5]]

for nums in nums_list:
    result = ''
    for num in nums:
        output = ''
        for count in range(num):
            output += 'x'
        print(output)
    print(result)