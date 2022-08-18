import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
from langdetect import detect, detect_langs
import pandas as pd
from selenium import webdriver

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="3f7964aa78e54c1b88dab7cfe8510eb7",
                                                           client_secret="e5daeab79308427f83bbd18e8c35a157"))



print("Dil girin: ")
inp = input()

if(inp == "tr"):
    country = inp
    locale = "tr_TR"
elif(inp == "it"):
    country = inp
    locale = "it_IT"
elif(inp == "es"):
    country = inp
    locale = "es_ES"
elif(inp == "fr"):
    country = inp
    locale = "fr_FR"
elif(inp == "de"):
    country = inp
    locale = "de_DE"
elif(inp == "en"):
    country = "us"
    locale = "en_US"

print("country={}  input={}".format(country,inp))
playlist = pd.DataFrame(sp.featured_playlists(country=country, locale=locale, limit=10)["playlists"]["items"])

playlist_list = []
track_list = []

for i in range(len(playlist)):
    if detect(playlist["name"][i]) == inp:
        playlist_list.append(playlist["id"][i])

playlist_list

items = len(playlist_list)
item = random.randint(0, items - 1)
playlist_id = playlist_list[item]
tracks = sp.playlist_items(playlist_id)["items"]

for i in range(len(tracks)):
    if detect(tracks[i]["track"]["name"]) == inp:
        track_list.append(tracks[i]["track"]["name"] + " - " + tracks[i]["track"]["artists"][0]["name"])

items = len(track_list)
item = random.randint(0, items - 1)
print(track_list[item])

print("Şarkıyı YouTube'da açmak ister misin? (e/h):")
answer = input()
if answer=="e":
    driver = webdriver.Firefox(executable_path="/home/serhat/İndirilenler/geckodriver-v0.31.0-linux64/geckodriver")
    url = "https://www.youtube.com/results?search_query=" + track_list[item]
    driver.get(url)


