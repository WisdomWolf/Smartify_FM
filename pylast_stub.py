import os
import pylast

# PyLast
API_KEY = os.environ['LASTFM_API_KEY']
API_SECRET = os.environ['LASTFM_API_SECRET']
lastfm_username = os.environ['LASTFM_DEFAULT_USERNAME']
password_hash = os.environ['LASTFM_DEFAULT_PWHASH']
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=lastfm_username,
                               password_hash=password_hash)

user = pylast.User(lastfm_username, network)


def get_all_tracks(user):
    playcount = user.get_playcount()
    tracks = set()
    last_timestamp = 0
    chunks = playcount // 1000 + 1
    for i in range(chunks):
        print('Getting chunk {} of {}'.format(i + 1, chunks))
        recent_tracks = user.get_recent_tracks(limit=1000, time_to=last_timestamp)
        tracks.union(recent_tracks)
        last_timestamp = int(recent_tracks[-1].timestamp)
    return sorted(list(tracks), key=lambda x: x.timestamp, reverse=True)
