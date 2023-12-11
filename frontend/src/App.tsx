import { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import './App.css';
import { SpotifyLogin } from './components/SpotifyLogin/SpotifyLogin';
import { PlaylistDisplay } from './components/PlaylistDisplay/PlaylistDisplay';
import { YoutubeLogin } from './components/YoutubeLogin/YoutubeLogin';
import { ConvertPlaylist } from './components/ConvertPlaylist/ConvertPlaylist';

export type UserPlaylistData = {
  name: string;
};

function App() {
  const [playlists, setPlaylists] = useState<UserPlaylistData[]>([]);
  const [processComplete, setProcessComplete] = useState(false);
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const loggedInSpotify = queryParams.get('loggedInSpotify'); // Get the 'loggedIn' parameter
  const loggedInYoutube = queryParams.get('loggedInYoutube');

  const handlePlaylistClick = async (playlist: UserPlaylistData) => {
    try {
      const response = await fetch('http://localhost:8888/convert_playlist', {
        method: 'POST',
        body: JSON.stringify(playlist),
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
      });

      if (!response.ok) {
        throw new Error('Could not select playlist');
      }

      const data = await response.json();

      if (data.success) {
        setProcessComplete(true);
      }
    } catch (error) {
      throw new Error('Error fetching data');
    }
  };

  const fetchPlaylists = async () => {
    try {
      const response = await fetch(
        'http://localhost:8888/get_playlists_spotify',
        {
          credentials: 'include',
        }
      );
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setPlaylists(data);
    } catch (error) {
      console.error('Error fetching data: ', error);
    }
  };

  useEffect(() => {
    if (loggedInSpotify === 'true') {
      console.log('User is logged in');
      fetchPlaylists();
    }
  }, [loggedInSpotify]); // This effect runs when the 'loggedInSpotify' parameter changes

  return (
    <div>
      {!loggedInYoutube && !loggedInSpotify && <SpotifyLogin />}
      {!processComplete && loggedInSpotify && playlists.length > 0 && (
        <PlaylistDisplay
          playlists={playlists}
          onPlaylistClick={handlePlaylistClick}
        />
      )}
      {processComplete && <YoutubeLogin />}
      {loggedInYoutube && <ConvertPlaylist />}
    </div>
  );
}

export default App;
