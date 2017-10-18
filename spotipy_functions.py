# coding: utf-8
import spotipy
import pickle
#context_uri = sp.current_playback().get('context').get('uri')
def get_playback_percentage(current_playback):
    if current_playback.get('is_playing'):
        return '{0:.0f}%'.format(current_playback.get('progress_ms') / current_playback.get('item').get('duration_ms') * 100)
    else:
        return 'Playback Stopped'


def get_context_playlist(uri):
    playlists = sp.current_user_playlists()
    playlist_uri_map = {playlist.get('uri'): playlist.get('name') for playlist in playlists.get('items')}
    return playlist_uri_map.get(uri.split(':')[-1])
