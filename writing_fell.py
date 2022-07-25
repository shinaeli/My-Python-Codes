# multi1 = '''
# '''
# str = 'Oluwaseyi.'
# str2 = 'Thursday'
# multi12 = '''
# '''
# multi1 += str
# multi1 += multi12
# multi1 += str2
# print(multi1)

nums_list = [[5,1,5,1,1], [5,1,5,1,5], [1,1,1,1,5], [1,1,1,1,5]]

for nums in nums_list:
    result = '''
'''
    for num in nums:
        output = ''
        for count in range(num):
            output += 'x'
        result += output
        result += result
    result += ' '
    result += ' '
    result += ' '
    print(result)


# xxxxx    xxxxx    x        x
# x        x        x        x
# xxxxx    xxxxx    x        x
# x        x        x        x
# x        xxxxx    xxxxx    xxxxx

