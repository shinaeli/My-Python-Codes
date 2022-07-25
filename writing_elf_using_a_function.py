def letter(nums_list):
    for num in nums_list:
        output = ''
        for count in range(num):
            output += 'x'
        print(output)
    print(' ')


letter([5,1,5,1,5])
letter([1,1,1,1,5])
letter([5,1,5,1,1])















