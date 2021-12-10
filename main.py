import sys
from validators import validate, is_time_later_than_now


def calculate_cron(line, time):
    hour, minute = time.split(":")
    cron_min, cron_hour, path = line.split(" ")

    day = "today"
    time_is_still_available_today = is_time_later_than_now(hour, minute)
    if cron_min == '*' and cron_hour == '*':  # * *
        if not time_is_still_available_today:
            day ="tomorrow"
        return f"{time} {day} - {path}"

    if cron_min != '*' and cron_hour == '*':  # 45 *
        if not time_is_still_available_today:
            day = "tomorrow"
        return f"{hour}:{cron_min} {day} - {path}"

    if cron_min != '*' and cron_hour != '*':  # 30 1
        if not time_is_still_available_today:
            day = "tomorrow"
        elif int(cron_hour) > int(hour):
            day = "today"
        else:
            day = "tomorrow"
        return f"{cron_hour}:{cron_min} {day} - {path}"

    if cron_min == '*' and cron_hour != '*':  # * 19
        if not time_is_still_available_today:
            day = "tomorrow"
        elif int(cron_hour) > int(hour):
            day = "today"
        else:
            day = "tomorrow"
        return f"{cron_hour}:00 {day} - {path}"


def minicron():
    if len(sys.argv[1:]) != 1:
        print({"Error": "Try running 'python main.py HH:mm' "})
    else:
        passed_value_validated = validate(sys.argv[1])

        if not passed_value_validated:
            print({"Error": "Incorrect Time Format. Try passing time in HH:mm"})
        else:
            time = sys.argv[1]
            output = []
            config = sys.stdin.read().split("\n")
            for line in config:
                output.append(calculate_cron(line, time))
            print("\n".join(output))


if __name__ == '__main__':
    minicron()

