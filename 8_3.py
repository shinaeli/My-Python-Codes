def make_shirt(size, title):
    print(f'This shirt is of size: "{size}" and it has a message "{title.title()}" printed on it.')

# Calling the function with positional arguments
make_shirt(12, 'The world is YOUrS!')
# Calling the function with keyword arguments
make_shirt(title='Life IS WHat yoU MAke iT', size=25)