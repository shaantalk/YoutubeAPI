import os
import isodate
import requests
from helperFunctions import human_readable_time

# Description : Takes playlist id and calculate duration


def calculate_playlist_duration(api_key, base_url, playlist_id):
    try:

        sum_duration = 0

        videos = []

        next_page_token = None

        playlist_length = get_number_of_videos_in_playlist(
            base_url,
            api_key,
            playlist_id,
            next_page_token
        )

        total_fetched_videos = 0

        while total_fetched_videos != playlist_length:

            # Comma seperated ids of upto 50 videos => "ID_1,ID_2,ID_3...."
            current_page_video_ids, next_page_token, num_videos_in_current_page = get_current_page_video_ids(
                base_url,
                api_key,
                playlist_id,
                next_page_token
            )

            # Updating the number of videos fetched
            total_fetched_videos += num_videos_in_current_page

            # Fetching details of the above 50 videos like id,title etc
            arr_video_details = get_details_of_videos(
                base_url,
                api_key,
                current_page_video_ids
            )

            for details_of_a_video in arr_video_details:

                # Destructuring the video details that we need from each video
                id = details_of_a_video['id']
                title = details_of_a_video['snippet']['title']
                duration = isodate.parse_duration(
                    details_of_a_video['contentDetails']['duration']
                ).total_seconds()

                # Adding current video details to the list of fetched videos
                videos.append((id, title, human_readable_time(duration)))

                # Adding current video duration to the sum of all video duration
                sum_duration += duration

            # Last page's next_page_token will be None
            if not next_page_token:
                return {'videos': videos, 'duration': human_readable_time(sum_duration)}

    except Exception as e:
        print(e)


# Description : returns the length of playlist i.e. total number of videos in playlist

def get_number_of_videos_in_playlist(base_url, api_key, playlist_id, next_page_token):
    playlist_items_list_url = base_url + '/playlistItems'
    playlist_api_params = {
        'key': api_key,
        'part': 'contentDetails',
        'playlistId': playlist_id,
        'maxResults': 50,
        'pageToken': next_page_token
    }
    response = requests.get(
        url=playlist_items_list_url,
        params=playlist_api_params
    ).json()

    return int(response['pageInfo']['totalResults'])

# Descpription : returns comma seperated video ids in a page of playlist items api


def get_current_page_video_ids(base_url, api_key, playlist_id, next_page_token):
    playlist_items_list_url = base_url + '/playlistItems'
    playlist_api_params = {
        'key': api_key,
        'part': 'contentDetails',
        'playlistId': playlist_id,
        'maxResults': 50,
        'pageToken': next_page_token
    }
    response = requests.get(
        url=playlist_items_list_url,
        params=playlist_api_params
    ).json()

    current_page_video_ids = [
        item['contentDetails']['videoId'] for item in response['items']
    ]

    str_curr_page_videos = ','.join(current_page_video_ids)

    # Last page in playlistItems api will not have the nextPageToken key hence default value is None
    next_page_token = response.get('nextPageToken', None)

    # Number of videos in current page
    num = len(current_page_video_ids)

    return str_curr_page_videos, next_page_token, num


# Description : Takes in comma seperated list of video ids and returns details of all videos like title and duration.
def get_details_of_videos(base_url, api_key, current_page_video_ids):

    videos_list_url = base_url + '/videos'
    videos_list_params = {
        'key': api_key,
        'part': "snippet,contentDetails,id",
        'id': current_page_video_ids
    }
    response = requests.get(
        url=videos_list_url,
        params=videos_list_params
    ).json()

    return response['items']
