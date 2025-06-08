import os
import argparse
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env
load_dotenv()


def get_args():
    parser = argparse.ArgumentParser(
        description='Add user\'s top tracks to a Spotify playlist')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Name of the playlist to update')
    parser.add_argument('-t', '--time', required=True, choices=['short', 'medium', 'long'],
                        help='Time range: short (4 weeks), medium (6 months), long (years)')
    return parser.parse_args()


def set_sp(scope):
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        cache_path='.cache'  # stays inside container
    ))


def get_time_range(range_short):
    return {
        'short': 'short_term',
        'medium': 'medium_term',
        'long': 'long_term'
    }.get(range_short, 'short_term')


def get_top_track_ids(sp, time_range):
    top_tracks = sp.current_user_top_tracks(time_range=time_range, limit=50)
    return [track['id'] for track in top_tracks['items']]


def get_or_create_playlist(sp, playlist_name):
    user_id = sp.me()['id']
    playlists = sp.current_user_playlists(limit=50)['items']
    for playlist in playlists:
        if playlist['name'].lower() == playlist_name.lower():
            return playlist['id']
    new = sp.user_playlist_create(user_id, playlist_name)
    return new['id']


def main():
    args = get_args()
    time_range = get_time_range(args.time)

    # Get top tracks
    sp_read = set_sp('user-top-read')
    track_ids = get_top_track_ids(sp_read, time_range)

    # Get playlist and add tracks
    sp_write = set_sp('playlist-modify-public')
    playlist_id = get_or_create_playlist(sp_write, args.playlist)
    sp_write.user_playlist_replace_items(
        sp_write.me()['id'], playlist_id, track_ids)

    print(f"✅ Playlist '{args.playlist}' updated with {len(track_ids)} top tracks ({args.time} term).")


if __name__ == '__main__':
    main()
