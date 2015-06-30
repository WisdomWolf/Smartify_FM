__author__ = 'WisdomWolf'
from flask import Flask, redirect, url_for, session, request
from flask_oauthlib.client import OAuth, OAuthException


SPOTIFY_APP_ID = '3193cf23af3d42588b9bbf90dec4972e'
SPOTIFY_APP_SECRET = '8b7d415777144a90b0c33df42925490a'


app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

spotify = oauth.remote_app(
    'spotify',
    consumer_key=SPOTIFY_APP_ID,
    consumer_secret=SPOTIFY_APP_SECRET,
    # Change the scope to match whatever it us you need
    # list of scopes can be found in the url below
    # https://developer.spotify.com/web-api/using-scopes/
    request_token_params={'scope': 'user-library-read'},
    base_url='https://accounts.spotify.com',
    request_token_url=None,
    access_token_url='/api/token',
    authorize_url='https://accounts.spotify.com/authorize'
)


@app.route('/')
def index():
    return redirect(url_for('login'))


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
    resp = spotify.authorized_response()
    if resp is None:
        return 'Access denied: reason={0} error={1}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, OAuthException):
        return 'Access denied: {0}'.format(resp.message)

    session['oauth_token'] = (resp['access_token'], '')
    me = spotify.get('https://api.spotify.com/v1/me')
    return 'Logged in as id={0} name={1} redirect={2}'.format(
        me.data['id'],
        me.data['display_name'],
        request.args.get('next')
    )


@spotify.tokengetter
def get_spotify_oauth_token():
    return session.get('oauth_token')


if __name__ == '__main__':
    app.run()
