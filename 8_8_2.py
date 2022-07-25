def make_album(artist_name, album_name):
    return {'artist': artist_name, 'album': album_name}


start = True
while start:
    user_artist = input("Provide the artist's name: ").lower()
    user_album_title = input("Provide the album's title: ").lower()

    if user_artist == 'quit' or user_album_title == 'quit':
        start = False
    else:
        call = make_album(user_artist.title(), user_album_title.title())
        print(call)