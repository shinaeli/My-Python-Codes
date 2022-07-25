guest_name = input('What is your name? ')

with open('guests.txt', 'w') as guest_object:
    guest_object.write(guest_name)