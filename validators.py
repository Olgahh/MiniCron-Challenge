import re
from datetime import datetime


def validate(time):
    # Regex to check valid time in 24-hour format.
    regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$"

    p = re.compile(regex)

    if time == "":
        return False

    matched_values = re.search(p, time)
    if matched_values is None:
        return False
    return True


def is_time_later_than_now(hour, minutes):
    this_time = datetime.now()
    hour_diff = this_time.hour - int(hour)
    min_diff = this_time.minute - int(minutes)
    if hour_diff < 0:
        return True
    elif hour_diff == 0 and min_diff <0:
        return True
    else:
        return False