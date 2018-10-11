#!/usr/env python3

import os
import pylast
import pickle
from pprint import pprint
from threading import Thread
import time
import concurrent.futures
import configparser
from pylast import NetworkError

def get_track_playcount(track):
    try:
        return track.get_userplaycount()
    except pylast.WSError:
        print('Error: Unable to find info for {} - {}'.format(track.artist, track.title))
        return -1
    except NetworkError:
        print('Network Error, delaying 10 seconds')
        time.sleep(10)
        return get_track_playcount(track)


def get_playcounts_threaded(track_list, workers=None):
    user_playcount_dict = {}
    workers = workers or 4
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
            user_playcount_dict['{} - {}'.format(track.title, track.artist)] = count
    print('Took: {}'.format(time.time() - start_time))
    return user_playcount_dict


def get_playcounts_single(track_list):
    user_playcount_dict = {}
    start_time = time.time()
    for track, count in zip(track_list, map(get_track_playcount, track_list)):
        user_playcount_dict[track] = count
    print('Took: {}'.format(time.time() - start_time))
    return user_playcount_dict


def get_playcounts_concurrent(track_list):
    user_playcount_dict = {}
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
            user_playcount_dict[track] = count
    print('Took: {}'.format(time.time() - start_time))
    return user_playcount_dict


# Ini
config = configparser.ConfigParser()
config.read('settings.ini')
env_vars = config['Environment Vars']

# PyLast
API_KEY = os.getenv('LASTFM_API_KEY') or env_vars['lastfm_api_key']
API_SECRET = os.getenv('LASTFM_API_SECRET') or env_vars['lastfm_api_secret']
lastfm_username = os.getenv('LASTFM_DEFAULT_USERNAME') or env_vars['lastfm_default_username']
password_hash = os.getenv('LASTFM_DEFAULT_PWHASH') or env_vars['lastfm_default_pwhash']
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=lastfm_username,
                               password_hash=password_hash)
# sets user to DEFAULT
user = pylast.User(lastfm_username, network)


def get_all_tracks(user, chunk_size=1000, last_timestamp=0):
    playcount = user.get_playcount()
    tracks = set()
    last_timestamp = last_timestamp
    chunks = playcount // chunk_size + 1
    for i in range(chunks):
        print('Getting chunk {} of {}'.format(i + 1, chunks))
        recent_tracks = user.get_recent_tracks(limit=chunk_size, time_to=last_timestamp)
        tracks = tracks.union(recent_tracks)
        last_timestamp = int(recent_tracks[-1].timestamp)
    return sorted(list(tracks), key=lambda x: x.timestamp, reverse=True)

def create_library_set(track_history, user):
    library_set = set()
    for entry in track_history:
        library_set.add(entry.track)
    for track in library_set:
        track.username = user.name
    return library_set

def get_playlist_playcounts(playlist):
    pylast_tracks = [pylast.Track(artist=item.track.artist, title=item.track.name, network=network, username=lastfm_username) for item in playlist.items]
    return get_playcounts_threaded(pylast_tracks, 64)

if __name__ == "__main__":

    with open('wisdomwolf_tracks.p', 'rb') as f:
        wisdomwolf_tracks = pickle.load(f)

    wisdomwolf_library = create_library_set(wisdomwolf_tracks, user)
    print('To get playcounts run: get_playcounts_threaded(wisdomwolf_library, 16/32/64)')
