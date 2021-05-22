from itertools import chain, repeat
from helper.functions import get_playlist_id


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
