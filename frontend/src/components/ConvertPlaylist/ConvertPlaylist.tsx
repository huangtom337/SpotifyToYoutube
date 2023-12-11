import { useState } from 'react';

export function ConvertPlaylist() {
  const [responseMsg, setResponseMsg] = useState('');
  const [responseSuccess, setResponseSuccess] = useState(false);
  const convertPlaylist = async () => {
    const response = await fetch(
      'http://localhost:8888/create_playlist_youtube',
      {
        credentials: 'include',
      }
    );

    if (!response.ok) {
      throw new Error('Could not convert playlist');
    }

    const data = await response.json();
    if (data.success) {
      setResponseSuccess(true);
      setResponseMsg(data.message);
    }
  };

  // set up progressing polling
  return (
    <div>
      {/* set up progress polling */}
      {!responseSuccess && <button onClick={convertPlaylist}>Convert</button>}
      <h1>{responseMsg}</h1>
    </div>
  );
}
