# Jellyfin Theme Song Downloader

## Environment Setup
```dotenv
JELLYFIN_ADDRESS= # IP or hostname of Jellyfin server
JELLYFIN_TOKEN= # API token created from Jellyfin admin dashboard
JELLYFIN_USER_ID= # User ID of the user to use for API calls
JELLYFIN_SHOWS_ID= # Library ID of the TV shows library to search for theme songs
```
## Running
```bash
docker run --env-file .env -v /path/to/shows:/mnt/shows rpungello/jellyfin-theme-song-downloader:latest
```