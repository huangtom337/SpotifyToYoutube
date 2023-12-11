export function SpotifyLogin() {
  const handleSpotifyLogin = () => {
    const loginURl = 'http://localhost:8888/login_spotify';
    window.location.href = loginURl;
  };

  return <button onClick={handleSpotifyLogin}>Login To Spotify</button>;
}
