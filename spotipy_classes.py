class _SpotipyBase(object):
	
	def __init__(self, href=None, type=None, uri=None):
		self.href = href
		self.type = type
		self.uri = uri
		
		
class SpotipyArtist(_SpotipyBase):
	
	def __init__(self, id, name, external_urls=None, href=None, type=None, uri=None):
		self.id = id
		self.name = name
		self.external_urls=external_urls
		self.href = href
		self.type = type
		self.uri = uri
		
		
class SpotipyAlbum(_SpotipyBase):
	
	def __init__(self, id, name, album_type=None, artists=None, available_markets=None, external_urls=None, href=None, images=None, type=None, uri=None):
		self.id = id
		self.name = name
		self.external_urls = external_urls or []
		self.artists = artists or []
		self.available_markets = available_markets or []
		self.href = href
		self.images = images or []
		self.type = type
		self.uri = uri
		
		
class SpotipyTrack(_SpotipyBase):
	
	def __init__(self, id, name, album, artists, available_markets=None, disc_number=None, duration_ms=0, explicit=False, external_ids=None, external_urls=None, href=None, popularity=None, preview_url=None, track_number=None, type=None, uri=None):
		self.id = id
		self.name = name
		self.album = album
		self.artists = artists
		self.available_markets = available_markets
		self.disc_number = disc_number
		self.duration_ms = duration_ms
		self.explicit = explicit
		self.external_ids = external_ids
		self.external_urls = external_urls
		self.href = href
		self.popularity = popularity
		self.preview_url = preview_url
		self.track_number = track_number
		self.type = type
		self.uri = uri


class SpotipyPlayback(object):
	
	def __init__(self, track, timestamp=None, progress_ms=None, is_playing=False, context=None):
		self.track = track
		self.timestamp = timestamp or time.time()
		self.progress_ms = progress_ms or 0
		self.is_playing = is_playing
		self.context = context
	
	
def get_currently_playing():
	current = currently_playing()
	track = current.get('item')
	a = track.get('album')
	album = SpotipyAlbum(a.get('id'), a.get('name'), a.get('album_type'), ) 