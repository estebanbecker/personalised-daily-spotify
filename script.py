import spotipy
import database
import user

from spotipy.oauth2 import SpotifyOAuth






def connect_new_user(data):
    scope = "user-library-read,user-read-recently-played,user-read-playback-position,\
    user-top-read,playlist-read-collaborative,playlist-modify-public,playlist-read-private\
    ,playlist-modify-private"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    connect_user = user.user(sp.me()["id"], sp.me()["display_name"])

    data.save_user(connect_user)

    return sp, connect_user

def connect_known_user(data, user_id):
    scope = "user-library-read,user-read-recently-played,user-read-playback-position,\
    user-top-read,playlist-read-collaborative,playlist-modify-public,playlist-read-private\
    ,playlist-modify-private"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=user_id))

    connect_user = data.get_user(user_id)

    return sp, connect_user

data = database.Database("database")


