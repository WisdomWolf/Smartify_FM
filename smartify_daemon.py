from spotipy_flask_test import SPOTIFY_APP_ID, LASTFM_API_KEY, LASTFM_API_SECRET, SCOPES
import pylast
import spotiwise
from spotiwise import oauth2
from spotiwise.object_classes import SpotiwiseArtist, SpotiwiseAlbum, SpotiwiseTrack, SpotiwisePlayback, SpotiwisePlaylist, SpotiwiseItem
#from spotiwise_classes import SpotipyArtist, SpotipyAlbum, SpotipyTrack, SpotipyPlayback, SpotipyPlaylist, Scrobbler
from spotiwise import util
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers import SchedulerNotRunningError
import logging
import configparser
from pylast_stub import get_playlist_playcounts
from aws_requests_auth.aws_auth import AWSRequestsAuth
from aws_requests_auth import boto_utils
from urllib import parse as urlparse
import re

redirect_url = 'http://127.0.0.1:5000/login/authorized'
scopes = ' '.join(SCOPES)

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s - %(message)s', filename='smartify_testing.log', level=logging.INFO)

scheduler = BackgroundScheduler()
username = 'wisdomwolf'

def get_aws_auth(url):
    api_gateway_netloc = urlparse.urlparse(url).netloc
    api_gateway_region = re.match(
        r"[a-z0-9]+\.execute-api\.(.+)\.amazonaws\.com",
        api_gateway_netloc
    ).group(1)

    return AWSRequestsAuth(
        aws_host=api_gateway_netloc,
        aws_region=api_gateway_region,
        aws_service='execute-api',
        **boto_utils.get_credentials()
    )

oauth = util.prompt_for_user_token(
    username=username,
    scope=scopes,
    client_id=SPOTIFY_APP_ID,
    redirect_uri=redirect_url,
    token_url="https://dk1ytlmiwk.execute-api.us-east-1.amazonaws.com/dev/token",
    auth_func=get_aws_auth
)
sp = spotiwise.Spotify(oauth=oauth)


config = configparser.ConfigParser()
config.read('settings.ini')
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
    playlist_name_uri_map = {playlist.name: playlist.uri for playlist in playlists}
    return playlist_name_uri_map.get(playlist_name)


def get_playlist_json(playlist_name):
    playlist_uri = get_playlist_uri(playlist_name).split(':')
    return sp._user_playlist(playlist_uri[2], playlist_uri[-1])


def get_playlist(playlist_name):
    playlist_uri = get_playlist_uri(playlist_name).split(':')
    return sp.user_playlist(playlist_uri[2], playlist_uri[-1], precache=True)


def create_spotiwise_playlist(playlist_name):
    return SpotiwisePlaylist(**get_playlist_json(playlist_name), sp=sp, precache=True)


def get_undiscovered_tracks(playlist):
    playcounts = get_playlist_playcounts(playlist)
    undiscovered = [track for track, count in playcounts.items() if count < 1]
    return [item.track for item in playlist.tracks if '{} - {}'.format(item.track.name, item.track.artist) in undiscovered]


def get_track_uris(track_list):
    return [item.track.uri for item in track_list]

if __name__ == '__main__':
    my_scrobbler = Scrobbler(sp, user, network)
    my_scrobbler.scheduler.add_job(my_scrobbler.update_track, 'interval', seconds=10)

