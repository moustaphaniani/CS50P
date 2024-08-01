'''
Program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
'''

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    # Loop
    while True:
        try:
            input_date = input("Date: ")
            output = verify_date(input_date)
            if output != False:
                print(output)
                break
        except:
            break


def verify_date(user_date):
    # Date in mm/dd/yyyy format
    if '/' in user_date:
        middle_endian_numbers = user_date.split('/')
        try:
            mm = int(middle_endian_numbers[0])
            dd = int(middle_endian_numbers[1])
            yyyy = int(middle_endian_numbers[2])
            if verify_day_month(dd, mm) is True:
                return f"{yyyy}-{mm:02}-{dd:02}"
            else:
                return False
        except:
            return False

    # Date in mmmm dd, yyyy format
    elif ',' in user_date:
        middle_endian_letters = user_date.replace(',', '').split(' ')
        try:
            yyyy = int(middle_endian_letters[2])
            dd = int(middle_endian_letters[1])
            user_month = middle_endian_letters[0]
            if user_month in months:
                mm = int(months.index(user_month)) + 1
            else:
                return False
            if verify_day_month(dd, mm) is True:
                return f"{yyyy}-{mm:02}-{dd:02}"
            else:
                return False
        except:
            return False
    # Other date format not accepted
    else:
        return False


def verify_day_month(d, m):
    if d < 1 or d > 31 or m < 1 or m > 12:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
