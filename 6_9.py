favorite_places = {
    'harry': ['atlanta', 'china', 'kwara'],
    'george': ['rio de janeiro', 'cuba', 'lagos'],
    'benjamin': ['miami', 'chicago', 'washington d. c.']
}

friend_name = input('What is your name? ').lower()

if friend_name in favorite_places.keys():
    print(f'{friend_name.title()} wants to visit: ')
    for place in favorite_places[friend_name]:
        print(place.title())
else:
    print('Your name does not exist in our database.')
