numbers_list = [12, 83, 20, 8, 7, 65, 9]
# Iterate through the 'numbers_list' list
for num in numbers_list:
    # Assume the first item in the 'numbers_list' is the largest number and call it 'max'
    max = numbers_list[0]
    # Iterate again through the 'numbers_list'
    for check in numbers_list:
        # For each iteration, check if the current item in 'numbers_list' is greater than 'max'
        if check > max:
            # If true, assign the current item as max(the newly found largest number)
            max = check
# Print max to the console
print(max) #83