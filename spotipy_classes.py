from datetime import date

class _SpotipyBase(object):

    def __init__(self, href=None, type=None, uri=None):
        self.href = href
        self.type = type
        self.uri = uri

    def __repr__(self):
        repr_list = []
        for k, v in self.__dict__.items():
            if v:
                if isinstance(v, date):
                    v = '{:%m/%d/%Y}'.format(v)
                k = k.replace('_', ' ')
                repr_list.append('{}={}'.format(k, v))
        return '{}({})'.format(self.__class__.__name__, ', '.join(sorted(repr_list, key=self._sort)))

    @staticmethod
    def _sort(key):
        '''Used to ensure certain attributes are listed first'''
        key = key.split(':')[0].lower()
        sort_keys = ['id', 'name'] # Should probably be a class variable so that it can be easily overridden
        try:
            return sort_keys.index(key)
        except ValueError:
            return float('inf')



class SpotipyArtist(_SpotipyBase):

    def __init__(self, id, name, external_urls=None, href=None, type=None, uri=None, *args, **kwargs):
        self.id = id
        self.name = name
        self.external_urls=external_urls
        self.href = href
        self.type = type
        self.uri = uri
        self._args = args
        self._kwargs = kwargs


class SpotipyAlbum(_SpotipyBase):

    def __init__(self, id, name, album_type=None, artists=None, available_markets=None, external_urls=None, href=None, images=None, type=None, uri=None, *args, **kwargs):
        self.id = id
        self.name = name
        self.external_urls = external_urls or []
        self._artists = [SpotipyArtist(**artist) if not isinstance(artist, SpotipyArtist) else artist for artist in artists]
        self.artist = self._artists[0].name
        self.available_markets = available_markets or []
        self.href = href
        self.images = images or []
        self.type = type
        self.uri = uri
        self._args = args
        self._kwargs = kwargs


class SpotipyTrack(_SpotipyBase):

    def __init__(self, id, name, album, artists, available_markets=None, disc_number=None, duration_ms=0, explicit=False, external_ids=None, external_urls=None, href=None, popularity=None, preview_url=None, track_number=None, type=None, uri=None, *args, **kwargs):
        #print('__init__ received')
       # for param, value in locals().items():
          #  print('{}: {}\n'.format(param, value))
        self.id = id
        self.name = name
        if isinstance(album, SpotipyAlbum):
            self.album = album
        else:
            self.album = SpotipyAlbum(**album)
        self._artists = [SpotipyArtist(**artist) if not isinstance(artist, SpotipyArtist) else artist for artist in artists]
        self.artist = self._artists[0].name
        self.available_markets = available_markets or []
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.duration = self.duration_ms // 1000
        self.explicit = explicit
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.href = href
        self.popularity = popularity
        self.preview_url = preview_url
        self.track_number = track_number
        self.type = type
        self.uri = uri
        self._args = args
        self._kwargs = kwargs


class SpotipyPlayback(_SpotipyBase):

    def __init__(self, item, timestamp=None, progress_ms=None, is_playing=False, context=None, *args, **kwargs):
       # print('__init__ received')
     #   for param, value in locals().items():
         #   print('{}: {}\n'.format(param, value))
        self.track = item if isinstance(item, SpotipyTrack) else SpotipyTrack(**item)
        self.timestamp = timestamp or time.time()
        self.epoch_timestamp = self.timestamp // 1000
        self.progress_ms = progress_ms or 0
        self.is_playing = is_playing
        self.context = context
        self._args = args
        self._kwargs = kwargs


def mad_parser(thing):
    results = {}
    if isinstance(thing, dict):
        for k, v in thing.items():
            results[k] = mad_parser(v)
            if thing.get('type') and thing.get('id'):
                return SpotipyTypes[thing['type']](**thing)
        return results
    elif isinstance(thing, list):
        things = []
        for x in thing:
            things.append(mad_parser(x))
        return things
    else:
        return thing


SpotipyTypes = {
    'album': SpotipyAlbum,
    'track': SpotipyTrack,
    'artist': SpotipyArtist
}

def get_currently_playing():
    current = currently_playing()
    track = current.get('item')
    a = track.get('album')
    album = SpotipyAlbum(a.get('id'), a.get('name'), a.get('album_type'), )


def scrobbler(sp, lastfm_user, lastfm_network):
    sp_now_playing = create_lastfm_tuple(sp.currently_playing())
    lastfm_now_playing = lastfm_user.get_now_playing()
    if sp_now_playing and not lastfm_now_playing:
        if playback_percentage(sp.currently_playing()) > 70:
            print('should scrobble {}'.format(sp_now_playing.title))
            lastfm_network.scrobble(*sp_now_playing)
        else:
            print('updating lastfm now playing')
            lastfm_network.update_now_playing(sp_now_playing.artist, sp_now_playing.title,
                        sp_now_playing.album, sp_now_playing.album_artist, sp_now_playing.duration)
    elif sp_now_playing.title != lastfm_now_playing.title:
        print('Spotify: {}\nLast.FM: {}'.format(sp_now_playing.title, lastfm_now_playing.title))
        print('updating lastfm')
        lastfm_network.update_now_playing(sp_now_playing.artist, sp_now_playing.title, sp_now_playing.album, sp_now_playing.album_artist, sp_now_playing.duration)
    else:
        print('Looks good!')


class Scrobbler(object):
    def __init__(self, spotify, lastfm_user, lastfm_network, current_track=None):
        self.previous_track = None
        self.spotify = spotify
        self.lastfm_user = lastfm_user
        self.lastfm_network = lastfm_network
        self.current_track = current_track or SpotipyPlayback(**self.spotify.currently_playing())

    def update_track(self, track=None):
        track = track or SpotipyPlayback(**self.spotify.currently_playing())
        if track and track.is_playing:
            if not lastfm_user.get_now_playing():
                print('updating lastfm now playing')
                self.lastfm_network.update_now_playing(track.track.artist, track.track.name,
                        track.track.album, track.track.album.artist, track.track.duration)
            if self.current_track != track:
                self.previous_track = self.current_track
                self.current_track = track
                self.scrobble_check()
        else:
            print('nothing currently playing')

    def scrobble_check(self):
        previous_track = self.previous_track.track
        if self.lastfm_user.get_recent_tracks(limit=1)[0].track.get_name != previous_track.track.name:
            print('should scrobble {}'.format(previous_track.title))
            lastfm_network.scrobble(artist=previous_track.artist, title=previous_track.name,
                timestamp=self.previous_track.epoch_timestamp, album=previous_track.album.name,
                album_artist=previous_track.album.artist, duration=previous_track.duration)


def create_lastfm_tuple(spotify_now_playing):
    from collections import namedtuple
    NowPlaying = namedtuple('NowPlaying', ['artist', 'title', 'timestamp', 'album', 'album_artist', 'duration'])
    NowPlaying.__new__.__defaults__ = (None, None, None)
    track = spotify_now_playing.get('item')
    return NowPlaying(artist=track.get('artists')[0].get('name'), title=track.get('name'), timestamp=spotify_now_playing.get('timestamp')//1000, album=track.get('album').get('name'),
        album_artist=track.get('album').get('artists')[0].get('name'), duration=track.get('duration_ms') // 1000)


if __name__ == '__main__':
    import json
    with open('example_track.json') as f:
        example_track = json.load(f)