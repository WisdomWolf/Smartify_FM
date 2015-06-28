import pylast

API_KEY = 'b0a63048f832f69173a58a6e1cdaa666'
API_SECRET = 'e9905ca5b6b44accdcdf661cbca132dc'

username = 'wisdomwolf'
password_hash = '077a7d34313a55bdaaa02b9a8785a8e1'

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

def test_user_play_count_in_track_info(self):
	# Arrange
	artist = "Test Artist"
	title = "Test Title"
	track = pylast.Track(
		artist=artist, title=title,
		network=self.network, username=self.username)

	# Act
	count = track.get_userplaycount()

	# Assert
	self.assertGreaterEqual(count, 0)