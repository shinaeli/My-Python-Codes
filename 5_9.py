usernames = []

if len(usernames) != 0:
    for name in usernames:
        if name == 'Admin':
            print(f'Hello {name}, would you like to see a status report?')
        else:
            print(f'Hello {name}, thank you for logging in again.')
else:
    print('We need to find some users.')