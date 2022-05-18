class playlist:

    id = ""
    name = ""
    tracks = []

    def __init__(self, id, name, tracks):
        self.id = id
        self.name = name
        self.tracks = tracks
    
    def add_track(self, track):
        self.tracks.append(track)
    
    def add_tracks(self, tracks):
        self.tracks.extend(tracks)
    
    def remove_track(self, track):
        self.tracks.remove(track)
    
    def delete_tracks(self, tracks):
        track = []

class track:

    id = ""
    name = ""
    artist = ""
    album = ""

    def __init__(self, id, name, artist, album):
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album
    
    def __str__(self):
        return self.name + " – " + self.artist + " (" + self.album + ")"
    

class user:

    id = ""
    username = ""
    playlists = []

    def __init__(self, id, username):
        self.id = id
        self.username = username

    def add_playlist(self, playlist):
        self.playlists.append(playlist)
    
    def add_playlists(self, playlists):
        self.playlists.extend(playlists)

    def remove_playlist(self, playlist):
        self.playlists.remove(playlist)
    
    def delete_playlists(self, playlists):
        playlists = []
    
    def get_id(self):
        return self.id
    
    def get_username(self):
        return self.username