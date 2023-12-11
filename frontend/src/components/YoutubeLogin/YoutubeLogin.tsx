export function YoutubeLogin() {
  const handleYoutubeLogin = () => {
    const loginURl = 'http://localhost:8888/authorize_youtube';
    window.location.href = loginURl;
  };

  return <button onClick={handleYoutubeLogin}>Login To Youtube</button>;
}
