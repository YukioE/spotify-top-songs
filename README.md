# Spotify User's Most Listened To
Utilizes Spotipy and Spotify Web API to create playlists of a users's most listened to songs for a certain period of time.

## Requirements
* Spotipy Library https://github.com/plamere/spotipy/tree/2.13.0
* Spotify Account https://www.spotify.com/
* Spotify Developer App/Client ID/Client Secret

# Instructions
1) Install requirements

`pip3 install -r requirements.txt`

2) Collect Spotify Credentials
* Go to your Spotify Developer Dashboard https://developer.spotify.com/dashboard/
* Register a new app
* Collect Client ID and Client Secret (recommended to put into secrets.py file along with redirect uri)
* Click the Edit Settings and add your desired Redirect URI (recommended is http://localhost:8888/callback/) to the Redirect URI section. This has to match the Redirect URI you have in your secret.py file in order to avoid an Invalid URI error
* Add Client ID and Client Secrets to secrets.py (Best results are when using `SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'`)
* Run file from command line with the title of the playlist you want to create as an argument

`python3 my_top_songs.py -p PLAYLIST_NAME -t TIME_RANGE`
* Input desired range of time as either `short` (4 weeks), `medium` (6 months), or `long` (All time)
* if TIME_RANGE argument is not present the default time range is short

## .env example

```
SPOTIPY_CLIENT_ID=
SPOTIPY_CLIENT_SECRET=
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback/
SPOTIFY_USERNAME=

# Playlist name and time range
PLAYLIST_NAME=My Top Songs
TIME_RANGE=short  # short, medium, long
```

Copy this to .env and fill in your credentials.

## ToDo
* Create GUI
* Add additional functionality
* Add option for text file

# Troubleshooting
* A user cannot have two playlists of the same name
* INVALID_REDIRECT_URI - Make sure you have set the REDIRECT_URI in both secrets.py and in your Spotify Developer Application settings. Make sure they match
* INVALID_CLIENT_ID - Make sure that you have added the correct CLIENT ID to secrets.py
* INVALID_CLIENT_SECRET - Make sure that you have added the correct CLIENT SECRET to secrets.py
