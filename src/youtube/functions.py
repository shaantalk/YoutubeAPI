import isodate
from googleapiclient.discovery import build
from helper.functions import human_readable_time

# ------------------------------------------------------------------------------------------------------------------
# Function Name : CalculateDuration
# Description : Calculate duration
# ------------------------------------------------------------------------------------------------------------------


def calculate_playlist_duration(playlist_id):
    try:
        api_key = 'AIzaSyBhJ1XmmRl9aON9Q1J-GPVC-MOKOybGEh4'

        youtube = build('youtube', 'v3', developerKey=api_key)

        sumDuration = 0

        videos = []

        nextPageToken = None
        while True:
            # API : https://developers.google.com/youtube/v3/docs/playlistItems/list?apix=true
            playlist_page = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=nextPageToken
            ).execute()

            video_ids = [item['contentDetails']['videoId']
                         for item in playlist_page['items']]

            # API : https://developers.google.com/youtube/v3/docs/videos/list
            video_items = youtube.videos().list(
                part="snippet,contentDetails,id",
                id=','.join(video_ids)
            ).execute()['items']

            for item in video_items:
                id = item['id']
                link = 'https://www.youtube.com/watch?v='+item['id']
                title = item['snippet']['title']
                duration = isodate.parse_duration(
                    item['contentDetails']['duration']).total_seconds()

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
