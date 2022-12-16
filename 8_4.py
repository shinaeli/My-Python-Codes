def make_shirt(size='large', title='I love Python'):
    print(f'This shirt is of size "{size}" and it has a message "{title.title()}" printed on it.')


make_shirt()
make_shirt('medium')
make_shirt(title='weiRD THougTs', size='extra large')

# This shirt is of size "large" and it has a message "I Love Python" printed on it.
# This shirt is of size "medium" and it has a message "I Love Python" printed on it.
# This shirt is of size "extra large" and it has a message "Weird Thougts" printed on it.