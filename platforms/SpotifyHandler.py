# todo - add docstr

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from typing import List # for type hinting

class SpotifyHandler(object):
    
    def __init__(self) -> None:
        self._scope = 'playlist-read-private'
        self._sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self._scope,
                                                             open_browser=False))
        self._user_id = self._sp.me()['id']
    
    def get_user_playlist_ids(self) -> List[str]:
        offset = 0
        pl_ids = list()
        while True: # there is a limit per req. so we loop
            response = self._sp.current_user_playlists(offset=offset) # todo - add fields filter param
            
            if len(response['items']) == 0: break # when none or done
            
            for playlist in response['items']: # todo - more pythonic
                if playlist['owner']['id'] == self._user_id:
                    if (playlist['name'] == 'Yorgun'): # todo - remove after debugging
                        pl_ids.append(playlist['id'])
                    
            offset = offset + len(response['items'])
        
        return pl_ids
    
    def get_tracks(self, playlist_id):
        offset = 0
        tracks = list()
        while True:
            response = self._sp.playlist_items(playlist_id=playlist_id,
                                            offset=offset,
                                            additional_types=['track'])

            if len(response['items']) == 0: break
        
            # we don't need spotify related stats for each track,
            # so strip them
            tracks.extend(item['track'] for item in response['items'])

            offset = offset + len(response['items'])
            
        return tracks

