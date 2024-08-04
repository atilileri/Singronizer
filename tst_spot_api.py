"""test spotify API."""

# todo - this only gets track info, extend in the future

import platforms.spotify_handler

print('##START')  # todo - remove after debug

if __name__ == '__main__':

    print("Hello")
    print()

    sh = platforms.spotify_handler.SpotifyHandler()
    print('Getting Playlists...')
    playlist_ids, playlist_names = sh.get_user_playlist_ids()

    assert playlist_ids

    playlist_ids = [playlist_ids[playlist_names.index('Yorgun')]] # todo - remove after debug

    for i, (p_id, name) in enumerate(zip(playlist_ids, playlist_names)):
        print(f"   {i+1:2d} {name:40s} {p_id}")

    print('Listing Tracks...')
    for pl_id in playlist_ids:
        tracks = sh.get_tracks(playlist_id=pl_id)
        assert tracks
        tracks = tracks[0:6]  # todo - remove after debug

        for i, tr in enumerate(tracks):
            print(f"   {i+1} {tr['artists'][0]['name']:32.32s} {tr['name']}")
