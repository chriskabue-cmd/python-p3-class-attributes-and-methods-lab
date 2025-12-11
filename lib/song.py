class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Count total songs
        Song.count += 1

        # Add all genres and artists (including duplicates)
        Song.genres.append(genre)
        Song.artists.append(artist)

        # Add unique genres and artists
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # Update histograms
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # -----------------------------
    # UNIQUE GENRES
    # -----------------------------
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    # -----------------------------
    # UNIQUE ARTISTS
    # -----------------------------
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # -----------------------------
    # GENRE HISTOGRAM
    # -----------------------------
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    # -----------------------------
    # ARTIST HISTOGRAM
    # -----------------------------
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
