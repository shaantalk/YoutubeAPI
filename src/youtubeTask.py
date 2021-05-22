
from input.functions import *
from youtube.functions import *
from output.functions import *

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
