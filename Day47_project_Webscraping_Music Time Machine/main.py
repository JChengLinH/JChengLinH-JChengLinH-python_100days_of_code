import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv(r"C:\python_course_projects\Day47_project_Webscraping_Music Time Machine\cred.env")


date_input = input("What year do you want to travel to (YYYY-MM-DD)? ")

web_url = f"https://www.billboard.com/charts/hot-100/{date_input}/"
response = requests.get(url=web_url)
web_html = response.text
soup = BeautifulSoup(web_html, "html.parser")
songs = soup.select("li > #title-of-a-story")

artist_name_css_paths = "ul > li.lrv-u-width-100p > ul > li.o-chart-results-list__item.\/\/.lrv-u-flex-grow-1.lrv-u-flex.\
lrv-u-flex-direction-column.lrv-u-justify-content-center.lrv-u-border-b-1.u-border-b-0\@mobile-max.lrv-u-border-color-grey-light.\
lrv-u-padding-l-1\@mobile-max > span"

artists = soup.select(artist_name_css_paths)
song_titles = [song.getText().replace("\n", "") for song in songs]
song_artists = [name.getText().replace(" Featuring", ",") for name in artists]
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True
    )
)

playlist = sp.user_playlist_create(user=os.getenv("USER_ID"), name=f"{date_input} Billboard Top 100", public=False)
song_uri = []
i = 0
#Searching for songs on Spotify.
for n in range(len(song_titles)):
    search_result = sp.search(f"track:{song_titles[n]} artist:{song_artists[n]}", type="track")
    try:
        song_uri.append(search_result["tracks"]["items"][0]["uri"])
    except IndexError:
        i += 1
        print(f"{song_titles[n]} by {song_artists[n]} doesn't exist in Spotify, {i} songs skipped.\n")

#Adding all the songs that were find in Spotify.
sp.playlist_add_items(playlist["id"], song_uri)

