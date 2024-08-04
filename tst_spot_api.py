import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

print('##START')

scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

searchPlName = 'Yorgun'
plId = None

print('Searching Playlists...')
offset = 0
while True: # get playlists
    response = sp.current_user_playlists(offset=offset)
    
    if len(response['items']) == 0:
        break

    for idx, item in enumerate(response['items']):
        print("%d / %d - %s" % (offset + idx+1, response['total'], item['name']), end='')
        if (item['name'] == searchPlName):
            print(' ======>>> Found', end='')
            plId = item['id']
            pprint.pprint(item)
            # break
        print('')
    
    offset = offset + len(response['items'])

assert(plId)
offset = 0
while True:
    response = sp.playlist_items(plId,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])

    if len(response['items']) == 0:
        break

    pprint.pprint(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])

# import spotipy
# from spotipy.oauth2 import SpotifyOAuth


# def show_tracks(results):
#     for i, item in enumerate(results['items']):
#         track = item['track']
#         print(
#             "   %d %32.32s %s" %
#             (i, track['artists'][0]['name'], track['name']))


# if __name__ == '__main__':
#     scope = 'playlist-read-private'
#     sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#     playlists = sp.current_user_playlists()
#     user_id = sp.me()['id']

#     for playlist in playlists['items']:
#         if playlist['owner']['id'] == user_id:
#             print()
#             print(playlist['name'])
#             print('  total tracks', playlist['tracks']['total'])

#             tracks = sp.playlist_items(playlist['id'], fields="items,next", additional_types=('tracks', ))
#             show_tracks(tracks)

#             while tracks['next']:
#                 tracks = sp.next(tracks)
#                 show_tracks(tracks)

print('##FIN')