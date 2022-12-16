user_list = input('Provide a comma-seperated list of numbers: ')
counter, real_list = 0, list(user_list)

for item in range(len(real_list)):
    if real_list[item] == 4:
        counter += 1
    else:
        continue

print(counter)