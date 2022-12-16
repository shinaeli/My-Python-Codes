print("Enter 'q' to quit.")

while True:
    user_input = input('Provide a number either negative or positive: ')
    if user_input == 'q':
        break
    else:
        if int(user_input) >= 0:
            print('It is a positive number.')
        else:
            print('It is a negative number.')

