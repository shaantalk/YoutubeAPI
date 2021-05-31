from inputFunctions import *
from youtubeFunctions import *
from outputFunctions import *


def main():
    api_key = os.environ.get('YOUTUBE_API_KEY')
    base_url = 'https://youtube.googleapis.com/youtube/v3'

    playlist_id = input("Enter playlist id : ")
    output_format = get_output_format_from_user()
    result = calculate_playlist_duration(api_key, base_url, playlist_id)

    if output_format == 'Print in Console':
        output_in_console(result)
    elif output_format == 'Excel File':
        output_in_excel_file(result)
    elif output_format == 'Text File':
        output_in_txt_file(result)
    elif output_format == 'All':
        output_in_console(result)
        output_in_excel_file(result)
        output_in_txt_file(result)

    print("Done")


if __name__ == "__main__":
    main()
