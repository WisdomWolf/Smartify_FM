__author__ = 'WisdomWolf'
import os
from flask import (
    Flask,
    redirect,
    url_for,
    session,
    request,
    jsonify,
    render_template
)
from flask_oauthlib.client import OAuth, OAuthException
from flask_bootstrap import Bootstrap
from configparser import ConfigParser
import pylast
import spotiwise
import sched
import time
import pdb
from pylast import WSError

# if os.path.exists('settings.ini'):
#     config = ConfigParser()
#     config.read('settings.ini')

#     env = config['Environment Vars']
#     for k, v in env.items():
#         os.environ[k] = v


# Ini
config = ConfigParser()
config.read('settings.ini')
env_vars = config['Environment Vars']

SCOPES = [
 'playlist-read-private',
 'playlist-read-collaborative',
 'playlist-modify-public',
 'playlist-modify-private',
 'streaming',
 'ugc-image-upload',
 'user-follow-modify',
 'user-follow-read',
 'user-library-read',
 'user-library-modify',
 'user-read-private',
 'user-read-birthdate',
 'user-read-email',
 'user-top-read',
 'user-read-playback-state',
 'user-modify-playback-state',
 'user-read-currently-playing',
 'user-read-recently-played']

# PyLast
LASTFM_API_KEY = os.getenv('LASTFM_API_KEY') or env_vars['LASTFM_API_KEY']
LASTFM_API_SECRET = os.getenv('LASTFM_API_SECRET') or env_vars['LASTFM_API_SECRET']
lastfm_username = os.getenv('LASTFM_DEFAULT_USERNAME') or env_vars['LASTFM_DEFAULT_USERNAME']
password_hash = os.getenv('LASTFM_DEFAULT_PWHASH') or env_vars['LASTFM_DEFAULT_PWHASH']
spotify_username = os.getenv('SPOTIFY_DEFAULT_USERNAME') or env_vars['SPOTIFY_DEFAULT_USERNAME']
sp = None

network = pylast.LastFMNetwork(api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET,
                               username=lastfm_username,
                               password_hash=password_hash)

# Spotify
SPOTIFY_APP_ID = os.getenv('SPOTIPY_CLIENT_ID') or env_vars['SPOTIPY_CLIENT_ID']
SPOTIFY_APP_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET') or env_vars['SPOTIPY_CLIENT_SECRET']

DEFAULT_ALBUM_ART = "http://upload.wikimedia.org/wikipedia/en/5/54/Public_image_ltd_album_cover.jpg"

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)
Bootstrap(app)
s = sched.scheduler(time.time, time.sleep)
playlist_is_initialized = False

spotify = oauth.remote_app(
    'spotify',
    consumer_key=SPOTIFY_APP_ID,
    consumer_secret=SPOTIFY_APP_SECRET,
    # Change the scope to match whatever it us you need
    # list of scopes can be found in the url below
    # https://developer.spotify.com/web-api/using-scopes/
    # request_token_params={'scope': 'playlist-modify-public user-read-playback-state'},
    request_token_params={'scope': ' '.join(SCOPES)},
    base_url='https://accounts.spotify.com',
    request_token_url=None,
    access_token_url='/api/token',
    authorize_url='https://accounts.spotify.com/authorize'
)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/now-playing')
def now_playing():
    user = pylast.User(lastfm_username, network)
    return '{0} | {1}'.format(user.get_now_playing().artist, user.get_now_playing().title)

@app.route('/currently-playing/')
@app.route('/currently-playing/<username>')
def currently_playing(username=None):
    username = username or 'wisdomwolf'
    playing = pylast.User(username, network).get_now_playing()
    try:
        image = get_cover_art(playing)
        print('{0} {1}'.format(playing.artist, playing.title))
        return render_template('currently-playing.html',
            artist=playing.artist, track=playing.title, image=image)
    except AttributeError:
        print('Nothing playing')
        return render_template('currently-playing.html',
                               artist='nothing', track='playing', image=DEFAULT_ALBUM_ART)

def get_cover_art(playing):
    try:
        album = playing.get_album()
        if not album:
            sp = spotiwise.Spotify()
            search_str = '{0} {1}'.format(playing.artist, playing.title)
            track = sp.search(search_str)['tracks']['items']
            if track:
                print('returning art from Spotify')
                return track[0]['album']['images'][0]['url']
            else:
                return DEFAULT_ALBUM_ART
        elif album.get_cover_image():
            return album.get_cover_image()
        else:
            return DEFAULT_ALBUM_ART
    except AttributeError:
        return DEFAULT_ALBUM_ART

@app.route('/update_now_playing')
def update_now_playing():
    username = request.args.get('username', '', type=str)
    try:
        playing = pylast.User(username, network).get_now_playing()
        print('{0} {1}'.format(playing.artist, playing.title))
        image = get_cover_art(playing)
        return jsonify(track=playing.title,
                       artist=playing.artist.get_name(),
                       image=image,
                       track_url=playing.get_url())
    except AttributeError:
        print('No data to update')
        return jsonify(track='playing',
                       artist='nothing',
                       image=DEFAULT_ALBUM_ART,
                       track_url='#')


@app.route('/recent-tracks')
def recent_tracks():
    user = pylast.User(lastfm_username, network)
    track_list = []
    print('{0} tracks found.'.format(len(user.get_recent_tracks(limit=2))))
    for played_track in user.get_recent_tracks(limit=2):
        track_list.append('{0} | {1}'.format(played_track.track.artist, played_track.track.title))

    return '<br/>'.join(track_list)

@app.route('/login')
def login():
    callback = url_for(
        'spotify_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True
    )
    return spotify.authorize(callback=callback)


@app.route('/login/authorized')
def spotify_authorized():
    global sp, spotify_username
    resp = spotify.authorized_response()
    if resp is None:
        return 'Access denied: reason={0} error={1}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, OAuthException):
        return 'Access denied: {0}'.format(resp.message)

    session['oauth_token'] = (resp['access_token'], '')
    token = session['oauth_token'][0]
    me = spotify.get('https://api.spotify.com/v1/me')
    spotify_username = me.data['id']
    sp = spotiwise.Spotify(auth=token)
    with open('{}_token.dat'.format(spotify_username), 'w') as f:
        f.write(token)
    print('Token stored')
    playlists = sp.user_playlists(spotify_username)
    return display_playlists(playlists)
    # return 'Logged in as id={0} name={1} redirect={2}'.format(
    #     me.data['id'],
    #     me.data['display_name'],
    #     request.args.get('next')
    # )

def display_playlists(playlists):
    result = []
    result_link = []
    track_toals = []
    for playlist in playlists['items']:
        result.append(playlist['name'])
        track_toals.append(playlist['tracks']['total'])
        result_link.append(url_for('display_tracks', playlist_id=playlist['id']))

    return render_template('display_playlists.html',
                           playlists=zip(result, track_toals, result_link))

@app.route('/list_tracks/<playlist_id>')
def display_tracks(playlist_id):
    global sp
    results = []
    playlist = sp.user_playlist(spotify_username, playlist_id)
    tracks = playlist['tracks']
    results += parse_tracks(tracks)
    page = 0
    while tracks['next']:
        page += 1
        tracks = sp.next(tracks)
        results += parse_tracks(tracks, page)
    pdb.set_trace()
    return '<br/>'.join(format_track_list(results))

def format_track_list(track_list):
    results = []
    for index, track in enumerate(track_list, start=1):
        info = '{0}. {1}/{2} | {3}'.format(index,
                                           track['artist'], track['name'],
                                           track['play_count'])
        results.append(info)
    return results

def parse_tracks(tracks, page=0):
    results = []
    for i, item in enumerate(tracks['items'], start=1):
        track = item['track']
        track['artist'] = track['artists'][0]['name']
        artist = track['artists'][0]['name']
        title = track['name']
        track_id = track['id']
        index = i + page + (page * 99)
        # play_count = get_user_play_count_in_track_info(artist, title)
        play_count = 0
        track['play_count'] = play_count
        # info = zip(index, artist, title, play_count, track_id)
        results.append(track)

    return results
        # print(name, '-', artist, '|', track_id, '|', play_count)

def get_user_play_count_in_track_info(artist, title):
    # Arrange
    track = pylast.Track(
        artist=artist, title=title,
        network=network, username=lastfm_username)

    # Act
    try:
        count = track.get_userplaycount()
    except WSError:
        print('Unable to locate {0} - {1}'.format(artist, title))
        count = -1
    return count

@spotify.tokengetter
def get_spotify_oauth_token():
    return session.get('oauth_token')

def remove_recent_from_playlist(playlist_id, playlist):
    pass

def initialize_playlist(playlist_id):
    global sp
    results = []
    playlist = sp.user_playlist(spotify_username, playlist_id)
    tracks = playlist['tracks']
    results += parse_tracks(tracks)
    page = 0
    while tracks['next']:
        page += 1
        tracks = sp.next(tracks)
        results += parse_tracks(tracks, page)

    return results



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
