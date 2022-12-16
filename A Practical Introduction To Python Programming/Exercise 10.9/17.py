# Write a program that repeatedly asks the user to enter a height in the format feet’inches" (like
# 5'11" or 6'3". The user indicates they are done entering heights by entering done. The
# program should return a count of how many 4-footers, 5-footers, 6-footers, and 7-footers
# were entered

output_list, checkers = [], [4, 5, 6, 7]
while True:
    user_input = input('provide a height in the format(feet\'inches\"): ')
    if user_input == 'done':
        break
    else:
        feet_index = user_input.index("'")
        get_feet = user_input[0:feet_index]
        output_list.append(int(get_feet))

for item in checkers:
    print(f'{output_list.count(item)} "{item}-footers" were entered.')


# provide a height in the format(feet'inches"): 4'18"
# provide a height in the format(feet'inches"): 21'9"
# provide a height in the format(feet'inches"): 4'13.8"
# provide a height in the format(feet'inches"): 5'2"
# provide a height in the format(feet'inches"): 8'3.05"
# provide a height in the format(feet'inches"): 6'0"
# provide a height in the format(feet'inches"): 7'9"
# provide a height in the format(feet'inches"): 7'4.2"
# provide a height in the format(feet'inches"): 8'0.2"
# provide a height in the format(feet'inches"): 4'66"
# provide a height in the format(feet'inches"): 6'8"
# provide a height in the format(feet'inches"): done
# 3 "4-footers" were entered.
# 1 "5-footers" were entered.
# 2 "6-footers" were entered.
# 2 "7-footers" were entered.

