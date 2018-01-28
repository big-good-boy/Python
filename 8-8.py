# -*- coding: utf-8 -*-

def make_album(artist_name, album_name):
    print("Артист: " + artist_name + ", " + "исполнитель: " + album_name)

while True:
    print("\nПожалуйста, введите информацию об альбоме")
    print("(для завершения работы введите \"q\")")

    artist = input("Введите имя исполнителя: ")
    if artist == 'q':
        break
    
    album = input("Введите название альбома: ")
    if album == 'q':
        break

    make_album(artist, album)