# Write a program that asks the user to enter a password. If the user enters the right password,
# the program should tell them they are logged in to the system. Otherwise, the program
# should ask them to reenter the password. The user should only get five tries to enter the
# password, after which point the program should tell them that they are kicked off of the
# system.

counter = 0
while counter <= 5:
    user_password = input('provide password: ')
    if user_password == '' or user_password.isalpha() == True or ' ' in user_password:
        print('Invalid Password')
        counter += 1
    else:
        print('You are logged into the system.')
        break
    if counter == 5:
        print('You are kicked off the system.')
        break


