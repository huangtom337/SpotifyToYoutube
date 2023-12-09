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
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
load_dotenv()

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri_spotify = 'http://localhost:8888/callback_spotify'
redirect_uri_youtube = 'http://localhost:8888/callback_youtube'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CLIENT_SECRETS_FILE = os.getenv('YOUTUBE_SECRET_FILE')
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
good_playlist = defaultdict(list)
youtube_playlist = defaultdict(list) # {playlist_name: [videoID...]}
youtube_playlist_id = defaultdict(list) # {playlist_id: [videoID...]}
app.secret_key = os.getenv('APP_SECRET_KEY')



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

def get_user_id(access_token):
    
    url = "https://api.spotify.com/v1/me"
    headers = {
        'Authorization': f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    
    if response.ok:
        return response.json()['id']
    else:
        return str(response.status_code) + response.text

def get_playlists(access_token, user_id):

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

def find_video_youtube():
    
    for playlist_name, songs in good_playlist.items():
        for song in songs:
            artist_names, song_name = song[0], song[1]
            query_string = song_name + " " + artist_names
        
            video_id = find_video_ID(query_string)
            youtube_playlist[playlist_name].append(video_id)

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
    credentials = spotify_credentials_to_dict(tokens)
    flask.session['spotify_credentials'] = credentials
  
    return redirect(f"http://localhost:5173?loggedIn=true")
    # Fetch playlists
    # playlists = get_playlists(spotify_access_token, user_id)
    # return flask.jsonify(playlists)
    # playlist_name_id = [(playlist['name'], playlist['id']) for playlist in playlists if playlist['name'] == '3am']
    # playlist_user = ""
    # playlist_name_id = None
    # # Get User input
    # while not playlist_name_id:
    #     for playlist in playlists:
    #         print(playlist['name'])
    #     playlist_user = input("Enter playlist name to be converted: ")
                
    #     playlist_name_id = [(playlist['name'], playlist['id']) for playlist in playlists if playlist['name'] == playlist_user]
    #     if not playlist_name_id:
    #         print('Please enter a valid playlist name')
    
    # for playlist_name, playlist_id in playlist_name_id: 
    #     songs = get_playlist_songs(spotify_access_token, playlist_id)
    #     if songs:
    #         for song in songs:
    #             song_artists = song['track'].get('artists', None)
    #             song_name = song['track'].get('name', None)
    #             if song_artists and song_name:
    #                 all_artists_string = ', '.join([artist.get('name', '') for artist in song_artists])
    #                 good_playlist[playlist_name].append((all_artists_string, song_name))
 
    # return flask.jsonify(good_playlist)
    # return flask.redirect('authorize_youtube')

@app.route('/create_playlist_youtube')
def create_playlist_youtube():

    credentials = youtube_credentials_from_dict(flask.session['youtube_credentials'])
    youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    
    for playlist_name in youtube_playlist:
        request = youtube.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": f"{playlist_name}",
                    "description": "",
                    "tags": [
                    "playlist",
                    "API call"
                    ],
                    "defaultLanguage": "en"
                },
                "status": {
                    "privacyStatus": "public"
                }
            }       
        )
        
        
        response = request.execute()

        playlist_id = response['id']
        youtube_playlist_id[playlist_id] = youtube_playlist[f"{playlist_name}"]

  
    return flask.redirect('insert_playlist')

@app.route('/insert_playlist')
def insert_playlist():

    credentials = youtube_credentials_from_dict(flask.session['youtube_credentials'])
    youtube = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)
   
    for playlist_id, video_ids in youtube_playlist_id.items():
        for video_id in video_ids:
           
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                "snippet": {
                    "playlistId": f"{playlist_id}",
                    "resourceId": {
                    "kind": "youtube#video",
                    "videoId": f"{video_id}"
                    }
                }
                }
            )
            response = request.execute()    

    return "hi"

@app.route('/authorize_youtube')
def authorize_youtube():
    # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)   
    flow.redirect_uri = flask.url_for('callback_youtube', _external=True)

    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    # Store the state so the callback can verify the auth server response.
    flask.session['state'] = state
    
    return flask.redirect(authorization_url)
    
@app.route('/callback_youtube')
def callback_youtube():
    # Specify the state when creating the flow in the callback so that it can
    # verified in the authorization server response.
    state = flask.session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('callback_youtube', _external=True)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store credentials in the session.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    credentials = flow.credentials

    flask.session['youtube_credentials'] = credentials_to_dict(credentials)
    find_video_youtube()
    
    return flask.redirect(flask.url_for('create_playlist_youtube'))    

@app.route('/clear')
def clear_credentials():
  if 'youtube_credentials' in flask.session:
    del flask.session['youtube_credentials']
  return ('Credentials have been cleared.<br><br>')    

def youtube_credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

def youtube_credentials_from_dict(credentials_dict):
    return google.oauth2.credentials.Credentials(
        token=credentials_dict['token'],
        refresh_token=credentials_dict['refresh_token'],
        token_uri=credentials_dict['token_uri'],
        client_id=credentials_dict['client_id'],
        client_secret=credentials_dict['client_secret'],
        scopes=credentials_dict['scopes'])

def spotify_credentials_to_dict(credentials):
    return {'access_token': credentials['access_token'], 
            'refresh_token': credentials['refresh_token'], 
            'user_id': get_user_id(credentials['access_token'])}


def main():
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    app.run(port=8888)
    
    
if __name__ == '__main__':
    main()
    






    

