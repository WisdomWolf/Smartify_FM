__author__ = 'WisdomWolf'
from configparser import ConfigParser
import sys
import os
import pdb
import pylast
import spotipy
import spotipy.util as util

config = ConfigParser()
config.read('settings.ini')

# PyLast
API_KEY = config['Last-FM API']['lastfm_api_key']
API_SECRET = config['Last-FM API']['lastfm_api_secret']

lastfm_username = config['LastFM']['Username']
password_hash = config['LastFM']['Password Hash']

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=lastfm_username,
                               password_hash=password_hash)

# SpotiPy
scope = 'user-library-read'
os.environ['SPOTIPY_CLIENT_ID'] = config['Spotify API']['spotipy_client_id']
os.environ['SPOTIPY_CLIENT_SECRET'] = config['Spotify API']['spotipy_client_secret']
os.environ['SPOTIPY_REDIRECT_URI'] = config['Spotify API']['spotipy_callback_url']


def show_tracks(results, page=0):
    for i, item in enumerate(tracks['items'], start=1):
        track = item['track']
        title = track['name']
        artist = track['artists'][0]['name']
        index = i + page + (page * 99)
        count = get_user_play_count_in_track_info(artist, title)
        info = '{0:<3}{1:>50} {2:<50}     {3}'.format(index, artist, title, count)
        print(info)
        csv_info = '{0},"{1}","{2}",{3}\n'.format(index, artist, title, count)
        # with open('playlist_counts.csv', 'a+') as playcount_file:
        #     print(index)
        #     playcount_file.write(csv_info)


def get_user_play_count_in_track_info(artist, title):
    # Arrange
    track = pylast.Track(
        artist=artist, title=title,
        network=network, username=lastfm_username)

    # Act
    count = track.get_userplaycount()
    return count


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        try:
            username = config['Spotify']['Username']
            print('reading username from ini file')
        except:
            print("Usage: %s username" % (sys.argv[0],))
            sys.exit()

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items'][:2]:
            if playlist['owner']['id'] == username:
                print()
                print(playlist['name'])
                track_total = playlist['tracks']['total']
                print('  total tracks', track_total)
                results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                page = 0
                while tracks['next']:
                    page += 1
                    tracks = sp.next(tracks)
                    show_tracks(tracks, page)
                print('end of playlist:{0}'.format(playlist['name']))
    else:
        print("Can't get token for", username)
