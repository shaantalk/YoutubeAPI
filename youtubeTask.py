import isodate
import tableprint
import xlsxwriter
import tableprint as tp
from itertools import chain, repeat
from googleapiclient.discovery import build


# ------------------------------------------------------------------------------------------------------------------
# Function Name : get_playlist_id
# Description : Returns playlist_id or none
# Unit Tests : Done
# www.youtube.com/watch?v=g4Fny0Zz5j8&list=PLkcctaU57y5ctgdK18QBThxJ8G4mB9q-u
# ------------------------------------------------------------------------------------------------------------------

def get_playlist_id(playlist_url):
    try:
        id = playlist_url.split('&list=')[1].split(
            '&')[0] if playlist_url.find('&list=') != -1 else None
        return id
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Function Name : get_playlist_link_from_user
# Description : Takes input from user with 3 max tries, checks if it is a playlist link
# ------------------------------------------------------------------------------------------------------------------


def get_playlist_link_from_user():
    try:
        prompts = chain(["Enter playlist link : "], repeat(
            "Not a playlist! Try again : ", 2))
        replies = map(input, prompts)

        valid_link = next(filter(get_playlist_id, replies), None)

        if valid_link:
            playlist_id = get_playlist_id(valid_link)
            print('Playlist ID : ' + playlist_id)
            return playlist_id
        else:
            print('Max tries over!')
            exit()
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Function Name : get_output_format_from_user
# Description : Gets the output format from user
# ------------------------------------------------------------------------------------------------------------------


def get_output_format_from_user():
    try:
        prompts = chain(["Enter 1 for console print, 2 for excel, 3 for txt file and 4 for all : "], repeat(
            "Wrong option! Try again : ", 2))
        replies = map(input, prompts)
        valid_response = next(filter(lambda option: option in [
            '1', '2', '3', '4'], replies), None)

        if valid_response:
            print('Output Format : ' + {
                '1': 'Print in Console',
                '2': 'Excel File',
                '3': 'Text File',
                '4': 'All'
            }[valid_response])

            return {
                '1': 'Print in Console',
                '2': 'Excel File',
                '3': 'Text File',
                '4': 'All'
            }[valid_response]
        else:
            print('Max tries over!')
            exit()
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Function Name : human_readable_time
# Description : Formats the duration of youtube playlist to human readable format
# ------------------------------------------------------------------------------------------------------------------


def human_readable_time(seconds):
    try:
        seconds = int(seconds)
        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        if days > 0:
            return '%d days %d hours %d mins %d secs' % (days, hours, minutes, seconds)
        elif hours > 0:
            return '%d hours %d mins %d secs' % (hours, minutes, seconds)
        elif minutes > 0:
            return '%d mins %d secs' % (minutes, seconds)
        else:
            return '%d secs' % (seconds,)
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------

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
# Function Name : output_in_console
# Description : Output in console
# ------------------------------------------------------------------------------------------------------------------
def output_in_console(result):
    try:
        headers = ['ID', 'Link', 'Title', 'Duration']
        width = [15, 45, 80, 15]

        tableprint.table(result['videos'], headers, width=width)

        print("Total Duration : ", result['duration'])
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Function Name : output_in_txt_file
# Description : Output in text file
# ------------------------------------------------------------------------------------------------------------------


def output_in_txt_file(result):
    try:
        f = open("Output.txt", "w+")

        for video in result['videos']:
            f.write('ID : '+video[0]+'\n')
            f.write('Link : '+video[1]+'\n')
            f.write('Title : '+video[2]+'\n')
            f.write('Duration : '+video[3]+'\n')
            f.write('\n\n')

        f.write('Total Duration : '+result['duration'])

        f.close()
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Function Name : output_in_excel_file
# Description : Output in excel file
# ------------------------------------------------------------------------------------------------------------------


def output_in_excel_file(result):
    try:
        workbook = xlsxwriter.Workbook('Output.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write_row(0, 1, ['Total Duration', result['duration']])

        options = {'data': result['videos'],
                   'name': 'Videos',
                   'autofilter': False,
                   'columns': [
            {'header': 'ID'},
            {'header': 'Link'},
            {'header': 'Title'},
            {'header': 'Duration'},
        ]
        }

        worksheet.add_table('A4:D'+str(len(result['videos'])+4), options)

        workbook.close()
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
# Function : main
# ------------------------------------------------------------------------------------------------------------------
def main():
    playlist_id = get_playlist_link_from_user()
    output_format = get_output_format_from_user()
    result = calculate_playlist_duration(playlist_id)
    if output_format == 'Print in Console':
        output_in_console(result)
    elif output_format == 'Print in Console':
        output_in_excel_file(result)
    elif output_format == 'Print in Console':
        output_in_txt_file(result)
    elif output_format == 'All':
        output_in_console(result)
        output_in_excel_file(result)
        output_in_txt_file(result)

    print("Done")


if __name__ == "__main__":
    main()
