import { UserPlaylistData } from '../../App';
import './PlaylistDisplay.css';

type PlaylistDisplayProps = {
  playlists: UserPlaylistData[];
  onPlaylistClick: (playlist: UserPlaylistData) => void;
};

export function PlaylistDisplay({
  playlists,
  onPlaylistClick,
}: PlaylistDisplayProps) {
  return (
    <div>
      <h1>Select a Playlist to Convert</h1>
      <ul className='playlist-ul'>
        {playlists.map((playlist, index) => (
          <li
            key={index}
            onClick={() => onPlaylistClick(playlist)}
            className='playlist-li'>
            <span className='playlist-text'>{playlist.name}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
