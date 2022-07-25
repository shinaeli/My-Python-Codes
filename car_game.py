user_input = input('Enter an input: ').lower()
while user_input != 'quit':
    if user_input == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
        break
    elif user_input == 'start':
        print('Car started...Ready to go')
        break
    elif user_input == 'stop':
        print('Car stopped')
        break
    elif user_input == 'quit':
        break
    else:
        print("I don't understand that")
        break

