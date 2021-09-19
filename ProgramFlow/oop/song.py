class Song(object):
    """Class to represent a song

    Attributes:
        title (str): the title of the song
        artist (Artist): Artist of the song
        duration (int): The duration of song in seconds and my be 0
    """

    def __init__(self, title, artist, duration: int = 0):
        """Song Init method - refer PEP 257

        title (str): initializes 'artist' attribute
        artist (Artist): Artist object
        duration (optional[int]): Initial value of the duration default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album(object):
    """Class to represent an album

    Attributes:
        name (str): Name of album
        year (int): published year
        artist (Artist): The creator of artist
            if not specified defaults to Artist with name "various artist"
        tracks (List[Song]): A list of song

    Methods:
        add_songs: Add a new song to tracks list
    """
    
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist('Various Artists')
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to tracks

        Args
            song (Song): Song to add
            position (Optional(int)): if given add to that position else to end of list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not added again (although this is yet to implemented).
        """
        self.albums.append(album)


# def load_data() -> list[Artist]:
#     """
#     Loads initial data for albums from text file called albums.txt
#     this should be present in current directory
#     :return: list of artist
#     """
#     new_artist = None
#     new_album = None
#     artist_list = []
#
#     with open("albums.txt", "r") as albums:
#         for line in albums:
#             # data row should consist of (artist, album, year, song)
#             artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
#             year_field = int(year_field)
#             print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))
#
#             if new_artist is None:
#                 new_artist = Artist(artist_field)
#             elif new_artist.name != artist_field:
#                 # We've just read details for a new artist
#                 # store the current album in the currents artists collection then create a new artist object
#                 new_artist.add_album(new_album)
#                 artist_list.append(new_artist)
#                 new_artist = Artist(artist_field)
#                 new_album = None
#
#             if new_album is None:
#                 new_album = Album(album_field, year_field, new_artist)
#             elif new_album.name != album_field:
#                 # We've just read a new album for the current artist
#                 # store the current album in the artist's collection then create a new album object
#                 new_artist.add_album(new_album)
#                 new_album = Album(album_field, year_field, new_artist)
#
#             # create a new song object and add it to the current album's collection
#             new_song = Song(song_field, new_artist)
#             new_album.add_song(new_song)
#
#         # After read the last line of the text file, we will have an artist and album that haven't
#         #  been store - process them now
#         if new_artist is not None:
#             if new_album is not None:
#                 new_artist.add_album(new_album)
#             artist_list.append(new_artist)
#
#     return artist_list


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data() -> list[Artist]:
    """
    Loads initial data for albums from text file called albums.txt
    this should be present in current directory
    :return: list of artist
    """
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # retrieve the artist object if there is one,
                # otherwise create a new artist object and add it to the artist list.
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist
                # Retrieve the album object if there is one,
                # otherwise create a new album object and store it in the artist's collection.
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == "__main__":
    print('running as main')
    help(Song)
    print()
    print('*' * 80)
    print('*' * 80)
    help(Song.__init__)

    print()
    print('*' * 80)
    print('*' * 80)
    print('printing a doc')
    print(Song.__init__.__doc__)

    print()
    print('*' * 80)
    print('*' * 80)
    print('changing a doc as an object')
    Song.__init__.__doc__ = """***** My doc is changed ***** Song Init method - refer PEP 257

        title (str): initializes 'artist' attribute
        artist (Artist): Artist object
        duration (optional(int)): Initial value of the duration default to zero if not specified
        """
    help(Song.__init__)

    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)
else:
    print('running as module')
