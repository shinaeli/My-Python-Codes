print('Enter "quit" to cancel the program.')

starter = True

while starter:
        with open('guest_book.txt', 'a') as guest_book_object:
            guest_name = input('What is your name? ')
            if guest_name.lower() == 'quit':
                guest_book_object.write('\n')
                starter = False
            else:
                guest_book_object.write(f"{guest_name}" + '\n')





