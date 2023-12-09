import { useState } from 'react';
import { useLocation } from 'react-router-dom';
import './App.css';

type UserPlaylistData = {
  name: string;
};

function App() {
  // const [playlists, setPlaylists] = useState<UserPlaylistData[]>([]);

  const handleSpotifyLogin = async () => {
    const loginURl = 'http://localhost:8888/login_spotify';

    window.location.href = loginURl;
  };
  // const fetchPlaylists = async () => {
  //   try {
  //     const response = await fetch('http://localhost:8888/callback_spotify');
  //     if (!response.ok) {
  //       throw new Error('Network response was not ok');
  //     }
  //     const data = await response.json();
  //     setPlaylists(data);
  //   } catch (error) {
  //     console.error('Error fetching data: ', error);
  //   }
  // };

  return (
    <div>
      <h1>User Playlists</h1>
      <button onClick={handleSpotifyLogin}>Login To Spotify</button>
      {/* {playlists.length > 0 && (
        <ul>
          {playlists.map((playlist, index) => (
            <li key={index}>{playlist.name}</li>
          ))}
        </ul>
      )} */}
    </div>
  );
}

export default App;
