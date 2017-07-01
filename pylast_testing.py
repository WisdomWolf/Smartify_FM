user.get_friends()
# OUT: [pylast.User('wisdomangel53', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1a
# OUT: cf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')), pylast.User('PurpleLover5198', pylast.LastFMNet
# OUT: work('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '0
# OUT: 77a7d34313a55bdaaa02b9a8785a8e1')), pylast.User('Skrimen', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b4
# OUT: 4accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')), pylast.User('Levia
# OUT: ton2Home', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1
# OUT: 061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')), pylast.User('pistol69', pylast.LastFMNetwork('b0a63048f832f69173a5
# OUT: 8a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a878
# OUT: 5a8e1'))]
user = pylast.User('Purplelover5198', network)
airin_scrobbles = get_all_tracks(user)
# OUT: Getting chunk 1 of 2
# OUT: Getting chunk 2 of 2
len(airin_scrobbles)
# OUT: 1634
airin_library = create_library_set(airin_scrobbles, user)
len(airin_library)
# OUT: 859
user_playcounts = {track: track.get_userplaycount() for track in airin_library}
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     user_playcounts = {track: track.get_userplaycount() for track in airin_library}
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<dictcomp>[39m
# OUT:     user_playcounts = {track: track.get_userplaycount() for track in airin_library}
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/pylast/__init__.py"[39m, line [35m[1m1887[0m
# OUT: [39m, in [36mget_userplaycount[39m
# OUT:     doc = self._request(self.ws_prefix + ".getInfo", True, params)
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/pylast/__init__.py"[39m, line [35m[1m1396[0m
# OUT: [39m, in [36m_request[39m
# OUT:     return _Request(self.network, method_name, params).execute(cacheable)
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/pylast/__init__.py"[39m, line [35m[1m1222[0m
# OUT: [39m, in [36mexecute[39m
# OUT:     response = self._download_response()
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/pylast/__init__.py"[39m, line [35m[1m1202[0m
# OUT: [39m, in [36m_download_response[39m
# OUT:     method='POST', url=HOST_SUBDIR, body=data, headers=headers)
# OUT:   File [32m"/usr/local/lib/python3.6/http/client.py"[39m, line [35m[1m1239[0m[39m, in [36mrequest[39m
# OUT:     self._send_request(method, url, body, headers, encode_chunked)
# OUT:   File [32m"/usr/local/lib/python3.6/http/client.py"[39m, line [35m[1m1285[0m[39m, in [36m_send_request[39m
# OUT:     self.endheaders(body, encode_chunked=encode_chunked)
# OUT:   File [32m"/usr/local/lib/python3.6/http/client.py"[39m, line [35m[1m1234[0m[39m, in [36mendheaders[39m
# OUT:     self._send_output(message_body, encode_chunked=encode_chunked)
# OUT:   File [32m"/usr/local/lib/python3.6/http/client.py"[39m, line [35m[1m1026[0m[39m, in [36m_send_output[39m
# OUT:     self.send(msg)
# OUT:   File [32m"/usr/local/lib/python3.6/http/client.py"[39m, line [35m[1m964[0m[39m, in [36msend[39m
# OUT:     self.connect()
# OUT:   File [32m"/usr/local/lib/python3.6/http/client.py"[39m, line [35m[1m1400[0m[39m, in [36mconnect[39m
# OUT:     server_hostname=server_hostname)
# OUT:   File [32m"/usr/local/lib/python3.6/ssl.py"[39m, line [35m[1m401[0m[39m, in [36mwrap_socket[39m
# OUT:     _context=self, _session=session)
# OUT:   File [32m"/usr/local/lib/python3.6/ssl.py"[39m, line [35m[1m808[0m[39m, in [36m__init__[39m
# OUT:     self.do_handshake()
# OUT:   File [32m"/usr/local/lib/python3.6/ssl.py"[39m, line [35m[1m1061[0m[39m, in [36mdo_handshake[39m
# OUT:     self._sslobj.do_handshake()
# OUT:   File [32m"/usr/local/lib/python3.6/ssl.py"[39m, line [35m[1m683[0m[39m, in [36mdo_handshake[39m
# OUT:     self._sslobj.do_handshake()
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/bpython/curtsiesfrontend/coderunner.py"[39m, lin
# OUT: e [35m[1m170[0m[39m, in [36msigint_handler[39m
# OUT:     raise KeyboardInterrupt()
# OUT: [31m[1mKeyboardInterrupt[0m[39m
library_sample = list(airin_library)[:10]
len(library_sample)
# OUT: 10
user_playcounts = {track: track.get_userplaycount() for track in library_sample}
user_playcounts
# OUT: {pylast.Track('BTS', '흥탄소년단 Boyz with Fun', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca
# OUT: 132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Wontolla', 'Can 
# OUT: You Feel Me', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bb
# OUT: ff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('Fall Out Boy', "I Don't Care", pylast.LastFMNe
# OUT: twork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '
# OUT: 077a7d34313a55bdaaa02b9a8785a8e1')): 4, pylast.Track('BTS', '상남자', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e990
# OUT: 5ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 4, pylast.
# OUT: Track('Demi Lovato', 'Stop the World', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc
# OUT: ', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Blood on the Dance Fl
# OUT: oor', 'Always And Forever', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf
# OUT: 325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Hinder', 'Heaven Sent', pylast.L
# OUT: astFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomw
# OUT: olf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Drowning Pool', 'Hell to Pay', pylast.LastFMNetwork('b0a63048f832f69
# OUT: 173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b
# OUT: 9a8785a8e1')): 1, pylast.Track('Simon Curtis', 'Diablo', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44a
# OUT: ccdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 3, pylast.Track('Dow
# OUT: nplay', 'Save Me', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126
# OUT: 325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1}
from pprint import pprint
pprint(user_playcounts)
# OUT: {pylast.Track('BTS', '흥탄소년단 Boyz with Fun', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca
# OUT: 132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1,
# OUT:  pylast.Track('BTS', '상남자', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf
# OUT: 325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 4,
# OUT:  pylast.Track('Demi Lovato', 'Stop the World', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661c
# OUT: bca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1,
# OUT:  pylast.Track('Drowning Pool', 'Hell to Pay', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cb
# OUT: ca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1,
# OUT:  pylast.Track('Blood on the Dance Floor', 'Always And Forever', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca
# OUT: 5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1,
# OUT:  pylast.Track('Wontolla', 'Can You Feel Me', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbc
# OUT: a132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2,
# OUT:  pylast.Track('Downplay', 'Save Me', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc',
# OUT:  'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1,
# OUT:  pylast.Track('Fall Out Boy', "I Don't Care", pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cb
# OUT: ca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 4,
# OUT:  pylast.Track('Hinder', 'Heaven Sent', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc
# OUT: ', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1,
# OUT:  pylast.Track('Simon Curtis', 'Diablo', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132d
# OUT: c', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 3}
w
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     w
# OUT: [31m[1mNameError[0m[39m: [36mname 'w' is not defined[39m
library_sample = list(airin_library)[:50]
user_playcounts = {track: track.get_userplaycount() for track in library_sample}
import time
def time_run(func, **kwargs):
    start_time = time.time()
    pass

def time_run():
    start_time = time.time()
    user_playcounts = {track: track.get_userplaycount() for track in library_sample}
    print(f'Elapsed Time: {time.time() - start_time}')
    return user_playcounts

user_playcounts = time_run()
# OUT: Elapsed Time: 24.188222408294678
library_sample = list(airin_library)[:100]
user_playcounts = time_run()
# OUT: Elapsed Time: 47.86662530899048
elapsed_time = 47.86662530899048
print(f'Elapsed Time: {elapsed_time:.2f}')
# OUT: Elapsed Time: 47.87
len(library_sample) / elapsed_time
# OUT: 2.0891382953044246
_
# OUT: 2.0891382953044246
track_time = _
track_time
# OUT: 2.0891382953044246
track_time * 15279
# OUT: 31919.944013956305
import datetime
long_ass_time = datetime.datetime(second=_)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     long_ass_time = datetime.datetime(second=_)
# OUT: [31m[1mTypeError[0m[39m: [36mRequired argument 'year' (pos 1) not found[39m
holy_shit = track_time * 15279
long_ass_time = datetime.time(hour=0, second=holy_shit)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     long_ass_time = datetime.time(hour=0, second=holy_shit)
# OUT: [31m[1mTypeError[0m[39m: [36minteger argument expected, got float[39m
long_ass_time = datetime.time(hour=0, second=int(holy_shit))
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     long_ass_time = datetime.time(hour=0, second=int(holy_shit))
# OUT: [31m[1mValueError[0m[39m: [36msecond must be in 0..59[39m
1 + 1
# OUT: 2
'1' + '1'
# OUT: '11'
'a' + 'b'
# OUT: 'ab'
holy_shit
# OUT: 31919.944013956305
user_playcounts[0]
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     user_playcounts[0]
# OUT: [31m[1mKeyError[0m[39m: [36m0[39m
type(user_playcounts)
# OUT: <class 'dict'>
type(airin_library)
# OUT: <class 'set'>
user_playcounts[list(airin_library)[0]]
# OUT: 1
user_playcounts
# OUT: {pylast.Track('BTS', '흥탄소년단 Boyz with Fun', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca
# OUT: 132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Wontolla', 'Can 
# OUT: You Feel Me', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bb
# OUT: ff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('Fall Out Boy', "I Don't Care", pylast.LastFMNe
# OUT: twork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '
# OUT: 077a7d34313a55bdaaa02b9a8785a8e1')): 4, pylast.Track('BTS', '상남자', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e990
# OUT: 5ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 4, pylast.
# OUT: Track('Demi Lovato', 'Stop the World', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc
# OUT: ', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Blood on the Dance Fl
# OUT: oor', 'Always And Forever', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf
# OUT: 325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Hinder', 'Heaven Sent', pylast.L
# OUT: astFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomw
# OUT: olf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Drowning Pool', 'Hell to Pay', pylast.LastFMNetwork('b0a63048f832f69
# OUT: 173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b
# OUT: 9a8785a8e1')): 1, pylast.Track('Simon Curtis', 'Diablo', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44a
# OUT: ccdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 3, pylast.Track('Dow
# OUT: nplay', 'Save Me', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126
# OUT: 325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('FFH', 'Undone', pylast.LastFMNetwork('b0a
# OUT: 63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d3431
# OUT: 3a55bdaaa02b9a8785a8e1')): 1, pylast.Track('B.A.P', 'Hurricane', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905c
# OUT: a5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Tr
# OUT: ack('Miss May I', 'I.H.E.', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf
# OUT: 325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('For Today', 'Fight the Silence',
# OUT:  pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88',
# OUT:  'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 6, pylast.Track('Ryan Paris', 'Broke', pylast.LastFMNetwork('b0a63048f832f69
# OUT: 173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b
# OUT: 9a8785a8e1')): 1, pylast.Track('Brett Eldredge', "Baby, It's Cold Outside (feat. Meghan Trainor)", pylast.LastFMNetwork('b0a63048
# OUT: f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55b
# OUT: daaa02b9a8785a8e1')): 1, pylast.Track('The All-American Rejects', 'Move Along', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cd
# OUT: aa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')
# OUT: ): 1, pylast.Track('Nightcore', 'Mother Murder', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf66
# OUT: 1cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 3, pylast.Track('Countess Co
# OUT: loratura', 'The Spectacle', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf
# OUT: 325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Papa Roach', 'Alive', pylast.Las
# OUT: tFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwol
# OUT: f', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Rite Hook', 'Cross the Line', pylast.LastFMNetwork('b0a63048f832f69173
# OUT: a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8
# OUT: 785a8e1')): 1, pylast.Track('Bullet for My Valentine', 'A Place Where You Belong', pylast.LastFMNetwork('b0a63048f832f69173a58a6e
# OUT: 1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e
# OUT: 1')): 1, pylast.Track('Panic! at the Disco', 'LA Devotee', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b4
# OUT: 4accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('B
# OUT: rennan Heart', 'Fight The Resistance', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc
# OUT: ', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Shinedown', 'Devour',
# OUT:  pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88',
# OUT:  'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Stitched Up Heart', 'Monster', pylast.LastFMNetwork('b0a630
# OUT: 48f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a5
# OUT: 5bdaaa02b9a8785a8e1')): 1, pylast.Track('Logical Terror', 'Ashes of Fate', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666
# OUT: ', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1,
# OUT:  pylast.Track('The Wombats', 'Is This Christmas? - Radio Edit', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca
# OUT: 5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Tra
# OUT: ck('Little Mix', 'Move', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325
# OUT: b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Skillet', 'Monster', pylast.LastFMN
# OUT: etwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', 
# OUT: '077a7d34313a55bdaaa02b9a8785a8e1')): 9, pylast.Track('Ledinsky', 'DonaldTrumpMakesMeWannaSmokeCrack - Pfannenstill Remix', pylas
# OUT: t.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisd
# OUT: omwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('Nightcore', 'Witchcraft', pylast.LastFMNetwork('b0a63048f832f6917
# OUT: 3a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a
# OUT: 8785a8e1')): 2, pylast.Track('Boiling Point', 'Put Your Hands Up', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e990
# OUT: 5ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.
# OUT: Track('Hinder', 'All American Nightmare', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca13
# OUT: 2dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('Simon Curtis', 'I 
# OUT: Hate U', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff106
# OUT: 1dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('Ashes of Soma', 'Meteor', pylast.LastFMNetwork('b0a
# OUT: 63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d3431
# OUT: 3a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Klaton', 'Kill The Sound', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', '
# OUT: e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pyl
# OUT: ast.Track('Simon Curtis', 'Joshua', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 
# OUT: 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Breaking Benjamin', 'So 
# OUT: Cold', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061d
# OUT: fd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Eisbrecher', 'Zwischen uns', pylast.LastFMNetwork('b0
# OUT: a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d343
# OUT: 13a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Slipknot', 'Psychosocial', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 
# OUT: 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 5, py
# OUT: last.Track('Panic! at the Disco', 'Death of a Bachelor', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44a
# OUT: ccdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Twi
# OUT: light Sparkle', 'The Midnight in Me', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc'
# OUT: , 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Devour The Day', 'Blac
# OUT: kout', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061d
# OUT: fd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 8, pylast.Track('Eminem', 'Like Toy Soldiers', pylast.LastFMNetwork('b
# OUT: 0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34
# OUT: 313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Fireflight', 'Unbreakable', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666'
# OUT: , 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, 
# OUT: pylast.Track('Asking Alexandria', 'Here I Am', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661c
# OUT: bca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Escape the Fa
# OUT: te', 'This War Is Ours (The Guillotine II)', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbc
# OUT: a132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Papa Roach', 'L
# OUT: eader of the Broken Hearts', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1ac
# OUT: f325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Semargl', 'Credo Revolution', p
# OUT: ylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', '
# OUT: wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('All Good Things', 'Get Up', pylast.LastFMNetwork('b0a63048f83
# OUT: 2f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaa
# OUT: a02b9a8785a8e1')): 2, pylast.Track('Bullet for My Valentine', 'Hand of Blood', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cda
# OUT: a666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1'))
# OUT: : 3, pylast.Track('Blue Stahli', 'Not Over Til We Say So', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b4
# OUT: 4accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('G
# OUT: emini Syndrome', 'Stardust', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1ac
# OUT: f325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 8, pylast.Track('The Dazzlings', 'Under Our Spel
# OUT: l', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd8
# OUT: 8', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 5, pylast.Track('Simon Curtis', "Don't Dance", pylast.LastFMNetwork('b0a6
# OUT: 3048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313
# OUT: a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Nature Sounds', 'Storm 2', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e
# OUT: 9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 3, pyla
# OUT: st.Track('Bullet for My Valentine', 'Raising Hell', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcd
# OUT: f661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Black Ve
# OUT: il Brides', 'In The End', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf32
# OUT: 5b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 12, pylast.Track('Bullet for My Valentine', 'Beggin
# OUT: g for Mercy', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bb
# OUT: ff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('Falling in Reverse', 'Good Girls Bad Guys', py
# OUT: last.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'w
# OUT: isdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Bob Carlisle', 'One Man Revival', pylast.LastFMNetwork('b0a630
# OUT: 48f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a5
# OUT: 5bdaaa02b9a8785a8e1')): 5, pylast.Track('NeverWake', 'Monster of My Own', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666'
# OUT: , 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, 
# OUT: pylast.Track('Rise Against', 'A Beautiful Indifference', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44a
# OUT: ccdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Rai
# OUT: n Sounds', 'Relaxing Rain', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf
# OUT: 325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 3, pylast.Track('Bob Carlisle', 'It Is Well With 
# OUT: My Soul', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff10
# OUT: 61dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 4, pylast.Track('Mord Fustang', 'Super Meat Freeze', pylast.LastFMN
# OUT: etwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', 
# OUT: '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Nhato', 'Past & Then - Original Mix', pylast.LastFMNetwork('b0a63048f832f6
# OUT: 9173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02
# OUT: b9a8785a8e1')): 1, pylast.Track('BMike', '2 Faces (feat. Maribelle)', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e
# OUT: 9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pyla
# OUT: st.Track('Bob Carlisle', 'Living Water', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132
# OUT: dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 4, pylast.Track('Thousand Foot Krutc
# OUT: h', 'War of Change', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a1
# OUT: 26325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 6, pylast.Track('Stephen Walking', 'Birthday Cake', pyla
# OUT: st.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wis
# OUT: domwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('B.A.P', 'No Mercy - Rap Version', pylast.LastFMNetwork('b0a63048
# OUT: f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55b
# OUT: daaa02b9a8785a8e1')): 3, pylast.Track('Amaranthe', 'Dynamite', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5
# OUT: b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Trac
# OUT: k('Diana Krall', 'Jingle Bells', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4
# OUT: c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Bullet for My Valentine', '
# OUT: Take It Out On Me', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a12
# OUT: 6325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('American Wolves', 'Part of Me', pylast.L
# OUT: astFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomw
# OUT: olf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Dabin', 'Velvet Room - Original Mix', pylast.LastFMNetwork('b0a63048
# OUT: f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55b
# OUT: daaa02b9a8785a8e1')): 1, pylast.Track('Pop Evil', 'Welcome to Reality', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 
# OUT: 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 5, py
# OUT: last.Track('The Jackson 5', 'I Saw Mommy Kissing Santa Claus', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5
# OUT: b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Trac
# OUT: k('Crazy Frog', 'Axel F - radio mix', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc'
# OUT: , 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Bullet for My Valentin
# OUT: e', 'Broken', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bb
# OUT: ff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('Five Finger Death Punch', 'Bad Company', pylas
# OUT: t.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisd
# OUT: omwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('Nightcore', 'Out of This Town', pylast.LastFMNetwork('b0a63048f83
# OUT: 2f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaa
# OUT: a02b9a8785a8e1')): 1, pylast.Track('Daniel Ingram', 'This Day Aria', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9
# OUT: 905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylas
# OUT: t.Track('BTS', 'We On', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b
# OUT: 5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Three Days Grace', 'The Good Life', 
# OUT: pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 
# OUT: 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Sleeping with Sirens', 'F**k You', pylast.LastFMNetwork('b0a
# OUT: 63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d3431
# OUT: 3a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Fall Out Boy', "Sugar, We're Goin Down", pylast.LastFMNetwork('b0a63048f832f69173a58a
# OUT: 6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a
# OUT: 8e1')): 1, pylast.Track('Asking Alexandria', "I Won't Give In", pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca
# OUT: 5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Tra
# OUT: ck('Mister Chase', 'Fuck U Betta', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', '
# OUT: a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Skillet', 'Comatose', pyl
# OUT: ast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wi
# OUT: sdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('Simon Curtis', 'Flesh', pylast.LastFMNetwork('b0a63048f832f6917
# OUT: 3a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a
# OUT: 8785a8e1')): 2, pylast.Track('Bullet for My Valentine', 'No Way Out', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e
# OUT: 9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pyla
# OUT: st.Track('Asking Alexandria', 'Believe', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132
# OUT: dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 3, pylast.Track('Nickelback', 'Burn 
# OUT: It To The Ground', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126
# OUT: 325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 2, pylast.Track('THE END OF GRACE', 'Beneath The Waves', p
# OUT: ylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', '
# OUT: wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1, pylast.Track('We the Kings', 'Check Yes Juliet', pylast.LastFMNetwork('b0a6
# OUT: 3048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313
# OUT: a55bdaaa02b9a8785a8e1')): 3, pylast.Track('Meghan Trainor', "I'll Be Home", pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa66
# OUT: 6', 'e9905ca5b6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 1
# OUT: , pylast.Track('Five Finger Death Punch', 'Wash it All Away', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b
# OUT: 6b44accdcdf661cbca132dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1')): 9}
airin_list = list(airin_lirbrary)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     airin_list = list(airin_lirbrary)
# OUT: [31m[1mNameError[0m[39m: [36mname 'airin_lirbrary' is not defined[39m
airin_list = list(airin_library)
airin_list[0]
# OUT: pylast.Track('BTS', '흥탄소년단 Boyz with Fun', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca1
# OUT: 32dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1'))
type(_)
# OUT: <class 'pylast.Track'>
airin_list[0].title
# OUT: '흥탄소년단 Boyz with Fun'
title = _
title
# OUT: '흥탄소년단 Boyz with Fun'
with open(title, 'wb') as f:
    f.write('testing')
    

# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m2[0m[39m, in [36m<module>[39m
# OUT:     f.write('testing')
# OUT: [31m[1mTypeError[0m[39m: [36ma bytes-like object is required, not 'str'[39m
type(title)
# OUT: <class 'str'>
bytes(title)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     bytes(title)
# OUT: [31m[1mTypeError[0m[39m: [36mstring argument without an encoding[39m
title.decode()
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     title.decode()
# OUT: [31m[1mAttributeError[0m[39m: [36m'str' object has no attribute 'decode'[39m
title.encode('utf-8')
# OUT: b'\xed\x9d\xa5\xed\x83\x84\xec\x86\x8c\xeb\x85\x84\xeb\x8b\xa8 Boyz with Fun'
type(_)
# OUT: <class 'bytes'>
with open(title, 'w') as f:
    f.write('testing')
    

# OUT: 7
os.listdir()
# OUT: ['Spotipy_flask_test.py', 'wisdomwolf_unique_tracks.p', 'Smartify.py', 'pylaster.py', 'pylast_stub.py', 'worker.py', 'Procfile', 
# OUT: 'all_tracks.p', 'static', 'templates', '흥탄소년단 Boyz with Fun', '.venv', 'wisdomwolf_tracks.p', 'new_requirements.txt', '.gitignore
# OUT: ', '.git', 'runtime.txt', 'requirements.txt', 'duplicate_tracks.p', 'spotipy']
    user_playcounts = {track: track.get_userplaycount() for track in library_sample}
# OUT:   File [32m"<bpython-input-74>"[39m, line [35m[1m1[0m[39m
# OUT:     user_playcounts = {track: track.get_userplaycount() for track in library_sample}
# OUT:     ^
# OUT: [31m[1mIndentationError[0m[39m: [36munexpected indent[39m
from queue import Queue
from threading import Thread
class DownloadWorker(Thread):
    def __ini__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        while True:
            track = self.queue.get()
            save_track(track)
            self.queue.task_done()
            
        
    

def save_track(track):
    playcount = (track.title, track.get_userplaycount())
    filename = '{}.p'.format(track.title)
    with open(filename, 'wb') as f:
        pickle.dump(playcount, f)
        
    

def get_playcounts(track_list):
    ts = time.time()
    queue = Queue()
    for x in range(8):
        workter = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for track in track_list:
        queue.put(track)
    queuue.join()
    print("Took: {}".format(time.time() - ts))
    

type(library_sample)
# OUT: <class 'list'>
len(library_sample)
# OUT: 100
get_playcounts(library_sample)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     get_playcounts(library_sample)
# OUT:   File [32m"<input>"[39m, line [35m[1m5[0m[39m, in [36mget_playcounts[39m
# OUT:     workter = DownloadWorker(queue)
# OUT:   File [32m"/usr/local/lib/python3.6/threading.py"[39m, line [35m[1m780[0m[39m, in [36m__init__[39m
# OUT:     assert group is None, "group argument must be None for now"
# OUT: [31m[1mAssertionError[0m[39m: [36mgroup argument must be None for now[39m
class DownloadWorker(Thread):
    def __ini__(self, queue):
        Thread.__init__()
        self.queue = queue
        
    def run(self):
        while True:
            track = self.queue.get()
            save_track(track)
            self.queue.task_done()
            
        
    

get_playcounts(library_sample)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     get_playcounts(library_sample)
# OUT:   File [32m"<input>"[39m, line [35m[1m5[0m[39m, in [36mget_playcounts[39m
# OUT:     workter = DownloadWorker(queue)
# OUT:   File [32m"/usr/local/lib/python3.6/threading.py"[39m, line [35m[1m780[0m[39m, in [36m__init__[39m
# OUT:     assert group is None, "group argument must be None for now"
# OUT: [31m[1mAssertionError[0m[39m: [36mgroup argument must be None for now[39m
    user_playcounts = {track: track.get_userplaycount() for track in library_sample}
# OUT:   File [32m"<bpython-input-130>"[39m, line [35m[1m1[0m[39m
# OUT:     user_playcounts = {track: track.get_userplaycount() for track in library_sample}
# OUT:     ^
# OUT: [31m[1mIndentationError[0m[39m: [36munexpected indent[39m
def get_playcounts_single(track_list):
    user_playcount_dict = {}
    for track, count in map(get_track_playcount, track_list):
        user_playcount_dict[track] = count
    return user_playcount_dict

def get_track_playcount(track):
    return track.get_userplaycount()

airin_library[0]
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     airin_library[0]
# OUT: [31m[1mTypeError[0m[39m: [36m'set' object does not support indexing[39m
airin_list[0]
# OUT: pylast.Track('BTS', '흥탄소년단 Boyz with Fun', pylast.LastFMNetwork('b0a63048f832f69173a58a6e1cdaa666', 'e9905ca5b6b44accdcdf661cbca1
# OUT: 32dc', 'a4c1acf325b5a126325bbff1061dfd88', 'wisdomwolf', '077a7d34313a55bdaaa02b9a8785a8e1'))
get_track_playcount(airin_list[0])
# OUT: 1
import concurrent.futures
def get_playcounts_concurrent(track_list):
    user_playcount_dict = {}
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
            user_playcount_dict[track] = count
    return user_playcount_dict

len(airin_list)
# OUT: 859
len(library_sample)
# OUT: 100
user_playcounts = get_playcounts_concurrent(library_sample)
def get_playcounts_concurrent(track_list):
    user_playcount_dict = {}
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
            user_playcount_dict[track] = count
    print('Took: {}'.format(time.time() - start_time))
    return user_playcount_dict

user_playcounts = get_playcounts_concurrent(library_sample)
# OUT: Took: 11.68919587135315
def get_playcounts_single(track_list):
    user_playcount_dict = {}
    start_time = time.time()
    for track, count in zip(track_list, map(get_track_playcount, track_list)):
        user_playcount_dict[track] = count
    print('Took: {}'.format(time.time() - start_time))
    return user_playcount_dict

single_user_playcounts = get_playcounts_single(library_sample)
# OUT: Took: 45.193033933639526
multiprocess_user_playcounts = get_playcounts_concurrent(library_sample)
# OUT: Took: 11.571243047714233
def get_playcounts_threaded(track_list):
    user_playcount_dict = {}
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
            user_playcount_dict[track] = count
    print('Took: {}'.format(time.time() - start_time))
    return user_playcount_dict

threaded_user_playcounts = get_playcounts_threaded(library_sample)
# OUT: Took: 11.429569959640503
library_sample = list(airin_library)[:200]
threaded_user_playcounts = get_playcounts_threaded(library_sample)
# OUT: Took: 22.992125272750854
multiprocess_user_playcounts = get_playcounts_concurrent(library_sample)
# OUT: Took: 23.09409999847412
def get_playcounts_threaded(track_list):
    user_playcount_dict = {}
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
            user_playcount_dict[track] = count
    print('Took: {}'.format(time.time() - start_time))
    return user_playcount_dict

threaded_user_playcounts = get_playcounts_threaded(library_sample)
# OUT: Took: 11.215579271316528
def get_playcounts_threaded(track_list, workers=None):
    user_playcount_dict = {}
    workers = workers or 4
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
            user_playcount_dict[track] = count
    print('Took: {}'.format(time.time() - start_time))
    return user_playcount_dict

threaded_user_playcounts = get_playcounts_threaded(library_sample, 16)
# OUT: Took: 5.91062331199646
threaded_user_playcounts = get_playcounts_threaded(library_sample, 32)
# OUT: Took: 3.0859785079956055
threaded_user_playcounts = get_playcounts_threaded(airin_list, 32)
# OUT: Took: 13.0833740234375
threaded_user_playcounts[airin_list[0]]
# OUT: 1
len(threaded_user_playcounts)
# OUT: 859
user = pylast.User('wisdomwolf', network)
wisdomwolf_tracks = get_all_tracks(wisdomwolf)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     wisdomwolf_tracks = get_all_tracks(wisdomwolf)
# OUT: [31m[1mNameError[0m[39m: [36mname 'wisdomwolf' is not defined[39m
wisdomwolf_tracks = get_all_tracks(user)
# OUT: Getting chunk 1 of 62
# OUT: Getting chunk 2 of 62
# OUT: Getting chunk 3 of 62
# OUT: Getting chunk 4 of 62
# OUT: Getting chunk 5 of 62
# OUT: Getting chunk 6 of 62
# OUT: Getting chunk 7 of 62
# OUT: Getting chunk 8 of 62
# OUT: Getting chunk 9 of 62
# OUT: Getting chunk 10 of 62
# OUT: Getting chunk 11 of 62
# OUT: Getting chunk 12 of 62
# OUT: Getting chunk 13 of 62
# OUT: Getting chunk 14 of 62
# OUT: Getting chunk 15 of 62
# OUT: Getting chunk 16 of 62
# OUT: Getting chunk 17 of 62
# OUT: Getting chunk 18 of 62
# OUT: Getting chunk 19 of 62
# OUT: Getting chunk 20 of 62
# OUT: Getting chunk 21 of 62
# OUT: Getting chunk 22 of 62
# OUT: Getting chunk 23 of 62
# OUT: Getting chunk 24 of 62
# OUT: Getting chunk 25 of 62
# OUT: Getting chunk 26 of 62
# OUT: Getting chunk 27 of 62
# OUT: Getting chunk 28 of 62
# OUT: Getting chunk 29 of 62
# OUT: Getting chunk 30 of 62
# OUT: Getting chunk 31 of 62
# OUT: Getting chunk 32 of 62
# OUT: Getting chunk 33 of 62
# OUT: Getting chunk 34 of 62
# OUT: Getting chunk 35 of 62
# OUT: Getting chunk 36 of 62
# OUT: Getting chunk 37 of 62
# OUT: Getting chunk 38 of 62
# OUT: Getting chunk 39 of 62
# OUT: Getting chunk 40 of 62
# OUT: Getting chunk 41 of 62
# OUT: Getting chunk 42 of 62
# OUT: Getting chunk 43 of 62
# OUT: Getting chunk 44 of 62
# OUT: Getting chunk 45 of 62
# OUT: Getting chunk 46 of 62
# OUT: Getting chunk 47 of 62
# OUT: Getting chunk 48 of 62
# OUT: Getting chunk 49 of 62
# OUT: Getting chunk 50 of 62
# OUT: Getting chunk 51 of 62
# OUT: Getting chunk 52 of 62
# OUT: Getting chunk 53 of 62
# OUT: Getting chunk 54 of 62
# OUT: Getting chunk 55 of 62
# OUT: Getting chunk 56 of 62
# OUT: Getting chunk 57 of 62
# OUT: Getting chunk 58 of 62
# OUT: Getting chunk 59 of 62
# OUT: Getting chunk 60 of 62
# OUT: Getting chunk 61 of 62
# OUT: Getting chunk 62 of 62
wisdomwolf_library = create_library_set(wisdomwolf_tracks)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     wisdomwolf_library = create_library_set(wisdomwolf_tracks)
# OUT: [31m[1mTypeError[0m[39m: [36mcreate_library_set() missing 1 required positional argument: 'user'[39m
wisdomwolf_library = create_library_set(wisdomwolf_tracks, user)
wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, 32)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, 32)
# OUT:   File [32m"<input>"[39m, line [35m[1m6[0m[39m, in [36mget_playcounts_threaded[39m
# OUT:     for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m556[0m[39m, in [36mresult_iterator[39m
# OUT:     yield future.result()
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m400[0m[39m, in [36mresult[39m
# OUT:     self._condition.wait(timeout)
# OUT:   File [32m"/usr/local/lib/python3.6/threading.py"[39m, line [35m[1m295[0m[39m, in [36mwait[39m
# OUT:     waiter.acquire()
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/bpython/curtsiesfrontend/coderunner.py"[39m, lin
# OUT: e [35m[1m170[0m[39m, in [36msigint_handler[39m
# OUT:     raise KeyboardInterrupt()
# OUT: [31m[1mKeyboardInterrupt[0m[39m
wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, 64)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, 64)
# OUT:   File [32m"<input>"[39m, line [35m[1m6[0m[39m, in [36mget_playcounts_threaded[39m
# OUT:     for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m556[0m[39m, in [36mresult_iterator[39m
# OUT:     yield future.result()
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m398[0m[39m, in [36mresult[39m
# OUT:     return self.__get_result()
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m357[0m[39m, in [36m__get_result[39m
# OUT:     raise self._exception
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/thread.py"[39m, line [35m[1m55[0m[39m, in [36mrun[39m
# OUT:     result = self.fn(*self.args, **self.kwargs)
# OUT:   File [32m"<input>"[39m, line [35m[1m2[0m[39m, in [36mget_track_playcount[39m
# OUT:     return track.get_userplaycount()
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/pylast/__init__.py"[39m, line [35m[1m1887[0m
# OUT: [39m, in [36mget_userplaycount[39m
# OUT:     doc = self._request(self.ws_prefix + ".getInfo", True, params)
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/pylast/__init__.py"[39m, line [35m[1m1396[0m
# OUT: [39m, in [36m_request[39m
# OUT:     return _Request(self.network, method_name, params).execute(cacheable)
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/pylast/__init__.py"[39m, line [35m[1m1222[0m
# OUT: [39m, in [36mexecute[39m
# OUT:     response = self._download_response()
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/pylast/__init__.py"[39m, line [35m[1m1213[0m
# OUT: [39m, in [36m_download_response[39m
# OUT:     self._check_response_for_errors(response_text)
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/pylast/__init__.py"[39m, line [35m[1m1242[0m
# OUT: [39m, in [36m_check_response_for_errors[39m
# OUT:     raise WSError(self.network, status, details)
# OUT: [31m[1mpylast.WSError[0m[39m: [36mTrack not found[39m
wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, )
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, )
# OUT:   File [32m"<input>"[39m, line [35m[1m6[0m[39m, in [36mget_playcounts_threaded[39m
# OUT:     for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m556[0m[39m, in [36mresult_iterator[39m
# OUT:     yield future.result()
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m400[0m[39m, in [36mresult[39m
# OUT:     self._condition.wait(timeout)
# OUT:   File [32m"/usr/local/lib/python3.6/threading.py"[39m, line [35m[1m295[0m[39m, in [36mwait[39m
# OUT:     waiter.acquire()
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/bpython/curtsiesfrontend/coderunner.py"[39m, lin
# OUT: e [35m[1m170[0m[39m, in [36msigint_handler[39m
# OUT:     raise KeyboardInterrupt()
# OUT: [31m[1mKeyboardInterrupt[0m[39m
def get_track_playcount(track):
    try:
        return track.get_userplaycount()
    except pylast.WSError:
        print('Error: Unable to find info for {} - {}'.format(track.artist, track.title))
        
    

def get_track_playcount(track):
    try:
        return track.get_userplaycount()
    except pylast.WSError:
        print('Error: Unable to find info for {} - {}'.format(track.artist, track.title))
        return 0
    

wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, 64)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, 64)
# OUT:   File [32m"<input>"[39m, line [35m[1m6[0m[39m, in [36mget_playcounts_threaded[39m
# OUT:     for track, count in zip(track_list, executor.map(get_track_playcount, track_list)):
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m556[0m[39m, in [36mresult_iterator[39m
# OUT:     yield future.result()
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m398[0m[39m, in [36mresult[39m
# OUT:     return self.__get_result()
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m[1m357[0m[39m, in [36m__get_result[39m
# OUT:     raise self._exception
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/thread.py"[39m, line [35m[1m55[0m[39m, in [36mrun[39m
# OUT:     result = self.fn(*self.args, **self.kwargs)
# OUT:   File [32m"<input>"[39m, line [35m[1m5[0m[39m, in [36mget_track_playcount[39m
# OUT:     print('Error: Unable to find info for {} - {}'.format(track.artist, track.title))
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/bpython/curtsiesfrontend/coderunner.py"[39m, lin
# OUT: e [35m[1m214[0m[39m, in [36mwrite[39m
# OUT:     return self.coderunner.request_from_main_greenlet(force_refresh=True)
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/bpython/curtsiesfrontend/coderunner.py"[39m, lin
# OUT: e [35m[1m189[0m[39m, in [36mrequest_from_main_greenlet[39m
# OUT:     value = self.main_greenlet.switch(Refresh())
# OUT: [31m[1mgreenlet.error[0m[39m: [36mcannot switch to a different thread[39m
# OUT: Error: Unable to find info for Beats Working - Move Your Ass - {Scooter}
wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, 32)
# OUT: Traceback (most recent call last):
# OUT:   File [32m"<input>"[39m, line [35m[1m1[0m[39m, in [36m<module>[39m
# OUT:     wisdomwolf_playcounts = get_playcounts_threaded(wisdomwolf_library, 32)
# OUT:   File [32m"<input>"[39m, line [35m[1m6[0m[39m, in [36mget_playcounts_threade
# OUT: d[39m
# OUT:     for track, count in zip(track_list, executor.map(get_track_playcount, track_list
# OUT: )):
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m
# OUT: [1m556[0m[39m, in [36mresult_iterator[39m
# OUT:     yield future.result()
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m
# OUT: [1m398[0m[39m, in [36mresult[39m
# OUT:     return self.__get_result()
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/_base.py"[39m, line [35m
# OUT: [1m357[0m[39m, in [36m__get_result[39m
# OUT:     raise self._exception
# OUT:   File [32m"/usr/local/lib/python3.6/concurrent/futures/thread.py"[39m, line [35m
# OUT: [1m55[0m[39m, in [36mrun[39m
# OUT:     result = self.fn(*self.args, **self.kwargs)
# OUT:   File [32m"<input>"[39m, line [35m[1m5[0m[39m, in [36mget_track_playcount[3
# OUT: 9m
# OUT:     print('Error: Unable to find info for {} - {}'.format(track.artist, track.title)
# OUT: )
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/bpyt
# OUT: hon/curtsiesfrontend/coderunner.py"[39m, line [35m[1m214[0m[39m, in [36mwrite
# OUT: [39m
# OUT:     return self.coderunner.request_from_main_greenlet(force_refresh=True)
# OUT:   File [32m"/home/wisdomwolf/.virtualenvs/smartify/lib/python3.6/site-packages/bpyt
# OUT: hon/curtsiesfrontend/coderunner.py"[39m, line [35m[1m189[0m[39m, in [36mreques
# OUT: t_from_main_greenlet[39m
# OUT:     value = self.main_greenlet.switch(Refresh())
# OUT: [31m[1mgreenlet.error[0m[39m: [36mcannot switch to a different thread[39m
# OUT: Error: Unable to find info for Beats Working - Move Your Ass - {Scooter}