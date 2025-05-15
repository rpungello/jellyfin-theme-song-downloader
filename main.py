import os
import urllib.request
from urllib.error import HTTPError

from jellyfin_apiclient_python import JellyfinClient
from jellyfin_apiclient_python.exceptions import HTTPException

client = JellyfinClient()
client.config.data['app.name']='Theme Song Downloader'
client.config.data['app.version']=os.environ['APP_VERSION']
client.config.data['auth.ssl'] = False
client.authenticate({
    "Servers": [
        {
            "address": os.environ['JELLYFIN_ADDRESS'],
            "AccessToken": os.environ['JELLYFIN_TOKEN'],
            "UserId": os.environ['JELLYFIN_USER_ID']
        }
    ]
}, discover=False)

try:
    shows = client.jellyfin.user_items(params={
        "parentId": os.environ['JELLYFIN_SHOWS_ID'],
    })
except HTTPException as e:
    print('Unable to connect to Jellyfin server. Did you set the environment variables correctly?')
    exit()


def download_theme_song(show: dict):
        theme_path = f"/mnt/shows/{os.path.basename(show['Path'])}/theme.mp3"
        theme_url = f"http://tvthemes.plexapp.com/{show['ProviderIds']['Tvdb']}.mp3"
        if os.path.exists(os.path.dirname(theme_path)):
            print(f"Downloading theme song for {show['Name']}.")
            try:
                urllib.request.urlretrieve(theme_url, theme_path)
            except HTTPError:
                print(f"No theme song found for {show['Name']}.")
        else:
            print(f"Directory does not exist for {show['Name']}, skipping download.")


for record in shows['Items']:
    song = client.jellyfin.get_items_theme_song(record['Id'])
    if song['TotalRecordCount'] == 0:
        info = client.jellyfin.get_item(record['Id'])
        if 'ProviderIds' in info and 'Tvdb' in info['ProviderIds']:
            download_theme_song(info)