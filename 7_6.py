
while True:
    user_age = int(input('Please, provide your age: '))
    if 1 <= user_age < 3:
        print('You have a free ticket.')
    elif 3 <= user_age <= 12:
        print(f'Your ticket price is ${10}.')
    elif user_age > 12:
        print(f'Your ticket price is ${15}.')
    else:
        break
