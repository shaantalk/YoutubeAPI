# Description : Formats the duration of youtube playlist to human readable format


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
