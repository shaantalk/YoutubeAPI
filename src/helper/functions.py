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
