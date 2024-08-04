import platforms
import pprint
import os

print('##START') # todo - remove after debug

if __name__ == '__main__':

    print("Hello")
    print()
    
    sh = platforms.SpotifyHandler.SpotifyHandler()
    print('Getting Playlists...')
    playlist_ids = sh.get_user_playlist_ids()

    assert(playlist_ids)
    
    print('Listing Tracks...')
    for pl_id in playlist_ids:
        tracks = sh.get_tracks(playlist_id=pl_id)
        tracks = tracks[0:6] # todo - remove after debug
        # pprint.pprint(tracks[0])

        for i, tr in enumerate(tracks):
            print(
                "   %d %32.32s %s" %
                (i+1, tr['artists'][0]['name'], tr['name']))
