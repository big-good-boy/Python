def make_album(artist_name, album_name, track=20):
    info = {'artist name': artist_name, 'album name': album_name}
    if track:
        info['track'] = track
    return info

print(make_album("Distemper", "25", "22"))
print(make_album(artist_name="Distemper", album_name="My Underground", track="24"))
print(make_album("Distemper", "XV"))