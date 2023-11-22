import requests
from collections import defaultdict
import flask
from flask import Flask, redirect, request, session
from dotenv import load_dotenv
import secrets
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from reverse_api import find_video_ID

app = Flask(__name__)
load_dotenv()

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri_spotify = 'http://localhost:8888/callback_spotify'
redirect_uri_youtube = 'http://localhost:8888/callback_youtube'
playlists_I_want = set(['Demon', '3am', 'DY', 'Does it get better than this', 'K', '青春', 'Piano x2', 'Artcore x2', '日本語'])
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CLIENT_SECRETS_FILE = os.getenv('YOUTUBE_SECRET_FILE')
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
good_playlist = defaultdict(list)
youtube_playlist = defaultdict(list) # {playlist_name: [videoID...]}

app.secret_key = 'akwdjnakwjdn'

#OAuth 2.0 Spotify
def get_access_token_spotify(code, spotify_client_id, spotify_client_secret):

    token_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri_spotify,
        'client_id': spotify_client_id,
        'client_secret': spotify_client_secret
    }

    response = requests.post(token_url, data=payload)
    if response.ok:
        return response.json()  # Contains access token and refresh token
    else:
        return response.text

def get_playlists(access_token):
    user_id = '12179241495'
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists?limit=50"
    headers = {
        'Authorization': f"Bearer {access_token}"
    }
    
    response = requests.get(url, headers=headers)
    
    data = None
    if response.ok:
        data = response.json()
    else:
        data = str(response.status_code) + response.text
    
    
    return get_own_playlists(data['items'], user_id)

def get_own_playlists(all_playlists, user_id):

    return [playlist for playlist in all_playlists if playlist['owner']['id'] == user_id] 


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

def create_playlist(youtube, title, description, privacy_status):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": title,
            "description": description
          },
          "status": {
            "privacyStatus": privacy_status
          }
        }
    )
    response = request.execute()
    print(f"Playlist created: {response['snippet']['title']} (ID: {response['id']})")
    return response

@app.route('/')
def index():
    return redirect("/login_spotify")

@app.route('/login_spotify')
def login_spotify():
    state = secrets.token_urlsafe(16)
      
    # Spotify authorization URL
    auth_url = "https://accounts.spotify.com/authorize?" + \
               f"client_id={spotify_client_id}&response_type=code&redirect_uri={redirect_uri_spotify}&state={state}&scope=playlist-read-private"
    return redirect(auth_url)

@app.route('/callback_spotify')
def callback_spotify():
    # Handle the callback from Spotify
    # Extract the authorization code from the request
    code = request.args.get('code')
   
    # Exchange code for access token
    tokens = get_access_token_spotify(code, spotify_client_id, spotify_client_secret)
    spotify_access_token = tokens['access_token']
    spotify_refresh_token = tokens['refresh_token']
   
    # Fetch playlists
    playlists = get_playlists(spotify_access_token)
    playlist_name_id = [(playlist['name'], playlist['id']) for playlist in playlists if playlist['name'] in playlists_I_want]
    # Fetch songs from playlists
    
    for playlist_name, playlist_id in playlist_name_id: 
        songs = get_playlist_songs(spotify_access_token, playlist_id)
        if songs:
            print(playlist_name)
            for song in songs:
                song_artists = song['track'].get('artists', None)
                song_name = song['track'].get('name', None)
                if song_artists and song_name:
                    all_artists_string = ', '.join([artist.get('name', '') for artist in song_artists])
                    good_playlist[playlist_name].append((all_artists_string, song_name))
 
    return flask.redirect('find_video_youtube')


@app.route('/find_video_youtube')
def find_video_youtube():
    
    for playlist_name, songs in good_playlist.items():
        for song in songs:
            artist_names, song_name = song[0], song[1]
            query_string = song_name + " " + artist_names
        
            video_id = find_video_ID(query_string)
            youtube_playlist[playlist_name].append(video_id)
    
    return flask.redict('create_playlist_youtube')

@app.route('/create_playlist_youtube')
def create_playlist_youtube():
    


#Youtube Quota Too Expensive
# @app.route('/find_video_youtube')
# def find_video_youtube(): 
#     if 'credentials' not in flask.session:
#         return flask.redirect('authorize_youtube')
    
#     credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])
    
#     youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    
#     youtube_playlist = defaultdict(list) # {playlist_name: [videoID...]}

#     for playlist_name, songs in session['good_playlist'].items():
#         for song in songs:
#             artist_names, song_name = song[0], song[1]
#             query_string = song_name + " " + artist_names
        
#             request = youtube.search().list(
#                 part="snippet",
#                 maxResults=1,
#                 order="relevance",
#                 q=f"{query_string}",
#                 type="video",
#                 videoCategoryId="10",
#             )
#             response = request.execute()
#             search_result = response['items'][0]
#             video_id = search_result['id']['videoId']
#             youtube_playlist[playlist_name].append(video_id)

#     flask.session['credentials'] = credentials_to_dict(credentials)

#     return flask.jsonify(**youtube_playlist)

# @app.route('/authorize_youtube')
# def authorize_youtube():
#     # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
#     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)   
#     # flow.redirect_uri = flask.url_for('callback_youtube', _external=True)

#     authorization_url, state = flow.authorization_url(
#         # Enable offline access so that you can refresh an access token without
#         # re-prompting the user for permission. Recommended for web server apps.
#         access_type='offline',
#         # Enable incremental authorization. Recommended as a best practice.
#         include_granted_scopes='true')

#     # Store the state so the callback can verify the auth server response.
#     flask.session['state'] = state
    
#     return flask.redirect(authorization_url)
    
# @app.route('/callback_youtube')
# def callback_youtube():
#     # Specify the state when creating the flow in the callback so that it can
#     # verified in the authorization server response.
#     state = flask.session['state']

#     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
#     flow.redirect_uri = flask.url_for('callback_youtube', _external=True)

#     # Use the authorization server's response to fetch the OAuth 2.0 tokens.
#     authorization_response = flask.request.url
#     flow.fetch_token(authorization_response=authorization_response)

#     # Store credentials in the session.
#     # ACTION ITEM: In a production app, you likely want to save these
#     #              credentials in a persistent database instead.
#     credentials = flow.credentials
#     flask.session['credentials'] = credentials_to_dict(credentials)

#     return flask.redirect(flask.url_for('find_video_youtube'))    

# @app.route('/clear')
# def clear_credentials():
#   if 'credentials' in flask.session:
#     del flask.session['credentials']
#   return ('Credentials have been cleared.<br><br>')    


# def credentials_to_dict(credentials):
#   return {'token': credentials.token,
#           'refresh_token': credentials.refresh_token,
#           'token_uri': credentials.token_uri,
#           'client_id': credentials.client_id,
#           'client_secret': credentials.client_secret,
#           'scopes': credentials.scopes}


if __name__ == '__main__':
    
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    app.run(port=8888)





    

