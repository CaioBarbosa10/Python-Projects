import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID ="111b084f149d4bb6a38054032073e95e"
CLIENT_SECRET = "a08c5c779fa04801bb05cabd87fe593d"

date = input("Wich Year do you want to travel to? type the date in this format YYYY-MM-DD:")
URL =f"https://www.billboard.com/charts/hot-100/{date}"


response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")

song_names_span = soup.select("li ul li h3")


all_song_names =[ songs.getText().strip() for songs in song_names_span]

#Spotify Authentication

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in all_song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

