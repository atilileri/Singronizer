"""test end to end functionality."""

import datetime
from ytmusicapi import YTMusic
import platforms.spotify_handler

sh = platforms.spotify_handler.SpotifyHandler()
print("Getting My Playlists...")
playlist_ids, playlist_names = sh.get_user_playlist_ids()

assert playlist_ids

playlist_ids = [
    playlist_ids[playlist_names.index("Yorgun")]
]  # todo - remove after debug
playlist_names = [
    playlist_names[playlist_names.index("Yorgun")]
]  # todo - remove after debug

for i, (p_id, name) in enumerate(zip(playlist_ids, playlist_names)):
    print(f"   {i+1:2d} {name:40s} {p_id}")

tracks = []
print("Listing Tracks...")
for pl_id in playlist_ids:
    tracks = sh.get_tracks(playlist_id=pl_id)
    assert tracks
    tracks = tracks[0:6]  # todo - remove after debug

    for i, tr in enumerate(tracks):
        print(f"   {i+1} {tr['artists'][0]['name']:32.32s} {tr['name']}")

print("Moving to YTMusic...")
yt = YTMusic("oauth.json")
pl_name = f"Yorgun_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}"

print(f"Create playlist {pl_name}...")
# playlistId = yt.create_playlist(title=pl_name, description="singronizer")
for tr in tracks:
    query = f"{tr['artists'][0]['name']} - {tr['name']}"
    print(f"Searching... {query:60.60s}", end="")
    search_results = yt.search(query=query)
    # yt.add_playlist_items(playlistId, [search_results[0]["videoId"]])
    print("Added...")
