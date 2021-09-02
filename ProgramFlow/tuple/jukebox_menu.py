from nested_data_clean import albums
# python executes the code in imported file hence moving to clean file

# for constant we dont have keyword rather all caps represents constant
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please print your album (invalid choice exits)")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print('PLease choose your song:')
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        pass
    else:
        break
    print("Playing {}".format(title))
    print('*' * 80)
