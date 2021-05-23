import isodate
import requests
from helperFunctions import human_readable_time

# ------------------------------------------------------------------------------------------------------------------
# Function Name : CalculateDuration
# Description : Calculate duration
# ------------------------------------------------------------------------------------------------------------------


def calculate_playlist_duration(playlist_id):
    try:
        api_key = 'AIzaSyBhJ1XmmRl9aON9Q1J-GPVC-MOKOybGEh4'

        sumDuration = 0

        videos = []

        nextPageToken = None
        while True:
            # API : https://developers.google.com/youtube/v3/docs/playlistItems/list?apix=true
            playlist_items_list_url = 'https://youtube.googleapis.com/youtube/v3/playlistItems'
            playlist_api_params = {
                'key': api_key,
                'part': 'contentDetails',
                'playlistId': playlist_id,
                'maxResults': 50,
                'pageToken': nextPageToken
            }
            playlist_page = requests.get(
                url=playlist_items_list_url, params=playlist_api_params).json()

            # print('Playlist Page', playlist_page)

            video_ids = [item['contentDetails']['videoId']
                         for item in playlist_page['items']]

            # print('Video IDs', video_ids)

            # API : https://developers.google.com/youtube/v3/docs/videos/list
            videos_list_url = 'https://youtube.googleapis.com/youtube/v3/videos'
            videos_list_params = {
                'key': api_key,
                'part': "snippet,contentDetails,id",
                'id': ','.join(video_ids)
            }

            video_items = requests.get(
                url=videos_list_url, params=videos_list_params).json()['items']
            # video_items = video_req.json()

            # print('Video Items', video_items['items'])

            for video in video_items:
                id = video['id']
                link = 'https://www.youtube.com/watch?v='+video['id']
                title = video['snippet']['title']
                duration = isodate.parse_duration(
                    video['contentDetails']['duration']).total_seconds()

                videos.append((id, link, title, human_readable_time(duration)))
                sumDuration += duration

            # Last page in playlist.list api will not have the nextPageToken key
            try:
                nextPageToken = playlist_page['nextPageToken']
            except KeyError:
                nextPageToken = None

            if not nextPageToken:
                return {'videos': videos, 'duration': human_readable_time(sumDuration)}
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------
