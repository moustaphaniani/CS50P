import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if depart := re.search(r"^(\d+):*(\d\d)* (A|P)M to (\d+):*(\d\d)* (A|P)M$", s):
        if 1 >= int(depart[1]) >= 12 or 1 >= int(depart[4]) >= 12:
            raise ValueError
        else:
            try:
                start_hour = time_to_24(depart[1], depart[2], depart[3])
                finish_hour = time_to_24(depart[4], depart[5], depart[6])
                return start_hour + ' to ' + finish_hour
            except:
                raise ValueError
    else:
        raise ValueError


def time_to_24(hour, min, ampm):
    # Return AM to 24
    # Hour in first place
    if ampm == 'A' and hour == '12':
        hour_in_24 = '00'
    elif ampm == 'A':
        hour_in_24 = str(f"{int(hour):02d}")
    elif ampm == 'P' and hour == '12':
        hour_in_24 = '12'
    elif ampm == 'P':
        hour_in_24 = str(int(hour) + 12)
    else:
        raise ValueError
    # Add minutes if any
    if min is None:
        hour_in_24 = hour_in_24 + ':00'
    elif min is not None and 0 <= int(min) <= 59:
        hour_in_24 = hour_in_24 + ':' + min
    else:
        raise ValueError
    return hour_in_24


if __name__ == "__main__":
    main()
