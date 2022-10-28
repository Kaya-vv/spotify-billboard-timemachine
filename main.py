import requests
from bs4 import BeautifulSoup
from Spotify import Spotify

date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, "html.parser")
year = date.split("-")[0]
song_tags = soup.select('.o-chart-results-list__item #title-of-a-story')
song_list = [song.getText().strip() for song in song_tags]

spotify = Spotify(date)
track_uris = []
print("Loading tracks....")
for song in song_list:
    track_uri = spotify.get_track_uri(song, year)
    if track_uri is None:
        continue
    track_uris.append(track_uri)
spotify.create_playlist(track_uris)