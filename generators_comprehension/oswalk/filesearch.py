import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        # Filter directories with a match
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):  # get the path
            yield song


# Chaining the generators album_list is passed in song_list
album_list = find_albums("music", "Aerosmith")
# album_list = find_albums("music", "Black*")  # this is platform dependent case match
song_list = find_songs(album_list)

# If we keep this code the generator would have already yielded the value hence song_list would be empty
# for a in album_list:
#     print(a)

print("*" * 80)

for s in song_list:
    print(s)
