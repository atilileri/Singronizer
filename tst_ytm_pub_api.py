"""test youtube music public."""

import pprint
from ytmusicapi import YTMusic

yt = YTMusic("oauth.json")
playlistId = yt.create_playlist("test", "test description")
search_results = yt.search("Oasis Wonderwall")
pprint.pprint(search_results)
# yt.add_playlist_items(playlistId, [search_results[0]["videoId"]])
