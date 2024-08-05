"""test end to end functionality."""

from io import BytesIO

import numpy as np
import requests
from PIL import Image
from ytmusicapi import YTMusic
import platforms.spotify_handler
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

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
    tracks = tracks[0:1]  # todo - remove after debug

    for i, tr in enumerate(tracks):
        print(f"   {i+1} {tr['artists'][0]['name']:32.32s} {tr['name']}")

spot_track = tracks[0]

print("Search on YTMusic...")
yt = YTMusic("oauth.json")

query = f"{spot_track['artists'][0]['name']} - {spot_track['name']}"

response = requests.get(spot_track["album"]["images"][-1]["url"], timeout=60)
spot_img = Image.open(BytesIO(response.content)).resize((60, 60)).convert("L")

for yt_track in yt.search(query=query)[0:5]:
    response = requests.get(yt_track["thumbnails"][0]["url"], timeout=60)
    ytm_img = Image.open(BytesIO(response.content)).resize((60, 60)).convert("L")

    mse = np.mean((np.array(spot_img) - np.array(ytm_img)) ** 2)
    print(f"MSE: {mse}")

    fig = plt.figure(figsize=(4, 8))

    gs = GridSpec(1, 2)
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])

    ax0.imshow(spot_img, cmap="gray")
    ax0.set_title("Spot")
    ax1.imshow(ytm_img, cmap="gray")
    ax1.set_title("YTM" + f" MSE: {mse}")

    for a in (ax0, ax1):
        a.set_axis_off()

    fig.tight_layout()
    plt.show()
