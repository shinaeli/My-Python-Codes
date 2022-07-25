def make_album(artist_name, album_name):
    return {'artist': artist_name, 'album': album_name}


while True:
    print("Enter 'quit' to quit")
    user_artist = input("Provide the artist's name: ").lower()
    if user_artist == 'quit':
        break

    print("Enter 'quit' to quit")
    user_album_title = input("Provide the album's title: ").lower()
    if user_album_title == 'quit':
        break

    call = make_album(user_artist.title(), user_album_title.title())
    print(call)




