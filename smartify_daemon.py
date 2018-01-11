from spotipy_flask_test import SPOTIFY_APP_ID, SPOTIFY_APP_SECRET, LASTFM_API_KEY, LASTFM_API_SECRET, SCOPES
import pylast
redirect_url = 'http://127.0.0.1:5000/login/authorized'
scopes = ' '.join(SCOPES)
import spotipy
from spotipy import oauth2
from spotipy_classes import SpotipyArtist, SpotipyAlbum, SpotipyTrack, SpotipyPlayback, SpotipyPlaylist, Scrobbler
from spotipy import util
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers import SchedulerNotRunningError
import logging
import configparser
from pylast_stub import get_playlist_playcounts

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s - %(message)s', filename='smartify_testing.log', level=logging.INFO)

scheduler = BackgroundScheduler()
username = 'wisdomwolf'
oauth = util.prompt_for_user_token(username=username,scope=scopes,client_id=SPOTIFY_APP_ID,client_secret=SPOTIFY_APP_SECRET,redirect_uri=redirect_url)
sp = spotipy.Spotify(oauth=oauth)


config = configparser.ConfigParser()
config.read('settings.ini')
#[Out]# ['settings.ini']
env_vars = config['Environment Vars']
password_hash = env_vars['lastfm_default_pwhash']
network = pylast.LastFMNetwork(api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET, username='wisdomwolf', password_hash=password_hash)
user = pylast.User('wisdomwolf', network)


def restart_scheduler():
    global scheduler
    try:
        scheduler.shutdown()
    except SchedulerNotRunningError:
        logging.info('Scheduler already shutdown')
        pass
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(my_scrobbler.update_track, 'interval', seconds=10, replace_existing=True)
    scheduler.start()
    logging.info('Scheduler Restarted')
    print('Scheduler restarted successfully')
    
    
def log_filter(record):
    if record.levelno < 30 and 'apscheduler' in record.name:
        return False
    else:
        return True


logger = logging.getLogger()
logger.handlers[0].addFilter(log_filter)

def get_playlist_uri(playlist_name):
    playlists = sp.current_user_playlists()
    playlist_name_uri_map = {playlist.get('name'): playlist.get('uri') for playlist in playlists.get('items')}
    return playlist_name_uri_map.get(playlist_name)


def get_playlist_json(playlist_name):
    playlist_uri = get_playlist_uri(playlist_name).split(':')
    return sp.user_playlist(playlist_uri[2], playlist_uri[-1])


def create_spotipy_playlist(playlist_name):
    return SpotipyPlaylist(**get_playlist_json(playlist_name), sp=sp, precache=True)


def get_undiscovered_tracks(playlist):
    playcounts = get_playlist_playcounts(playlist)
    undiscovered = [track for track, count in playcounts.items() if count < 1]
    return [track for track in playlist.tracks if '{} - {}'.format(track.name, track.artist) in undiscovered]


def get_track_uris(track_list):
    return [track.uri for track in track_list]

if __name__ == '__main__':
    my_scrobbler = Scrobbler(sp, user, network)
