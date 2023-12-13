import { useState, useEffect } from 'react';

export function ConvertPlaylist() {
  const [responseSuccess, setResponseSuccess] = useState(false);
  const [processStarted, setProcessStarted] = useState(false);
  const [progressFinding, setProgressFinding] = useState(0);
  const [progressConverting, setProgressConverting] = useState(0);
  const [findingComplete, setFindingComplete] = useState(false);
  const [convertingComplete, setConvertingComplete] = useState(false);
  const convertPlaylist = async () => {
    setProcessStarted(true);
    const response = await fetch('http://localhost:8888/find_video_youtube', {
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error('Could not convert playlist');
    }

    const data = await response.json();
    if (data.success) {
      setResponseSuccess(true);
    }
  };

  // Polling for finding videos progress
  useEffect(() => {
    const interval = setInterval(async () => {
      const response = await fetch('http://localhost:8888/find_video_progress');
      const data = await response.json();
      setProgressFinding(data.progress);
      if (data.progress >= 100) {
        clearInterval(interval); // Stop polling when progress is 100%
        setFindingComplete(true);
      }
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  // Polling for converting videos progress
  useEffect(() => {
    let interval: NodeJS.Timer;
    if (findingComplete) {
      interval = setInterval(async () => {
        const response = await fetch(
          'http://localhost:8888/insert_playlist_progress'
        );
        const data = await response.json();
        setProgressConverting(data.progress);
        if (data.progress >= 100) {
          clearInterval(interval);
          setConvertingComplete(true); // Set converting videos as complete
        }
      }, 1000);
    }

    return () => interval && clearInterval(interval);
  }, [findingComplete]);
  return (
    <div>
      {!processStarted && !responseSuccess && (
        <button onClick={convertPlaylist}>Convert</button>
      )}
      {processStarted && !findingComplete && (
        <div>Finding Videos Progress: {progressFinding}%</div>
      )}
      {findingComplete && !convertingComplete && (
        <div>Converting Videos Progress: {progressConverting}%</div>
      )}
      {convertingComplete && <h2>Conversion Complete!</h2>}
    </div>
  );
}
