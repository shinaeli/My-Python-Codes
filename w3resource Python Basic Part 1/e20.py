user_input, counter = input('Provide a string: '), 0

for char in range(len(user_input)):
    if user_input[char] == ' ':
        continue
    else:
        counter += 1
        print(f'{counter}.) {user_input.title()}')

# 1.) Deji
# 2.) Deji
# 3.) Deji
# 4.) Deji

# 1.) Are You Mad?
# 2.) Are You Mad?
# 3.) Are You Mad?
# 4.) Are You Mad?
# 5.) Are You Mad?
# 6.) Are You Mad?
# 7.) Are You Mad?
# 8.) Are You Mad?
# 9.) Are You Mad?
# 10.) Are You Mad?