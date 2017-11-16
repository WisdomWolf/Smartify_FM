from spotipy_flask_test import SPOTIFY_APP_ID, SPOTIFY_APP_SECRET, LASTFM_API_KEY, LASTFM_API_SECRET, SCOPES
import pylast
redirect_url = 'http://127.0.0.1:5000/login/authorized'
scopes = ' '.join(SCOPES)
import spotipy
from spotipy import oauth2
from spotipy_classes import SpotipyArtist, SpotipyAlbum, SpotipyTrack, SpotipyPlayback, Scrobbler
from spotipy import util
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers import SchedulerNotRunningError
import logging
import configparser

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
my_scrobbler = Scrobbler(sp, user, network)

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
