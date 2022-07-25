counter = True

while counter:
    user_age = input('Please, provide your age: ')
    if user_age.lower() != 'quit':
        if int(user_age) < 3:
            print('You have a free ticket.')
        elif 3 <= int(user_age) <= 12:
            print(f'Your ticket price is ${10}.')
        elif int(user_age) > 12:
            print(f'Your ticket price is ${15}.')
    else:
        counter = False
