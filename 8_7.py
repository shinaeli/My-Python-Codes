def make_album(artist_name, album_name, no_of_songs = None):
    return {'artist': artist_name, 'album': album_name, 'songs': no_of_songs}


call_1 = make_album('Nas', 'Illmatic', 14)
print(call_1)
call_2 = make_album('Jay-Z', 'The Blueprint', 16)
print(call_2)
call_3 = make_album('T.I.', 'Paper Trail')
print(call_3)

# {'artist': 'Nas', 'album': 'Illmatic', 'songs': 14}
# {'artist': 'Jay-Z', 'album': 'The Blueprint', 'songs': 16}
# {'artist': 'T.I.', 'album': 'Paper Trail', 'songs': None}