#!/usr/env python3

import os
import pylast
import pickle
from pprint import pprint
from threading import Thread

def get_track_playcount(track):
    try:
        return track.get_userplaycount()
    except pylast.WSError:
        print('Error: Unable to find info for {} - {}'.format(track.artist, track.title))
        return 0


def get_playcounts_threaded(track_list, workers=None):
    user_playcount_dict = {}
    workers = workers or 4
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
            user_playcount_dict[track] = count
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


# PyLast
API_KEY = os.environ['LASTFM_API_KEY']
API_SECRET = os.environ['LASTFM_API_SECRET']
lastfm_username = os.environ['LASTFM_DEFAULT_USERNAME']
password_hash = os.environ['LASTFM_DEFAULT_PWHASH']
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=lastfm_username,
                               password_hash=password_hash)
# sets user to DEFAULT
user = pylast.User(lastfm_username, network)


def get_all_tracks(user):
    playcount = user.get_playcount()
    tracks = set()
    last_timestamp = 0
    chunks = playcount // 1000 + 1
    for i in range(chunks):
        print('Getting chunk {} of {}'.format(i + 1, chunks))
        recent_tracks = user.get_recent_tracks(limit=1000, time_to=last_timestamp)
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

with open('wisdomwolf_tracks.p', 'rb') as f:
    wisdomwolf_tracks = pickle.load(f)
