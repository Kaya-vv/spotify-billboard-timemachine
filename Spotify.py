import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import os

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']


class Spotify:
    def __init__(self, date):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                            client_secret=CLIENT_SECRET,
                                                            redirect_uri="http://example.com",
                                                            scope="playlist-modify-private"))
        self.user_id = self.sp.current_user()['id']
        self.date = date

    def get_track_uri(self, track, year):
        song = self.sp.search(f"track:{track} year:{year}", type='track')
        try:
            track_uri = song['tracks']['items'][0]['uri']
        except IndexError:
            print(f"{track} doesnt exist in Spotify. Skipped")
            return None
        return track_uri

    def create_playlist(self, tracks):
        playlist_id = self.sp.user_playlist_create(self.user_id, f"{self.date} Billboard 100", public=False)

        if self.sp.playlist_add_items(playlist_id=playlist_id['id'], items=tracks):
            print("Playlist successfully created")
