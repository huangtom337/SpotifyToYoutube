import requests
from collections import defaultdict

client_id = '4bc9917a9eb24f6bb9d2061034aa5682'
client_secret = 'f0ebcd8f19b24fc9aba8cd731a8d9836'
access_token = None
playlists_I_want = set(['Demon', '3am', 'DY', 'Does it get better than this', 'K', '青春', 'Piano x2', 'Artcore x2', '日本語'])

def get_access_token(client_id, client_secret):

    url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers, data=data)

    access_token = None
    if response.ok:
        access_token = response.json().get('access_token', None)
        
    else:
        access_token = str(response.status_code) + response.text
    
    return access_token

access_token = get_access_token(client_id, client_secret)

def get_playlists():
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

playlists = get_playlists()['items']
playlist_name_id= [(playlist['name'], playlist['id']) for playlist in playlists if playlist['name'] in playlists_I_want ]

def get_playlist_songs(playlist_id):
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

good_playlist = defaultdict(list) # playlist_name : [(artists, song name)]

for playlist_name, playlist_id in playlist_name_id: 
    songs = get_playlist_songs(playlist_id)
    
    if songs:
        for song in songs:
        
            song_artists = song['track'].get('artists', None)
            song_name = song['track'].get('name', None)
            
            if song_artists and song_name:
                all_artists_string = ', '.join([artist.get('name', '') for artist in song_artists])
                good_playlist[playlist_name].append((all_artists_string, song_name))
               
            elif not song_artists and not song_name:
                print('This song cannot be added')

print(good_playlist)

      



    

