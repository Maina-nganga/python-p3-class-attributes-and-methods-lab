class Song:
    all = []
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre


        Song.all.append(self)
        Song.count += 1

 
        if genre not in Song.genres:
            Song.genres.append(genre)

     
        if artist not in Song.artists:
            Song.artists.append(artist)

 
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1

        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        self._name = value


    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        if not isinstance(value, str):
            raise Exception("Artist must be a string.")
        self._artist = value


    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if not isinstance(value, str):
            raise Exception("Genre must be a string.")
        self._genre = value
