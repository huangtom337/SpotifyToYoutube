import requests
from collections import defaultdict
from flask import Flask, redirect, request
from dotenv import load_dotenv
import secrets
import os

app = Flask(__name__)
load_dotenv()

client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri = 'http://localhost:8888/callback'
access_token = None
playlists_I_want = set(['Demon', '3am', 'DY', 'Does it get better than this', 'K', '青春', 'Piano x2', 'Artcore x2', '日本語'])

#OAuth 2.0
def get_access_token(code, client_id, client_secret):

    token_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(token_url, data=payload)
    if response.ok:
        return response.json()  # Contains access token and refresh token
    else:
        return response.text

def get_playlists(access_token):
    url = "https://api.spotify.com/v1/users/12179241495/playlists"
    headers = {
        'Authorization': f"Bearer {access_token}"
    }
    
    response = requests.get(url, headers=headers)
    
    data = None
    if response.ok:
        data = response.json()
    else:
        data = str(response.status_code) + response.text
    
    return data

def get_playlist_songs(access_token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {
        'Authorization': f"Bearer {access_token}"
    }
    
    response = requests.get(url, headers=headers)

    data = None
    if response.ok:
        data = response.json()
    else:
        data = str(response.status_code) + response.text
    
    tracks = data.get('tracks', None)
    tracks_items = tracks.get('items', None)
    
    return tracks_items


@app.route('/')
def index():
    return redirect("/login")

@app.route('/login')
def login():
    state = secrets.token_urlsafe(16)
      
    # Spotify authorization URL
    auth_url = "https://accounts.spotify.com/authorize?" + \
               f"client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&state={state}&scope=playlist-read-private"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Handle the callback from Spotify
    # Extract the authorization code from the request
    code = request.args.get('code')
   
    # Exchange code for access token
    tokens = get_access_token(code, client_id, client_secret)
    access_token = tokens['access_token']
    refresh_token = tokens['refresh_token']
   
    # Fetch playlists
    playlists = get_playlists(access_token)['items']
    playlist_name_id = [(playlist['name'], playlist['id']) for playlist in playlists if playlist['name'] in playlists_I_want]
    # Fetch songs from playlists
    good_playlist = defaultdict(list)
    for playlist_name, playlist_id in playlist_name_id: 
        songs = get_playlist_songs(access_token, playlist_id)
        if songs:
            for song in songs:
                song_artists = song['track'].get('artists', None)
                song_name = song['track'].get('name', None)
                if song_artists and song_name:
                    all_artists_string = ', '.join([artist.get('name', '') for artist in song_artists])
                    good_playlist[playlist_name].append((all_artists_string, song_name))
    return str(good_playlist)  # Convert the result to string for display



if __name__ == '__main__':
    app.run(port=8888)
      



    

